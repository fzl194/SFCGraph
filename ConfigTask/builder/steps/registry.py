# ConfigTask/builder/steps/registry.py
"""Step 注册表。每个 step 是 callable(ctx) -> int|str。

返回值约定：
- int（产出数）：正常完成，build_all 继续下一步
- "PAUSE"：Agent 步的待处理 prompt 输出尚未回填，build_all 打印交接信息后停止

agent 步（split_tasks/merge_fields/extract_rules）负责 prep→check→ingest，
不直接调 LLM；纯文件交接（prompts 在 data/agent_prompts，输出在 data/agent_outputs）。
"""
STEPS = {}
PRODUCT_FILE = {}
AGENT_STEPS = set()


def step(name, output_file=None, agent=False):
    """装饰器：注册一个 pipeline step。

    Args:
        name: step 名
        output_file: 输出文件名（用于自动步 skip-if-exists）
        agent: True = Agent 步（build_all 不因输出存在而跳过，总执行 prep/check）
    """
    def deco(fn):
        STEPS[name] = fn
        if output_file:
            PRODUCT_FILE[name] = output_file
        if agent:
            AGENT_STEPS.add(name)
        return fn
    return deco
