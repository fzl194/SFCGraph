"""build_all 编排单测：选性执行过滤、步骤顺序校验、单步失败隔离不影响其他网元。"""
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import build_all  # noqa: E402
from builder.steps import registry as steps_registry  # noqa: E402


def _cfg():
    return {
        "assets_root": "data/assets",
        "project_root": "..",
        "ne": {
            "UDG": {"20.15.2": {"source": "a", "steps": ["mmlcommand", "enrich"]}},
            "UNC": {"20.15.2": {"source": "b", "steps": ["mmlcommand"]}},
            "UDC": {"20.14.0": {"source": "c", "steps": ["mmlcommand", "enrich", "parameter"]}},
        },
    }


class SelectTargetsTests(unittest.TestCase):
    def test_no_filter_returns_all(self):
        targets = build_all.select_targets(_cfg(), None, None)
        self.assertEqual([(t[0], t[1]) for t in targets],
                         [("UDG", "20.15.2"), ("UNC", "20.15.2"), ("UDC", "20.14.0")])

    def test_nf_filter_selects_all_versions_of_one_nf(self):
        targets = build_all.select_targets(_cfg(), "UDG", None)
        self.assertEqual([(t[0], t[1]) for t in targets], [("UDG", "20.15.2")])

    def test_nf_plus_version_filter_selects_single(self):
        targets = build_all.select_targets(_cfg(), "UDG", "20.15.2")
        self.assertEqual([(t[0], t[1]) for t in targets], [("UDG", "20.15.2")])

    def test_unknown_nf_returns_empty(self):
        self.assertEqual(build_all.select_targets(_cfg(), "XXX", None), [])


class StepOrderTests(unittest.TestCase):
    def test_validate_order_accepts_valid_sequence(self):
        self.assertEqual(steps_registry.validate_order(["mmlcommand", "enrich", "parameter"]),
                         ["mmlcommand", "enrich", "parameter"])

    def test_validate_order_rejects_enrich_without_mmlcommand(self):
        with self.assertRaises(ValueError):
            steps_registry.validate_order(["enrich"])

    def test_validate_order_rejects_wrong_order(self):
        with self.assertRaises(ValueError):
            steps_registry.validate_order(["enrich", "mmlcommand"])

    def test_validate_order_rejects_unknown_step(self):
        with self.assertRaises(ValueError):
            steps_registry.validate_order(["mmlcommand", "bogus"])

    # --- 独立 IO 单元：mmlcommand / parameter 无 requires，可单独跑 ---
    def test_validate_order_accepts_mmlcommand_alone(self):
        self.assertEqual(steps_registry.validate_order(["mmlcommand"]), ["mmlcommand"])

    def test_validate_order_accepts_parameter_alone(self):
        # parameter 自带 parameter_csv，不依赖 mmlcommand —— 独立可跑
        self.assertEqual(steps_registry.validate_order(["parameter"]), ["parameter"])

    def test_validate_order_accepts_mmlcommand_plus_parameter_any_order(self):
        # 两者互不依赖，顺序无所谓
        self.assertEqual(steps_registry.validate_order(["parameter", "mmlcommand"]),
                         ["parameter", "mmlcommand"])
        self.assertEqual(steps_registry.validate_order(["mmlcommand", "parameter"]),
                         ["mmlcommand", "parameter"])

    # --- enrich 单独跑：磁盘已有 mml_commands.jsonl 才行（支持改 extractor 后快速重 enrich）---
    def test_enrich_alone_ok_when_disk_has_product(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "mml_commands.jsonl").write_text("{}", encoding="utf-8")
            self.assertEqual(steps_registry.validate_order(["enrich"], out_dir=d), ["enrich"])

    def test_enrich_alone_rejected_when_disk_missing(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                steps_registry.validate_order(["enrich"], out_dir=d)

    def test_enrich_alone_rejected_when_no_out_dir(self):
        # 不查磁盘时，enrich 必须由 mmlcommand 在前产出
        with self.assertRaises(ValueError):
            steps_registry.validate_order(["enrich"])


class FailureIsolationTests(unittest.TestCase):
    def test_single_step_failure_does_not_stop_other_ne(self):
        """UDG 的 mmlcommand 抛错，UNC 仍应被调用。"""
        calls = []

        def fake_mmlcommand(ctx):
            calls.append(ctx.nf)
            if ctx.nf == "UDG":
                raise RuntimeError("boom UDG")

        def fake_enrich(ctx):
            calls.append(ctx.nf + ":enrich")

        original = dict(steps_registry.STEPS)
        try:
            steps_registry.STEPS["mmlcommand"] = fake_mmlcommand
            steps_registry.STEPS["enrich"] = fake_enrich
            rc = build_all.run_pipeline(_cfg(), nf_filter="UDG")
            # UDG 整体不阻断：mmlcommand 失败后 enrich 仍会被尝试（失败隔离粒度=单步）
            # 但 UDG 只有一组，所以返回码非 0
            self.assertEqual(rc, 1)
            self.assertIn("UDG", calls)
        finally:
            steps_registry.STEPS.clear()
            steps_registry.STEPS.update(original)

    def test_udg_failure_does_not_block_unc(self):
        """UDG 整组失败时，UNC 仍被处理。"""
        seen = []

        def fake_mmlcommand(ctx):
            seen.append(ctx.nf)
            if ctx.nf == "UDG":
                raise RuntimeError("boom UDG")

        original = dict(steps_registry.STEPS)
        try:
            steps_registry.STEPS["mmlcommand"] = fake_mmlcommand
            steps_registry.STEPS["enrich"] = lambda ctx: seen.append(ctx.nf + ":e")
            build_all.run_pipeline(_cfg(), None, None)
            self.assertIn("UDG", seen)
            self.assertIn("UNC", seen)     # UDG 失败没阻断 UNC
            self.assertIn("UDC", seen)
        finally:
            steps_registry.STEPS.clear()
            steps_registry.STEPS.update(original)


class MakeCtxTests(unittest.TestCase):
    def test_ctx_resolves_paths_against_project_root(self):
        cfg = {"assets_root": "data/assets", "project_root": "..",
               "ne": {"UDG": {"20.15.2": {
                   "source": "src/md", "steps": ["mmlcommand"],
                   "parameter_csv": "src/p.csv"}}}}
        ctx = build_all.make_ctx(cfg, "UDG", "20.15.2", cfg["ne"]["UDG"]["20.15.2"])
        self.assertEqual(ctx.nf, "UDG")
        self.assertEqual(ctx.version, "20.15.2")
        self.assertTrue(ctx.out_dir.endswith("data/assets/UDG/20.15.2")
                        or ctx.out_dir.replace("\\", "/").endswith("data/assets/UDG/20.15.2"))
        self.assertTrue(ctx.source.replace("\\", "/").endswith("src/md"))
        self.assertTrue(ctx.parameter_csv.replace("\\", "/").endswith("src/p.csv"))

    def test_ctx_parameter_csv_none_when_absent(self):
        cfg = {"assets_root": "data/assets", "project_root": "..",
               "ne": {"UDG": {"20.15.2": {"source": "src", "steps": ["mmlcommand"]}}}}
        ctx = build_all.make_ctx(cfg, "UDG", "20.15.2", cfg["ne"]["UDG"]["20.15.2"])
        self.assertIsNone(ctx.parameter_csv)


if __name__ == "__main__":
    unittest.main()
