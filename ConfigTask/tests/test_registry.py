# ConfigTask/tests/test_registry.py
import pytest
from builder.steps.registry import step, validate_order, STEPS, PROVIDES, REQUIRES


def test_step_registers_provides_requires():
    @step("__t1_reg", provides=("p1",), requires=("r1",))
    def fn(ctx):
        return 1
    assert STEPS["__t1_reg"] is fn
    assert PROVIDES["__t1_reg"] == ("p1",)
    assert REQUIRES["__t1_reg"] == ("r1",)


def test_validate_order_ok_when_requirement_provided_earlier():
    @step("__t2_a", provides=("docX",))
    def a(ctx):
        pass
    @step("__t2_b", requires=("docX",))
    def b(ctx):
        pass
    # a 在 b 前，提供 docX → 合法
    validate_order(["__t2_a", "__t2_b"])


def test_validate_order_fails_when_requirement_missing():
    @step("__t3_b", requires=("docY",))
    def b(ctx):
        pass
    # 没人在 b 前提供 docY → 应抛错
    with pytest.raises(AssertionError):
        validate_order(["__t3_b"])
