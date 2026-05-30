# -*- coding: utf-8 -*-
"""Extract MML commands from feature docs and copy matching command reference MDs."""
import os, re, shutil, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'D:/mywork/KnowledgeBase/SFCGraph'
FEATURE_DIR = f'{BASE}/business-graph/SKILL/feature'
COMMAND_DIR = f'{BASE}/business-graph/SKILL/command'

UDG_CMD_SRC = f'{BASE}/output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令'
UNC_CMD_SRC = f'{BASE}/output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令'

# MML command pattern: VERB KEYWORD (e.g. ADD SRVCHAIN, SET QOSBA, LST APNQOSATTR)
# Verbs: ADD MOD RMV SET LST DSP EXC GEN EXP CLR ACT DEA BLK UBL RST STR STP CRT DLT CHG ENT BND UBD SWP TST IMP
MML_PATTERN = re.compile(
    r'\b(ADD|MOD|RMV|SET|LST|DSP|EXC|GEN|EXP|CLR|ACT|DEA|BLK|UBL|RST|STR|STP|CRT|DLT|CHG|ENT|BND|UBD|SWP|TST|IMP)\s+([A-Z][A-Z0-9_]{1,})\b'
)

# Chinese description inside parentheses in command file names
CMD_NAME_PATTERN = re.compile(r'[（(]([A-Z]{2,}\s+[A-Z0-9_]+)[）)]')


def build_command_map(src_dir):
    """Build map: normalized command name (uppercase) -> full file path."""
    cmd_map = {}
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            if not f.endswith('.md'):
                continue
            # Extract command name from parentheses in filename
            m = CMD_NAME_PATTERN.search(f)
            if m:
                cmd_name = m.group(1).strip().upper()
                cmd_map[cmd_name] = os.path.join(root, f)
    return cmd_map


def extract_mml_from_docs(feature_path):
    """Extract all MML commands from MD files under a feature directory."""
    commands = set()
    for root, dirs, files in os.walk(feature_path):
        for f in files:
            if not f.endswith('.md'):
                continue
            filepath = os.path.join(root, f)
            try:
                with open(filepath, 'r', encoding='utf-8') as fh:
                    content = fh.read()
                    for m in MML_PATTERN.finditer(content):
                        cmd = f'{m.group(1)} {m.group(2)}'.upper()
                        commands.add(cmd)
            except Exception as e:
                print(f'  WARN: cannot read {filepath}: {e}')
    return commands


def main():
    print('Building UDG command reference map...')
    udg_cmd_map = build_command_map(UDG_CMD_SRC)
    print(f'  UDG commands available: {len(udg_cmd_map)}')

    print('Building UNC command reference map...')
    unc_cmd_map = build_command_map(UNC_CMD_SRC)
    print(f'  UNC commands available: {len(unc_cmd_map)}')

    # Collect commands per source
    udg_extracted = set()  # commands found in UDG feature docs
    unc_extracted = set()  # commands found in UNC feature docs

    # Process UDG features
    udg_feature_base = f'{FEATURE_DIR}/UDG'
    if os.path.exists(udg_feature_base):
        for nf in os.listdir(udg_feature_base):
            nf_path = f'{udg_feature_base}/{nf}'
            if not os.path.isdir(nf_path):
                continue
            for feat_id in os.listdir(nf_path):
                feat_path = f'{nf_path}/{feat_id}'
                if not os.path.isdir(feat_path):
                    continue
                cmds = extract_mml_from_docs(feat_path)
                udg_extracted.update(cmds)

    # Process UNC features
    unc_feature_base = f'{FEATURE_DIR}/UNC'
    if os.path.exists(unc_feature_base):
        for nf in os.listdir(unc_feature_base):
            nf_path = f'{unc_feature_base}/{nf}'
            if not os.path.isdir(nf_path):
                continue
            for feat_id in os.listdir(nf_path):
                feat_path = f'{nf_path}/{feat_id}'
                if not os.path.isdir(feat_path):
                    continue
                cmds = extract_mml_from_docs(feat_path)
                unc_extracted.update(cmds)

    print(f'\nExtracted MML commands:')
    print(f'  From UDG features: {len(udg_extracted)}')
    print(f'  From UNC features: {len(unc_extracted)}')

    # Match and copy UDG commands
    print('\n--- Matching UDG commands ---')
    udg_matched = {}  # cmd_name -> src_path
    udg_unmatched = []
    for cmd in sorted(udg_extracted):
        if cmd in udg_cmd_map:
            udg_matched[cmd] = udg_cmd_map[cmd]
        else:
            udg_unmatched.append(cmd)

    print(f'  Matched: {len(udg_matched)}')
    print(f'  Unmatched: {len(udg_unmatched)}')

    # Match and copy UNC commands
    print('\n--- Matching UNC commands ---')
    unc_matched = {}
    unc_unmatched = []
    for cmd in sorted(unc_extracted):
        if cmd in unc_cmd_map:
            unc_matched[cmd] = unc_cmd_map[cmd]
        else:
            unc_unmatched.append(cmd)

    print(f'  Matched: {len(unc_matched)}')
    print(f'  Unmatched: {len(unc_unmatched)}')

    # Copy files
    udg_dest = f'{COMMAND_DIR}/UDG'
    unc_dest = f'{COMMAND_DIR}/UNC'

    copied = 0
    os.makedirs(udg_dest, exist_ok=True)
    for cmd, src in sorted(udg_matched.items()):
        fname = os.path.basename(src)
        shutil.copy2(src, f'{udg_dest}/{fname}')
        copied += 1

    os.makedirs(unc_dest, exist_ok=True)
    for cmd, src in sorted(unc_matched.items()):
        fname = os.path.basename(src)
        shutil.copy2(src, f'{unc_dest}/{fname}')
        copied += 1

    print(f'\nCopied {copied} command MDs to {COMMAND_DIR}')
    print(f'  UDG: {len(udg_matched)} commands')
    print(f'  UNC: {len(unc_matched)} commands')

    # Show unmatched for reference
    if udg_unmatched:
        print(f'\nUDG unmatched ({len(udg_unmatched)}):')
        for c in sorted(udg_unmatched):
            print(f'  {c}')

    if unc_unmatched:
        print(f'\nUNC unmatched ({len(unc_unmatched)}):')
        for c in sorted(unc_unmatched):
            print(f'  {c}')


if __name__ == '__main__':
    main()
