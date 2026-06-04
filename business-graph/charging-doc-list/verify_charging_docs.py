"""
校验计费文档清单完整性：
1. 扫描指定目录下所有md文件
2. 对比已收录清单
3. 对未收录文件做内容关键词检查，判断是否被遗漏
"""

import os
import re
from pathlib import Path

# === 配置 ===
UNC_BASE = Path(r"D:\mywork\KnowledgeBase\SFCGraph\output\UNC 20.15.2 产品文档(裸机容器) 05")
UDG_BASE = Path(r"D:\mywork\KnowledgeBase\SFCGraph\output\UDG_Product_Documentation_CH_20.15.2")
BATCH_DIR = Path(r"D:\mywork\KnowledgeBase\SFCGraph\business-graph\charging-doc-list")

# 计费关键词（用于内容扫描）
CHARGING_KEYWORDS = [
    '计费', 'URR', 'Usage Report', 'Quota', '配额', '话单',
    'CCR', 'CCA', 'Gy接口', 'Ga接口', 'N40', 'Nchf',
    'CHF', 'OCS', 'CG', 'billing', 'charging',
    'RG', 'Rating Group', 'SCUR', 'MSCUR',
    'USAGERPTMODE', 'OFFMETERINGTYPE', 'ONLMETERINGTYPE',
    'METERINGTYPE', 'OFFLINE', 'ONLINE',
    '流量计费', '时长计费', '事件计费', '内容计费',
    '费率', '资费', '用量', 'USAGE',
    '融合计费', '在线计费', '离线计费',
    'Charging-Rule', 'Charging Data',
    'Granted-Service-Unit', 'Used-Service-Unit',
    'Rating-Group', 'Reporting-Level',
    'PCCPOLICYGRP', 'URRGROUP',
]

# 需要校验的目录（只校验做了筛选的目录，不校验全量收录的）
DIRS_TO_CHECK = [
    # (描述, UNC下的相对路径, 是否一望5G层需检查特定子目录)
    ("PCC之SM策略", "网络部署/业务专题/5G PCC之SM策略解决方案", False),
    ("ULCL分流", "网络部署/业务专题/5G Core ULCL分流解决方案", False),
    ("FUP", "网络部署/业务专题/5G Core FUP解决方案", False),
    ("Gx接口", "快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/Gx", False),
    ("PFCP_N4", "快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口", False),
    ("PFCP_Sx", "快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/Sx", False),
    ("初始配置-计费", "网络部署/初始配置", False),
    ("网络运维-计费", "网络运维", False),
]


