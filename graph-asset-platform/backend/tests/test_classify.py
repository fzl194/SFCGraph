from app.classify import classify
from app.registry import Registry

R = Registry.load_default()

def test_nf_command():
    rel, fname = classify("UDG@MMLCommand@ADD URR", R, {"version": "20.15.2"})
    assert fname == "UDG@MMLCommand@ADD URR.md"
    assert rel == "Command/UDG/20.15.2"

def test_nf_configobject():
    rel, fname = classify("UDG@ConfigObject@URR", R, {"version": "20.15.2"})
    assert rel == "ConfigObject/UDG/20.15.2"
    assert fname == "UDG@ConfigObject@URR.md"

def test_business_domain():
    rel, fname = classify("BusinessDomain@demo", R, {"domain": "demo-domain"})
    assert rel == "Business/demo-domain"
    assert fname == "BusinessDomain@demo.md"

def test_business_scenario():
    rel, fname = classify("NetworkScenario@demo", R, {"domain": "demo-domain", "scenario": "demo"})
    assert rel == "Business/demo-domain/demo"

def test_business_solution():
    rel, fname = classify("ConfigurationSolution@demo-online", R, {"domain": "demo-domain", "scenario": "demo"})
    assert rel == "Business/demo-domain/demo"
    assert fname == "ConfigurationSolution@demo-online.md"

def test_missing_version_raises():
    import pytest
    with pytest.raises(ValueError):
        classify("UDG@MMLCommand@ADD URR", R, {})  # NF 类缺 version
