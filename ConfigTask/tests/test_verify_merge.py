# ConfigTask/tests/test_verify_merge.py
"""verify_merge 校验测试。"""
from builder.steps.verify_merge import verify_task


def _task(**over):
    t = {
        "task_logical_name": "配置URR", "task_goal": "g", "task_summary": "s",
        "commands": [{"command_ref": "ADD URR", "parameters": [
            {"parameter_ref": "URRID", "binding_type": "variable", "variable_source": "global_planned"},
            {"parameter_ref": "UPURRNAME1", "binding_type": "reference"},
        ]}],
        "_decision_points": ["x"], "_split_notes": "y",
    }
    t.update(over)
    return t


def test_valid_task_passes():
    errs = verify_task(_task())
    assert not [e for e in errs if e.startswith("HARD:")]
    assert not [e for e in errs if e.startswith("WARN:")]


def test_empty_required_field_hard():
    errs = verify_task(_task(task_goal=""))
    assert any("task_goal" in e and e.startswith("HARD:") for e in errs)


def test_bad_binding_type_hard():
    t = _task()
    t["commands"][0]["parameters"][0]["binding_type"] = "weird"
    errs = verify_task(t)
    assert any("binding_type" in e for e in errs)


def test_variable_without_source_hard():
    t = _task()
    t["commands"][0]["parameters"][0]["variable_source"] = None
    errs = verify_task(t)
    assert any("variable_source" in e for e in errs)


def test_fixed_without_value_hard():
    t = _task()
    p = t["commands"][0]["parameters"]
    p.append({"parameter_ref": "MODE", "binding_type": "fixed"})  # 无 fixed_value
    errs = verify_task(t)
    assert any("fixed_value" in e for e in errs)


def test_reference_needs_no_source():
    # reference 参数不需要 variable_source，不应报错
    errs = verify_task(_task())
    assert not any("UPURRNAME1" in e for e in errs)


def test_missing_decision_points_warn():
    t = _task()
    del t["_decision_points"]
    del t["_split_notes"]
    errs = verify_task(t)
    assert any(e.startswith("WARN:") for e in errs)
    assert not [e for e in errs if e.startswith("HARD:")]
