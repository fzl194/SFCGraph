"""paramref builder 单元测试。

覆盖：_parse_param_ref（参数引用串 → 实例键）、build_param_references
（references 边 + 推导对象 refers_to 边 + 边属性）。
"""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from builder.core import param_reference as core  # noqa: E402


class ParseParamRefTests(unittest.TestCase):
    def test_parse_basic(self):
        r = core._parse_param_ref("UDG:ADD_FLTBINDFLOWF.FILTERNAME", "20.15.2")
        self.assertIsNotNone(r)
        self.assertEqual(r["nf"], "UDG")
        self.assertEqual(r["command_name"], "ADD FLTBINDFLOWF")
        self.assertEqual(r["object_name"], "FLTBINDFLOWF")
        self.assertEqual(r["param_name"], "FILTERNAME")
        self.assertEqual(r["parameter_id"],
                         "UDG@20.15.2@CommandParameter@ADD FLTBINDFLOWF:FILTERNAME")

    def test_parse_invalid(self):
        self.assertIsNone(core._parse_param_ref("", "20.15.2"))
        self.assertIsNone(core._parse_param_ref("UDG:ADD_FILTER", "20.15.2"))  # 无参数
        self.assertIsNone(core._parse_param_ref("NO_COLON", "20.15.2"))         # 无冒号


class BuildParamReferencesTests(unittest.TestCase):
    def test_build_references_and_refers_to(self):
        csv_text = (
            "ID,网元,版本,节点,节点名称,节点命令,配置(后配),"
            "配置依赖参数(前后节点顺序以J列为准),是否匹配（操作命令的条件放到该列）,"
            "索引检查(依赖命令的条件放到该列),0：弱绑定，1：强绑定,是否联动删除\n"
            "1,UDG,20.15.2,FLTBINDFLOWF,FILTERNAME,ADD FLTBINDFLOWF,"
            "UDG:ADD_FLTBINDFLOWF.FILTERNAME,UDG:ADD_FILTER.FILTERNAME,"
            "ADD_FLTBINDFLOWF.FILTERNAME != null,.equalsIgnoreCase,1,0\n"
            "2,UDG,20.15.2,URRGROUP,UPURRNAME1,ADD URRGROUP,"
            "UDG:ADD_URRGROUP.UPURRNAME1,UDG:ADD_URR.URRNAME,"
            "ADD_URRGROUP.UPURRNAME1 != null,.equalsIgnoreCase,1,0\n"
        )
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as f:
            f.write(csv_text)
            path = f.name
        try:
            result = core.build_param_references(path, "20.15.2")
            # 2 条 references 边
            self.assertEqual(len(result["parameter_references"]), 2)
            r0 = result["parameter_references"][0]
            self.assertEqual(r0["edge_type"], "references")
            self.assertEqual(r0["from_parameter_ref"],
                             "UDG@20.15.2@CommandParameter@ADD FLTBINDFLOWF:FILTERNAME")
            self.assertEqual(r0["to_parameter_ref"],
                             "UDG@20.15.2@CommandParameter@ADD FILTER:FILTERNAME")
            self.assertEqual(r0["binding_strength"], "强绑定")
            self.assertFalse(r0["cascade_delete"])
            # 2 条对象间 refers_to（FLTBINDFLOWF→FILTER, URRGROUP→URR）
            self.assertEqual(len(result["object_refers_to"]), 2)
            pair = {(e["from_object_ref"], e["to_object_ref"]) for e in result["object_refers_to"]}
            self.assertIn(("UDG@20.15.2@ConfigObject@FLTBINDFLOWF", "UDG@20.15.2@ConfigObject@FILTER"), pair)
            self.assertIn(("UDG@20.15.2@ConfigObject@URRGROUP", "UDG@20.15.2@ConfigObject@URR"), pair)
        finally:
            Path(path).unlink()


if __name__ == "__main__":
    unittest.main()
