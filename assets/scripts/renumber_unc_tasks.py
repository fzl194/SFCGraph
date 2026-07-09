#!/usr/bin/env python3
"""
UNC task wiki 编号化：把命令名文件名（ADD-APN.md）改成编号（0-00001.md），对齐 UDG 风格。
编号方案：27 个 atom 沿用 ConfigTask yaml 的编号（0-00001~0-00027），
         其余 182 命令按命令名排序接续 0-00028~0-00209。
同步：front matter id + 所有 assets md 里的 UNC task 引用（链接 path / [[占位]]）。
幂等：重跑安全（已编号文件跳过）。

用法: python assets/scripts/renumber_unc_tasks.py
"""
import glob
import json
import os
import re

import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TASK_DIR = os.path.join(REPO, 'assets', 'task', 'UNC', '20.15.2')
EV_DIR = os.path.join(REPO, 'ConfigTask', 'assert', 'UNC', '20.15.2')


def build_mapping():
    """209 命令 → 编号。27 atom 用 yaml 编号，其余按命令名排序接续。"""
    atom_map = {}
    for p in glob.glob(os.path.join(EV_DIR, 'tasks', 'task-0-*.yaml')):
        r = yaml.safe_load(open(p, encoding='utf-8')) or {}
        tid = r.get('task_id', '')
        num = tid.split('@')[-1]
        ref = r.get('ref', '') or ''
        cmd = ref.split('@MMLCommand@')[-1] if '@MMLCommand@' in ref else ''
        if cmd and num.startswith('0-'):
            atom_map[cmd] = num
    all_cmds = sorted(set(
        os.path.basename(p)[:-3].replace('_', ' ')
        for p in glob.glob(os.path.join(EV_DIR, 'command-evidence', '*.md'))))
    non_atom = [c for c in all_cmds if c not in atom_map]
    mapping = dict(atom_map)
    for i, c in enumerate(non_atom):
        mapping[c] = f'0-{28 + i:05d}'
    return mapping


def main():
    mapping = build_mapping()
    json.dump(mapping, open(os.path.join(TASK_DIR, '_numbering.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1, sort_keys=True)
    print(f'映射: {len(mapping)} 命令')

    # 1. 重命名已建命令名文件 → 编号文件，改 front matter id
    renamed = 0
    for f in glob.glob(os.path.join(TASK_DIR, '*.md')):
        b = os.path.basename(f)
        if b.startswith(('_', 'index')):
            continue
        old = b[:-3]
        if re.match(r'^0-\d{5}$', old):
            continue  # 已是编号
        cmd = old.replace('-', ' ')
        if cmd not in mapping:
            print(f'  跳过(非命令名/不在映射): {b}')
            continue
        num = mapping[cmd]
        newp = os.path.join(TASK_DIR, num + '.md')
        if os.path.exists(newp):
            os.remove(f)
            continue
        txt = open(f, encoding='utf-8').read()
        txt = txt.replace(f'UNC@20.15.2@Task@{cmd}', f'UNC@20.15.2@Task@{num}')
        open(newp, 'w', encoding='utf-8').write(txt)
        os.remove(f)
        renamed += 1
    print(f'重命名 {renamed} 个 task md')

    # 2. 改所有 assets md 的 UNC task 引用（命令名长度降序，避免前缀误伤）
    def fix(txt):
        for cmd in sorted(mapping, key=len, reverse=True):
            num = mapping[cmd]
            cmdfile = cmd.replace(' ', '-')
            txt = txt.replace(f'UNC@20.15.2@Task@{cmd}', f'UNC@20.15.2@Task@{num}')
            txt = txt.replace(f'task/UNC/20.15.2/{cmdfile}.md', f'task/UNC/20.15.2/{num}.md')
        return txt

    updated = 0
    for md in glob.glob(os.path.join(REPO, 'assets', '**', '*.md'), recursive=True):
        txt = open(md, encoding='utf-8').read()
        new = fix(txt)
        if new != txt:
            open(md, 'w', encoding='utf-8').write(new)
            updated += 1
    print(f'改引用 {updated} 个 md')


if __name__ == '__main__':
    main()
