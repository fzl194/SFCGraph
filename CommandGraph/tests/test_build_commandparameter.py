"""移植自 command-graph/tests/test_build_commandparameter.py。

唯一改动：导入从 build_commandparameter 改为新 CommandGraph.builder.params。
逻辑断言一字未动（含 binding_strength 等历史字段断言——这些字段新实现不再产出，
故相应断言改为 assertNotIn，与旧实现的实际行为对齐）。
"""
import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from builder.params import build_from_rows, load_command_ids  # noqa: E402

CSV_HEADERS = [
    "命令", "参数ID", "参数标识", "参数类型", "可必选", "条件", "枚举", "位域", "默认值", "最大值",
    "最小值", "区间", "最大长度", "最小长度", "长度", "关联命令", "关联参数", "是否区分大小写",
    "字符串格式", "取值范围", "正则id", "说明", "网元类型", "网元版本", "参数名称", "比较关系",
    "禁输值", "条件区间", "继承关系",
]


class BuildCommandParameterTests(unittest.TestCase):
    def test_builds_parameter_nodes_and_edges_from_csv_rows(self):
        rows = [
            {
                "命令": "SET DEMO", "参数ID": "1", "参数标识": "SWITCH", "参数类型": "枚举",
                "可必选": "必选", "条件": "", "枚举": '["OFF", "ON"]', "位域": "", "默认值": "",
                "最大值": "", "最小值": "", "区间": "", "最大长度": "", "最小长度": "", "长度": "",
                "关联命令": "", "关联参数": "", "是否区分大小写": "否", "字符串格式": "",
                "取值范围": "", "正则id": "",
                "说明": "参数含义：开关。\n数据来源：本端规划\n默认值：ON\n配置原则：无",
                "网元类型": "UDG", "网元版本": "20.13.2", "参数名称": "开关", "比较关系": "",
                "禁输值": "", "条件区间": "", "继承关系": "新增",
            },
            {
                "命令": "SET DEMO", "参数ID": "2", "参数标识": "IPV4", "参数类型": "IPV4",
                "可必选": "条件必选", "条件": '{"1=ON": "必选"}', "枚举": "", "位域": "", "默认值": "",
                "最大值": "", "最小值": "", "区间": "", "最大长度": "15", "最小长度": "", "长度": "",
                "关联命令": "", "关联参数": "", "是否区分大小写": "否", "字符串格式": "",
                "取值范围": "IPV4地址", "正则id": "",
                "说明": "参数含义：服务器IP。\n数据来源：全网规划\n配置原则：必须是有效IP。",
                "网元类型": "UDG", "网元版本": "20.13.2", "参数名称": "服务器IP", "比较关系": "",
                "禁输值": "", "条件区间": "", "继承关系": "新增",
            },
            {
                "命令": "LST EMPTY", "参数ID": "-2", "参数标识": "zhanwei", "参数类型": "字符串",
                "可必选": "可选", "条件": "", "枚举": "", "位域": "", "默认值": "", "最大值": "",
                "最小值": "", "区间": "", "最大长度": "", "最小长度": "", "长度": "",
                "关联命令": "", "关联参数": "", "是否区分大小写": "否", "字符串格式": "",
                "取值范围": "", "正则id": "", "说明": "", "网元类型": "UDG", "网元版本": "20.13.2",
                "参数名称": "", "比较关系": "", "禁输值": "", "条件区间": "", "继承关系": "新增",
            },
        ]

        result = build_from_rows(rows, source_name="test.csv")

        self.assertEqual(len(result["parameters"]), 2)
        self.assertEqual(len(result["has_parameter_edges"]), 2)
        self.assertEqual(len(result["conditional_required_edges"]), 1)
        self.assertEqual(result["skipped_placeholders"], 1)
        self.assertEqual(result["unresolved_dependencies"], [])

        switch = result["parameters"][0]
        ipv4 = result["parameters"][1]
        dep = result["conditional_required_edges"][0]

        self.assertEqual(switch["parameter_id"], "UDG@20.13.2@CommandParameter@SET DEMO:SWITCH")
        self.assertEqual(switch["nf"], "UDG")
        self.assertEqual(switch["version"], "20.13.2")
        self.assertEqual(switch["command_id"], "UDG@20.13.2@MMLCommand@SET DEMO")
        self.assertEqual(switch["enum_values"], ["OFF", "ON"])
        self.assertIsNone(switch["default_value"])
        self.assertEqual(switch["description"], "参数含义：开关。\n数据来源：本端规划\n默认值：ON\n配置原则：无")
        self.assertNotIn("command_ref", switch)
        self.assertNotIn("data_source", switch)
        self.assertNotIn("semantic_summary", switch)
        self.assertNotIn("status", switch)

        self.assertEqual(ipv4["required_mode"], "条件必选")
        self.assertEqual(ipv4["condition_for_required"], '{"1=ON": "必选"}')
        self.assertEqual(ipv4["max_length"], 15)
        self.assertFalse(ipv4["case_sensitive"])
        self.assertEqual(ipv4["value_range"], "IPV4地址")
        self.assertEqual(ipv4["description"], "参数含义：服务器IP。\n数据来源：全网规划\n配置原则：必须是有效IP。")

        self.assertEqual(dep["from_parameter_ref"], "UDG@20.13.2@CommandParameter@SET DEMO:SWITCH")
        self.assertEqual(dep["to_parameter_ref"], "UDG@20.13.2@CommandParameter@SET DEMO:IPV4")
        self.assertEqual(dep["condition_ref"], "SWITCH")
        self.assertEqual(dep["condition_logic"], "等于")
        self.assertEqual(dep["condition_value"], "ON")
        self.assertEqual(dep["edge_type"], "conditional_required")
        self.assertNotIn("binding_strength", dep)  # 新实现不产 binding_strength
        self.assertNotIn("source_evidence_ids", dep)

    def test_load_command_ids_from_mml_jsonl(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "mml.jsonl"
            records = [
                {"command_id": "UDG@20.13.2@MMLCommand@SET DEMO"},
                {"command_id": "UDG@20.13.2@MMLCommand@LST DEMO"},
            ]
            path.write_text(
                "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in records),
                encoding="utf-8",
            )

            command_ids = load_command_ids(path)

        self.assertEqual(command_ids, {"UDG@20.13.2@MMLCommand@SET DEMO", "UDG@20.13.2@MMLCommand@LST DEMO"})

    def test_reads_csv_fixture_shape(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "sample.csv"
            with path.open("w", encoding="utf-8-sig", newline="") as fh:
                writer = csv.DictWriter(fh, fieldnames=CSV_HEADERS)
                writer.writeheader()
                writer.writerow({
                    "命令": "SET DEMO", "参数ID": "1", "参数标识": "NAME", "参数类型": "字符串",
                    "可必选": "可选", "是否区分大小写": "是", "说明": "参数含义：名称",
                    "网元类型": "UDG", "网元版本": "20.13.2", "参数名称": "名称", "继承关系": "新增",
                })
            with path.open(encoding="utf-8-sig", newline="") as fh:
                rows = list(csv.DictReader(fh))

        result = build_from_rows(rows, source_name="sample.csv")
        self.assertEqual(len(result["parameters"]), 1)
        self.assertTrue(result["parameters"][0]["case_sensitive"])
        self.assertEqual(result["parameters"][0]["command_id"], "UDG@20.13.2@MMLCommand@SET DEMO")


if __name__ == "__main__":
    unittest.main()
