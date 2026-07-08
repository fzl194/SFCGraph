#!/usr/bin/env python3
"""
通用 Lint：扫 assets/ 所有 md，把已建对象的 [[四段式ID]] 占位换成 markdown 链接。
CLAUDE.md §4.3 Lint（缺页/占位回填）+ §5.5（已建 [..](.md) / 未建 [[ID]]）。

可回填对象（有独立 md）：MMLCommand/ConfigObject/Feature/License/Task
内嵌对象（无独立 md，保留占位）：DecisionPoint/TaskRule/TaskRelation/CommandParameter/其他

用法:
  python assets/scripts/lint_and_backfill.py            # 回填
  python assets/scripts/lint_and_backfill.py --dry      # 只报告
"""
import argparse
import glob
import os
import re
from collections import Counter

ASSETS = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

DIR = {
    'MMLCommand': 'command',
    'ConfigObject': 'configobject',
    'Feature': 'feature',
    'License': 'license',
    'Task': 'task',
}


def sanitize(s: str) -> str:
    return re.sub(r'[\s/\\:*?"<>|]+', '-', str(s)).strip('-')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry', action='store_true')
    args = ap.parse_args()

    mds = glob.glob(os.path.join(ASSETS, '**', '*.md'), recursive=True)
    pat = re.compile(r'\[\[([^\[\]]+)\]\]')
    updated_files = 0
    total_replaced = 0
    leftover = Counter()

    for md in mds:
        with open(md, encoding='utf-8') as f:
            txt = f.read()
        orig = txt

        def repl(m):
            nonlocal total_replaced
            oid = m.group(1)
            parts = oid.split('@')
            if len(parts) < 4:
                leftover[parts[2] if len(parts) > 2 else '?'] += 1
                return m.group(0)
            nf, ver, otype = parts[0], parts[1], parts[2]
            local = '@'.join(parts[3:])
            if otype not in DIR:
                leftover[otype] += 1
                return m.group(0)
            path = f"{DIR[otype]}/{nf}/{ver}/{sanitize(local)}.md"
            if os.path.exists(os.path.join(ASSETS, path)):
                total_replaced += 1
                return f"[{local}]({path})"
            leftover[otype] += 1
            return m.group(0)

        txt = pat.sub(repl, txt)
        if txt != orig:
            updated_files += 1
            if not args.dry:
                with open(md, 'w', encoding='utf-8') as f:
                    f.write(txt)

    print(f"扫描 md 文件: {len(mds)}")
    print(f"回填占位: {total_replaced} 处，涉及 {updated_files} 个文件")
    print(f"剩余占位（内嵌/未建）: {dict(leftover)}")


if __name__ == '__main__':
    main()
