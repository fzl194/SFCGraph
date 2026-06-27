"""core/legacy.py 测试。"""
from builder.core.legacy import (
    load_legacy_attributes,
    load_legacy_licenses,
    load_legacy_dependencies,
)

ATTRS = ("id,feature_id,feature_type,config_required,applicable_nf,first_release_version\n"
         "UDG:GWFD-020301,GWFD-020301,config_enable,true,SGW-U,20.0.0\n")
LIC = ("id,feature_id,license_number,license_code,license_name,applicable_nf\n"
       "GWFD-020301:license:82209822,GWFD-020301,82209822,LKV3G5BCBC01,内容计费基本功能,\n")
DEP = ("id,source_feature_id,target_feature_id,dependency_type,description\n"
       "GWFD-020301:dep:GWFD-110101,GWFD-020301,GWFD-110101,depends_on,必须先开启SA\n")


def test_load_attributes(tmp_path):
    (tmp_path / "l1_udg_feature_attributes.csv").write_text(ATTRS, encoding="utf-8")
    a = load_legacy_attributes(tmp_path, "UDG")
    assert a["GWFD-020301"]["feature_type"] == "config_enable"
    assert a["GWFD-020301"]["first_release_version"] == "20.0.0"


def test_load_licenses_and_deps(tmp_path):
    (tmp_path / "l1_udg_feature_license.csv").write_text(LIC, encoding="utf-8")
    (tmp_path / "l1_udg_feature_dependency.csv").write_text(DEP, encoding="utf-8")
    lic = load_legacy_licenses(tmp_path, "UDG")
    assert lic[0]["license_code"] == "LKV3G5BCBC01"
    deps = load_legacy_dependencies(tmp_path, "UDG")
    assert deps[0]["target_feature_code"] == "GWFD-110101"


def test_missing_returns_empty(tmp_path):
    assert load_legacy_attributes(tmp_path, "UDG") == {}
    assert load_legacy_licenses(tmp_path, "UDG") == []
    assert load_legacy_dependencies(tmp_path, "UNC") == []