def load_included_files():
    """从batch文件中提取已收录的文件名（不含路径）"""
    included = {}  # key: dir_desc, value: set of filenames

    # Batch 01: SA+计费+PCC静态规则 (UNC一望5G, 已去重保留UNC)
    included['一望5G-SA计费PCC'] = set()

    # 手动构建已收录文件集合
    # Batch 01: 11 files from UNC一望5G (SA专题6+计费1+PCC静态4)
    sa_files = [
        '何为业务感知——What？_86009700.md', '使用业务感知——Why？_32687383.md',
        '业务感知概览_32946283.md', '相关概念_86169670.md',
        '业务感知流程_85850060.md', '结语_32789113.md',
        '计费解决方案_85721346.md',
        '何为PCC静态规则——What？_86169704.md', '使用PCC静态规则——Why？_32946325.md',
        'PCC静态规则原理——How？_86009740.md', '结语_33031965.md',
    ]

    # Batch 02: PCC QoS/AM中计费相关 (7 files from UNC一望5G)
    qos_files = [
        '5G PCC策略—E2E QoS管理机制_32945129.md',
        'SM策略之QoS的管理机制_32686211.md',
        'SM策略之QoS的下发与执行_33030755.md',
        'SMF发起的策略更新_85720414.md',
        'PCF发起的策略更新_86168492.md',
        'AMF功能演进介绍_32945513.md',
        'PCF发起的策略更新_85720808.md',
    ]

    # Batch 03: 200 files - 全部计费专题，不需要校验遗漏

    # Batch 04: 从batch-04文件解析
    sm_policy_files = [
        '整体介绍_86483627.md', '计费参数_86483630.md', '重定向_86483631.md',
        '概述_66416527.md', '配置示例_19416800.md', '业务配置逻辑_66336491.md',
        '概述_64489687.md', '配置示例_18009858.md', '业务配置逻辑_64569729.md',
        '概述_18099670.md', '配置示例_18259562.md', '业务配置逻辑_65059427.md',
        '需求描述_08571737.md', '整体方案设计_93907864.md',
        '需求描述_24058834.md', '套餐配置_24671552.md',
        '需求描述_08571766.md',
        '快速调测法_21200422.md', '信令调测法_67482083.md',
        '快速调测法_20442424.md', '信令调测法_20602326.md',
        '快速调测法_67920177.md', '信令调测法_67363127.md',
    ]
    ulcl_files = [
        '分流场景下的计费_97585673.md', '关键参数_51596268.md',
        '关键参数_51436464.md', '系统影响与约束_97556113.md',
        '系统影响与约束_97476021.md',
    ]
    fup_files = [
        '关键参数_70607723.md', '基于Gx接口策略控制_24087904.md',
        '基于N7接口策略控制_23928080.md', '系统影响与约束_70687833.md',
        '配置会话级累计流量策略控制_23928082.md',
        '关键参数_23928086.md', '基于Gx接口策略控制_70687837.md',
        '基于N7接口策略控制_70607727.md', '系统影响与约束_24087910.md',
        '配置业务级累计流量策略控制_70607729.md',
    ]
    fup_indirect = [
        '20.7.0 01（2021-08-30）_24087900.md', '特性映射_23928078.md',
        '调测会话级累计流量策略控制_24087906.md', '调测业务级累计流量策略控制_70687839.md',
        '原理描述_24087908.md',
    ]

    # Batch 05: 从文件解析Gy(167 all)/Gx(41)/PFCP(16)/融合计费(5)/会话流程(12)
    # Gy全部收录，不需要校验

    # Batch 06/07: 少量文件

    return {
        'PCC之SM策略': set(sm_policy_files),
        'ULCL分流': set(ulcl_files),
        'FUP': set(fup_files + fup_indirect),
    }


def scan_charging_keywords(filepath, keywords, max_lines=80):
    """扫描文件前N行，返回命中的关键词"""
    hits = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i >= max_lines:
                    break
                for kw in keywords:
                    if kw.lower() in line.lower():
                        hits.append((kw, i+1, line.strip()[:100]))
    except Exception as e:
        return [(f"READ_ERROR: {e}", 0, "")]
    return hits


def check_dir(dir_desc, rel_path, included_filenames):
    """检查一个目录下的所有md文件"""
    full_path = UNC_BASE / rel_path
    if not full_path.exists():
        print(f"  [WARN] 目录不存在: {full_path}")
        return []

    # 获取所有md文件
    all_mds = []
    for root, dirs, files in os.walk(full_path):
        for f in files:
            if f.endswith('.md'):
                all_mds.append(Path(root) / f)

    if not all_mds:
        print(f"  [INFO] 无md文件: {full_path}")
        return []

    # 找出未收录的文件
    missed = []
    for md_path in all_mds:
        fname = md_path.name
        # 检查文件名是否在已收录列表中
        if fname not in included_filenames:
            # 扫描内容
            hits = scan_charging_keywords(md_path, CHARGING_KEYWORDS)
            if hits:
                missed.append((md_path, hits))

    return missed


