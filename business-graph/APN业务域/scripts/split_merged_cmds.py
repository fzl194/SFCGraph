#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
拆分04-command-graph.md里command_name用/合并多命令的CMD。
每个合并CMD拆成独立MMLCommand(每条命令一个CMD),编号用-1/-2后缀。
修复用户反馈:task下面命令要单条,一个MMLCommand=一条命令。
"""
import re
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

PATH = r"D:\mywork\KnowledgeBase\SFCGraph\业务图谱体系\APN业务域\three-layer-graph\04-command-graph.md"

with open(PATH, encoding="utf-8") as f:
    lines = f.read().split("\n")

# 匹配 MMLCommand 数据行: | `CMD-xxx` | `name1` / `name2` ... | verb | obj | summary | params | ev |
# command_name列含 / 分隔多个`命令名`即为合并CMD
pat = re.compile(
    r"^\| `(?P<cid>CMD-[A-Z]+-\d+)` \| (?P<names>`[^`]+`(?: */ *`[^`]+`)+)"
    r" \| (?P<rest>.+) \|\s*$"
)

new_lines = []
split_count = 0
new_cmd_count = 0
for line in lines:
    m = pat.match(line)
    if not m:
        new_lines.append(line)
        continue
    cid = m.group("cid")
    names = re.findall(r"`([^`]+)`", m.group("names"))
    rest = m.group("rest")
    rest_parts = [p.strip() for p in rest.split("|")]
    # rest_parts: [verb, object_keyword, summary, params, source_evidence_ids]
    summary = rest_parts[2] if len(rest_parts) > 2 else ""
    params = rest_parts[3] if len(rest_parts) > 3 else ""
    ev = rest_parts[4] if len(rest_parts) > 4 else ""
    split_count += 1
    for i, name in enumerate(names, 1):
        new_cid = f"{cid}-{i}"
        parts = name.split(" ", 1)
        verb = parts[0]
        obj = parts[1] if len(parts) > 1 else (rest_parts[1] if len(rest_parts) > 1 else "")
        new_lines.append(
            f"| `{new_cid}` | `{name}` | {verb} | {obj} | {summary} | {params} | {ev} |"
        )
        new_cmd_count += 1

with open(PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(new_lines))

print(f"拆分合并CMD: {split_count} 处")
print(f"生成独立CMD: {new_cmd_count} 个")
