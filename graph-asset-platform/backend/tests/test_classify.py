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
    rel, fname = classify("BusinessDomain@charging", R, {"domain": "business-awareness"})
    assert rel == "Business/business-awareness"
    assert fname == "BusinessDomain@charging.md"

def test_business_scenario():
    rel, fname = classify("NetworkScenario@charging", R, {"domain": "business-awareness", "scenario": "charging"})
    assert rel == "Business/business-awareness/charging"

def test_business_solution():
    rel, fname = classify("ConfigurationSolution@charging-online", R, {"domain": "business-awareness", "scenario": "charging"})
    assert rel == "Business/business-awareness/charging"
    assert fname == "ConfigurationSolution@charging-online.md"

def test_missing_version_raises():
    import pytest
    with pytest.raises(ValueError):
        classify("UDG@MMLCommand@ADD URR", R, {})  # NF 类缺 version
