# ConfigTask/tests/test_object_family.py
"""对象族核查：一个 candidate 内最大族占比 ≥ 50%。"""
from builder.verify.object_family import classify_family, verify_family_coherence


def test_classify():
    assert classify_family("ADD URR") == "URR"
    assert classify_family("ADD URRGROUP") == "URR"
    assert classify_family("ADD PCCPOLICYGRP") == "URR"
    assert classify_family("ADD FILTER") == "FILTER"
    assert classify_family("ADD L7FILTER") == "FILTER"
    assert classify_family("ADD FLOWFILTER") == "FILTER"
    assert classify_family("ADD RULE") == "RULE"
    assert classify_family("ADD USERPROFILE") == "PROFILE"
    assert classify_family("SET LICENSESWITCH") == "LICENSE"
    assert classify_family("SET REFRESHSRV") == "REFRESH"
    assert classify_family("ADD OSPFV3") == "OSPF"


def test_coherent_family():
    assert verify_family_coherence(["ADD FILTER", "ADD L7FILTER", "ADD FLOWFILTER"]) == []


def test_mixed_family():
    warnings = verify_family_coherence(["ADD URR", "ADD URRGROUP", "ADD FILTER", "ADD L7FILTER"])
    assert len(warnings) > 0


def test_license_merged_ok():
    assert verify_family_coherence(["SET LICENSESWITCH", "ADD APN", "SET APNQOSATTR"]) == []
