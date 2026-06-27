"""Step 注册表。每个 step 是 callable(ctx) -> int | "PAUSE"。

返回值约定：
- int（产出数）：正常完成，build_all 继续下一步
- "PAUSE"：Agent 步的待处理 prompt 输出尚未回填，build_all 打印交接信息后停

agent 步负责 prep→check→ingest，不直接调 LLM；纯文件交接
（prompts 在 data/{nf}/{version}/agent_prompts/{step}，输出在 .../agent_outputs/{step}）。

各 step 模块的注册由 builder/steps/__init__.py 触发（import 各 step 模块），
本文件只定义装饰器与容器，不 import step，避免循环依赖。
"""
STEPS: dict = {}
PRODUCT_FILE: dict = {}
AGENT_STEPS: set = set()


def step(name: str, output_file: str | None = None, agent: bool = False):
    """装饰器：注册一个 pipeline step。

    Args:
        name: step 名
        output_file: 输出文件名（自动步 skip-if-exists 判定）
        agent: True = Agent 步（build_all 不因输出存在跳过，总执行 prep/check）
    """
    def deco(fn):
        STEPS[name] = fn
        if output_file:
            PRODUCT_FILE[name] = output_file
        AGENT_STEPS.discard(name)  # 重注册时清除旧 agent 状态（如 agent 标志变更）
        if agent:
            AGENT_STEPS.add(name)
        return fn
    return deco