def main():
    print("=" * 70)
    print("计费文档清单完整性校验")
    print("=" * 70)

    included = load_included_files()

    # === 1. 校验PCC之SM策略 ===
    print("\n## 1. PCC之SM策略 (已收录23/79) ##")
    missed = check_dir(
        'PCC之SM策略',
        '网络部署/业务专题/5G PCC之SM策略解决方案',
        included['PCC之SM策略']
    )
    total_mds = sum(1 for _, _, files in os.walk(UNC_BASE / '网络部署/业务专题/5G PCC之SM策略解决方案')
                    for f in files if f.endswith('.md'))
    excluded = total_mds - len(included['PCC之SM策略'])
    print(f"  总文件: {total_mds}, 已收录: {len(included['PCC之SM策略'])}, 未收录: {excluded}")
    print(f"  未收录文件中命中计费关键词: {len(missed)}")
    for path, hits in missed:
        rel = path.relative_to(UNC_BASE)
        print(f"\n  [可能遗漏] {rel}")
        for kw, line_no, line_text in hits[:5]:
            print(f"    L{line_no} [{kw}]: {line_text}")

    # === 2. 校验ULCL分流 ===
    print("\n\n## 2. ULCL分流 (已收录5/60) ##")
    missed = check_dir(
        'ULCL分流',
        '网络部署/业务专题/5G Core ULCL分流解决方案',
        included['ULCL分流']
    )
    total_mds = sum(1 for _, _, files in os.walk(UNC_BASE / '网络部署/业务专题/5G Core ULCL分流解决方案')
                    for f in files if f.endswith('.md'))
    excluded = total_mds - len(included['ULCL分流'])
    print(f"  总文件: {total_mds}, 已收录: {len(included['ULCL分流'])}, 未收录: {excluded}")
    print(f"  未收录文件中命中计费关键词: {len(missed)}")
    for path, hits in missed:
        rel = path.relative_to(UNC_BASE)
        print(f"\n  [可能遗漏] {rel}")
        for kw, line_no, line_text in hits[:5]:
            print(f"    L{line_no} [{kw}]: {line_text}")

    # === 3. 校验FUP ===
    print("\n\n## 3. FUP (已收录15/15) ##")
    missed = check_dir(
        'FUP',
        '网络部署/业务专题/5G Core FUP解决方案',
        included['FUP']
    )
    total_mds = sum(1 for _, _, files in os.walk(UNC_BASE / '网络部署/业务专题/5G Core FUP解决方案')
                    for f in files if f.endswith('.md'))
    excluded = total_mds - len(included['FUP'])
    print(f"  总文件: {total_mds}, 已收录: {len(included['FUP'])}, 未收录: {excluded}")
    print(f"  未收录文件中命中计费关键词: {len(missed)}")
    for path, hits in missed:
        rel = path.relative_to(UNC_BASE)
        print(f"\n  [可能遗漏] {rel}")
        for kw, line_no, line_text in hits[:5]:
            print(f"    L{line_no} [{kw}]: {line_text}")

    # === 4. 校验Gx接口 (大量信元) ===
    print("\n\n## 4. Gx接口 (已收录41/182) ##")
    gx_dir = UNC_BASE / '快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/Gx'
    # 先从batch-05中提取已收录的Gx文件
    gx_included = set()
    batch05 = BATCH_DIR / 'batch-05-协议流程.md'
    if batch05.exists():
        with open(batch05, 'r', encoding='utf-8') as f:
            in_gx_section = False
            for line in f:
                if 'Gx接口' in line:
                    in_gx_section = True
                if in_gx_section and '## 3.' in line:
                    break
                if in_gx_section and line.startswith('- '):
                    fname = line.strip('- ').strip()
                    if fname.endswith('.md'):
                        gx_included.add(fname)

    total_mds = sum(1 for _, _, files in os.walk(gx_dir)
                    for f in files if f.endswith('.md'))
    excluded = total_mds - len(gx_included)
    print(f"  总文件: {total_mds}, 已收录: {len(gx_included)}, 未收录: {excluded}")

    # 对未收录的Gx文件做关键词扫描
    missed_gx = []
    for root, dirs, files in os.walk(gx_dir):
        for f in files:
            if f.endswith('.md') and f not in gx_included:
                fp = Path(root) / f
                hits = scan_charging_keywords(fp, [
                    'Charging', 'Quota', 'Rating', 'Usage', 'Metering',
                    'Offline', 'Online', 'Reporting', 'Rule',
                    '计费', '配额', '用量',
                ])
                if hits:
                    missed_gx.append((fp, hits))
    print(f"  未收录文件中命中计费关键词: {len(missed_gx)}")
    for path, hits in missed_gx[:20]:  # 限制输出
        rel = path.relative_to(UNC_BASE)
        print(f"\n  [可能遗漏] {rel}")
        for kw, line_no, line_text in hits[:3]:
            print(f"    L{line_no} [{kw}]: {line_text}")
    if len(missed_gx) > 20:
        print(f"\n  ... 还有 {len(missed_gx) - 20} 个文件省略")

    # === 5. 校验PFCP/N4/Sx ===
    print("\n\n## 5. PFCP (N4+Sx, 已收录16/63) ##")
    pfcp_included = set()
    if batch05.exists():
        with open(batch05, 'r', encoding='utf-8') as f:
            in_pfcp = False
            for line in f:
                if 'PFCP' in line and 'Usage Report' in line:
                    in_pfcp = True
                if in_pfcp and line.startswith('## ') and 'PFCP' not in line:
                    break
                if in_pfcp and line.startswith('- '):
                    fname = line.strip('- ').strip()
                    if fname.endswith('.md'):
                        pfcp_included.add(fname)

    # 扫描N4和Sx
    for pfcp_subdir in ['快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口',
                         '快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/Sx']:
        pfcp_path = UNC_BASE / pfcp_subdir
        if not pfcp_path.exists():
            continue
        missed_pfcp = []
        total = 0
        for root, dirs, files in os.walk(pfcp_path):
            for f in files:
                if f.endswith('.md'):
                    total += 1
                    if f not in pfcp_included:
                        fp = Path(root) / f
                        hits = scan_charging_keywords(fp, [
                            'Usage', 'Report', 'URR', 'Quota', 'Measure',
                            '计费', '配额', '用量',
                        ])
                        if hits:
                            missed_pfcp.append((fp, hits))

        subdir_name = Path(pfcp_subdir).name
        inc = sum(1 for root, dirs, files in os.walk(pfcp_path) for f in files if f.endswith('.md') and f in pfcp_included)
        print(f"\n  [{subdir_name}] 总: {total}, 已收录: {inc}, 命中关键词的遗漏: {len(missed_pfcp)}")
        for path, hits in missed_pfcp[:10]:
            rel = path.relative_to(UNC_BASE)
            print(f"    [可能遗漏] {rel}")
            for kw, line_no, line_text in hits[:2]:
                print(f"      L{line_no} [{kw}]: {line_text}")

    # === 6. 校验初始配置 ===
    print("\n\n## 6. 初始配置 (部分收录) ##")
    # 从batch-06提取已收录文件
    batch06 = BATCH_DIR / 'batch-06-配置运维.md'
    config_included = set()
    if batch06.exists():
        with open(batch06, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('- '):
                    fname = line.strip('- ').strip()
                    if fname.endswith('.md'):
                        config_included.add(fname)

    config_dir = UNC_BASE / '网络部署/初始配置'
    missed_config = []
    total = 0
    for root, dirs, files in os.walk(config_dir):
        for f in files:
            if f.endswith('.md'):
                total += 1
                if f not in config_included:
                    fp = Path(root) / f
                    hits = scan_charging_keywords(fp, [
                        '计费', 'URR', 'Quota', '配额', 'Charging',
                        'PCC', '策略', 'PCF', 'CHF', 'OCS',
                        '话单', '费率', 'CC',
                    ], max_lines=50)
                    if hits:
                        missed_config.append((fp, hits))

    print(f"  总文件: {total}, 已收录: {len(config_included)}, 命中关键词的遗漏: {len(missed_config)}")
    for path, hits in missed_config[:20]:
        rel = path.relative_to(UNC_BASE)
        print(f"\n  [可能遗漏] {rel}")
        for kw, line_no, line_text in hits[:3]:
            print(f"    L{line_no} [{kw}]: {line_text}")
    if len(missed_config) > 20:
        print(f"\n  ... 还有 {len(missed_config) - 20} 个文件省略")

    print("\n" + "=" * 70)
    print("校验完成")


if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    main()
