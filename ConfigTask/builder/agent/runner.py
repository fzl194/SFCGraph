# ConfigTask/builder/agent/runner.py
"""Agent 批量调度 + 进度管理 + 失败重试。"""
import json


def load_progress(ctx, step_name):
    progress_dir = ctx["data_dir"] / "progress"
    progress_dir.mkdir(parents=True, exist_ok=True)
    path = progress_dir / f"{step_name}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def save_progress(ctx, step_name, progress):
    progress_dir = ctx["data_dir"] / "progress"
    progress_dir.mkdir(parents=True, exist_ok=True)
    path = progress_dir / f"{step_name}.json"
    path.write_text(json.dumps(progress, ensure_ascii=False, indent=2), encoding="utf-8")


def run_agent_step(ctx, step_name, input_items, agent_fn, verify_fn, key_field="doc_path"):
    """执行一个 Agent step（批量调度 + 核查 + 进度管理）。

    Args:
        ctx: pipeline 上下文
        step_name: step 名称（用于 progress 文件）
        input_items: 全量输入列表
        agent_fn: callable(batch) -> dict(key -> output)
        verify_fn: callable(input_item, output) -> list[str](errors, HARD:/WARN:)
        key_field: 输入项的唯一标识字段

    Returns:
        list: 所有成功产出
    """
    progress = load_progress(ctx, step_name)

    if "rerun_target" in ctx:
        target = ctx["rerun_target"]
        for k in [k for k in progress if target in k]:
            del progress[k]

    all_keys = [item[key_field] for item in input_items]
    todo = [item for item in input_items if progress.get(item[key_field]) != "ok"]

    if not todo:
        ok = sum(1 for v in progress.values() if v == "ok")
        print(f"  {step_name}: 全部已完成 ({ok}/{len(all_keys)})")
        return []

    batch_size = ctx.get("agent_batch_size", 5)
    results = []

    for i in range(0, len(todo), batch_size):
        batch = todo[i:i + batch_size]
        batch_keys = [item[key_field] for item in batch]
        print(f"  {step_name}: 批次 {i//batch_size + 1} ({len(batch)} 项)")

        agent_output = agent_fn(batch)

        for item in batch:
            key = item[key_field]
            output = agent_output.get(key)
            if output is None:
                progress[key] = "fail"
                print(f"    FAIL {key}: Agent 未返回")
                continue

            errors = verify_fn(item, output)
            hard_errors = [e for e in errors if e.startswith("HARD:")]
            if hard_errors:
                progress[key] = "fail"
                print(f"    FAIL {key}: {hard_errors}")
            else:
                progress[key] = "ok"
                results.append(output)
                if errors:
                    print(f"    WARN {key}: {errors}")

        save_progress(ctx, step_name, progress)

    ok_count = sum(1 for v in progress.values() if v == "ok")
    fail_count = sum(1 for v in progress.values() if v == "fail")
    total = len(all_keys)

    if fail_count > 0:
        print(f"  {step_name}: {fail_count} 项失败，下轮重试")
    if ok_count + fail_count < total:
        print(f"  {step_name}: {total - ok_count - fail_count} 项未处理")

    return results
