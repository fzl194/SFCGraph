"""extractors registry 单测：注册即被 apply_all 调用 + 返回 immutable 新 dict。"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from builder.extractors import registry  # noqa: E402


class ExtractorsRegistryTests(unittest.TestCase):
    def test_all_ten_derived_fields_registered(self):
        expected = {
            "command_category", "applicable_nf", "max_records", "permission_groups",
            "output_ref_command", "is_dangerous", "effect_mode", "spec_threshold",
            "initial_values", "output_fields",
        }
        self.assertEqual(set(registry.names()), expected)

    def test_apply_all_invokes_every_registered_extractor(self):
        cmd = {
            "verb": "SET",
            "command_function": "适用NF：UDG",
            "notes": ["最大记录数为 100", "属于高危"],
            "permission_text": "需要 G_1 G_2",
            "output_description": "| 输出项名称 | 输出项解释 |\n| --- | --- |\n| A | descA |",
        }
        out = registry.apply_all(cmd)
        # 关键派生字段被填上 → 证明注册即被调用
        self.assertEqual(out["command_category"], "配置类")    # SET → 配置类
        self.assertEqual(out["applicable_nf"], ["UDG"])
        self.assertEqual(out["max_records"], 100)
        self.assertEqual(out["permission_groups"], ["G_1", "G_2"])
        self.assertTrue(out["is_dangerous"])                  # 含"属于高危"
        self.assertEqual(out["output_fields"][0]["field"], "A")

    def test_apply_all_returns_immutable_new_dict(self):
        cmd = {"verb": "LST", "command_function": "", "notes": [], "permission_text": ""}
        original_keys = set(cmd.keys())
        out = registry.apply_all(cmd)
        self.assertIsNot(out, cmd)                            # 新对象
        self.assertEqual(set(cmd.keys()), original_keys)      # 入参键集合不变
        # 入参完全未被修改（没有任何派生字段写回 cmd）
        for name in registry.names():
            self.assertNotIn(name, cmd)
        # 输出却带上了全部派生字段
        for name in registry.names():
            self.assertIn(name, out)

    def test_apply_all_handles_missing_source_fields(self):
        # 极简 cmd：只给 verb，其余字段缺失不应抛
        out = registry.apply_all({"verb": "DSP"})
        self.assertEqual(out["command_category"], "查询类")
        self.assertEqual(out["applicable_nf"], [])
        self.assertEqual(out["max_records"], None)
        self.assertEqual(out["permission_groups"], [])
        self.assertFalse(out["is_dangerous"])
        self.assertEqual(out["effect_mode"], "")


if __name__ == "__main__":
    unittest.main()
