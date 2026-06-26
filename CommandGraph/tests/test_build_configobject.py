"""ConfigObject builder 单元测试。

覆盖：object_kind 5 类判定（含 binding 边界）、object_name_zh 去动词、
build_config_objects 聚合（11 字段）、命令→对象边 verb→relation_type。
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from builder.core import config_object as core  # noqa: E402


class ClassifyKindTests(unittest.TestCase):
    def test_entity_crud(self):
        self.assertEqual(core.classify_kind("URR", ["ADD", "MOD", "RMV", "LST"]), "entity")

    def test_global_setting_set_only(self):
        self.assertEqual(core.classify_kind("REFRESHSRV", ["SET"]), "global_setting")
        self.assertEqual(core.classify_kind("GLBPARA", ["SET", "LST"]), "global_setting")

    def test_query_target_lst_only(self):
        self.assertEqual(core.classify_kind("NATSESSION", ["DSP"]), "query_target")
        self.assertEqual(core.classify_kind("STAT", ["LST", "DSP"]), "query_target")

    def test_action_non_config_non_query(self):
        self.assertEqual(core.classify_kind("BGPALL", ["SYN"]), "action")
        self.assertEqual(core.classify_kind("ARP", ["RTR"]), "action")

    def test_binding_name_and_crud(self):
        self.assertEqual(core.classify_kind("RULEBINDING", ["ADD", "RMV", "LST"]), "binding")

    def test_binding_set_only_falls_to_global_setting(self):
        # 命名含 BIND 但只 SET → 按行为归 global_setting（binding 双条件不满足）
        self.assertEqual(core.classify_kind("URRGRPBINDING", ["SET"]), "global_setting")


class StripVerbPrefixTests(unittest.TestCase):
    def test_strips_known_verbs(self):
        self.assertEqual(core.strip_verb_prefix("增加URR"), "URR")
        self.assertEqual(core.strip_verb_prefix("查询NAT用户会话信息"), "NAT用户会话信息")
        self.assertEqual(core.strip_verb_prefix("设置自动日志策略"), "自动日志策略")

    def test_no_verb_returns_as_is(self):
        self.assertEqual(core.strip_verb_prefix("业务刷新"), "业务刷新")
        self.assertEqual(core.strip_verb_prefix(""), "")


class BuildConfigObjectsTests(unittest.TestCase):
    def setUp(self):
        nf, ver = "UDG", "20.15.2"
        self.nf, self.ver = nf, ver
        cid = lambda c: f"{nf}@{ver}@MMLCommand@{c}"  # noqa: E731
        self.mml_commands = [
            {"command_id": cid("ADD URR"), "command_name": "ADD URR", "verb": "ADD",
             "object_keyword": "URR", "command_name_zh": "增加使用量上报规则",
             "command_function": "该命令用于增加URR实例。", "applicable_nf": ["UPF"],
             "output_fields": [], "source_evidence_ids": ["a.md"]},
            {"command_id": cid("MOD URR"), "command_name": "MOD URR", "verb": "MOD",
             "object_keyword": "URR", "command_name_zh": "修改使用量上报规则",
             "command_function": "", "applicable_nf": ["UPF", "PGW-U"],
             "output_fields": [], "source_evidence_ids": ["b.md"]},
            {"command_id": cid("LST URR"), "command_name": "LST URR", "verb": "LST",
             "object_keyword": "URR", "command_name_zh": "查询使用量上报规则",
             "command_function": "", "applicable_nf": [],
             "output_fields": [{"field": "URRNAME"}, {"field": "URRID"}, {"field": "USAGERPTMODE"}],
             "source_evidence_ids": ["c.md"]},
            {"command_id": cid("SET REFRESHSRV"), "command_name": "SET REFRESHSRV", "verb": "SET",
             "object_keyword": "REFRESHSRV", "command_name_zh": "业务刷新",
             "command_function": "该命令用于刷新生效。", "applicable_nf": [],
             "output_fields": [], "source_evidence_ids": ["r.md"]},
        ]
        self.command_parameters = [
            {"parameter_id": f"{nf}@{ver}@CommandParameter@ADD URR:URRNAME",
             "command_id": cid("ADD URR"), "parameter_name": "URRNAME"},
            {"parameter_id": f"{nf}@{ver}@CommandParameter@ADD URR:URRID",
             "command_id": cid("ADD URR"), "parameter_name": "URRID"},
        ]
        self.mod_rules = {"URR": ["URRNAME"]}
        self.rmv_rules = {}
        self.uniq_rules = {"URR": [["URRNAME"]]}

    def _build(self):
        return core.build_config_objects(self.nf, self.ver, self.mml_commands,
                                         self.command_parameters, self.mod_rules,
                                         self.rmv_rules, self.uniq_rules)

    def test_object_count_and_ids(self):
        r = self._build()
        self.assertEqual(len(r["objects"]), 2)
        self.assertEqual({o["object_id"] for o in r["objects"]}, {
            "UDG@20.15.2@ConfigObject@URR",
            "UDG@20.15.2@ConfigObject@REFRESHSRV",
        })

    def test_urr_object_fields(self):
        urr = next(o for o in self._build()["objects"] if o["object_name"] == "URR")
        self.assertEqual(urr["object_kind"], "entity")
        self.assertEqual(urr["object_name_zh"], "使用量上报规则")  # 去动词"增加"
        self.assertEqual(urr["identifier_parameters"], ["URRNAME"])
        self.assertEqual(urr["uniqueness_keys"], [["URRNAME"]])
        # ADD 参数(URRNAME/URRID)，不含 LST output_fields（USAGERPTMODE 不再并入）
        self.assertEqual(urr["attribute_names"], ["URRNAME", "URRID"])
        self.assertEqual(urr["description"], "该命令用于增加URR实例。")  # ADD 优先
        self.assertEqual(urr["applicable_nf"], ["UPF", "PGW-U"])  # 并集保序
        self.assertEqual(urr["status"], "active")
        self.assertEqual(urr["source_evidence_ids"], ["a.md", "b.md", "c.md"])

    def test_refreshsrv_global_setting(self):
        ref = next(o for o in self._build()["objects"] if o["object_name"] == "REFRESHSRV")
        self.assertEqual(ref["object_kind"], "global_setting")
        self.assertEqual(ref["identifier_parameters"], [])
        self.assertEqual(ref["uniqueness_keys"], [])

    def test_edges_verb_to_relation(self):
        edges = self._build()["edges"]
        self.assertEqual(len(edges), 4)
        rel = {e["from_command_ref"].split("@")[-1]: e["edge_type"] for e in edges}
        self.assertEqual(rel["ADD URR"], "creates")
        self.assertEqual(rel["MOD URR"], "modifies")
        self.assertEqual(rel["LST URR"], "queries")
        self.assertEqual(rel["SET REFRESHSRV"], "sets")
        # 边端点指向对象
        urr_edges = [e for e in edges if e["to_object_ref"].endswith("@URR")]
        self.assertEqual(len(urr_edges), 3)


if __name__ == "__main__":
    unittest.main()
