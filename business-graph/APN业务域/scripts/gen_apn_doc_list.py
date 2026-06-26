#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
生成APN业务域文档清单。
- 特性: 11个(仅ID,按配置树三大类:地址分配/鉴权计费/接入方式),共122文件
- 业务专题: 4个APN核心专题(用户IP地址管理/UPF选择/接入控制/网元选择),展开所有md
- 5G基础知识概念: APN相关(地址分配/会话管理/网元选择/网络架构)
- 排除: MML命令文档、其他场景已纳入的业务专题、与APN无关的功能专题

参考: 带宽控制场景 scripts/gen_bandwidth_doc_list.py
"""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from typing import List, Tuple

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"D:\mywork\KnowledgeBase\SFCGraph"
UDG_ROOT = os.path.join(ROOT, "output", "UDG_Product_Documentation_CH_20.15.2")
UNC_ROOT = os.path.join(ROOT, "output", "UNC 20.15.2 产品文档(裸机容器) 05")
OUT_DIR = os.path.join(ROOT, "业务图谱体系", "APN业务域")


@dataclass(frozen=True)
class Feature:
    fid: str
    name: str
    product: str  # UDG | UNC | UDG+UNC
    category: str  # 地址分配 | 鉴权计费 | 接入方式
    fcount: int
    desc: str
    priority: str  # ★核心 | 辅助


@dataclass(frozen=True)
class Topic:
    product: str
    name: str
    abs_path: str
    desc: str


@dataclass(frozen=True)
class Concept:
    product: str
    name: str
    abs_path: str


# 37个特性(配置树11 + T1核心补全26),文件数与 apn-feature-doc-list.md 一致
FEATURES: Tuple[Feature, ...] = (
    # APN基础(会话管理+用户数据+APN专项)
    Feature("GWFD-010101", "会话管理", "UDG", "APN基础", 16, "会话管理(UPF侧)", "★核心"),
    Feature("WSFD-010501", "会话管理", "UNC", "APN基础", 8, "会话管理(SMF侧)", "★核心"),
    Feature("WSFD-010503", "多PDN/PDU功能", "UNC", "APN基础", 5, "多PDN/PDU并发会话", "★核心"),
    Feature("WSFD-010400", "用户数据管理", "UNC", "APN基础", 7, "用户签约数据(UDM交互)", "★核心"),
    Feature("WSFD-106203", "别名APN", "UNC", "APN基础", 10, "别名/虚拟APN", "★核心"),
    # 地址分配(OR)
    Feature("GWFD-010105", "用户面地址分配", "UDG", "地址分配", 10, "UPF分配(APN/DNN、SMF)", "★核心"),
    Feature("GWFD-010104", "地址分配方式", "UDG", "地址分配", 6, "地址分配方式总览", "★核心"),
    Feature("GWFD-020421", "基于位置的地址分配", "UDG", "地址分配", 5, "UPF分配(位置区,需License)", "★核心"),
    Feature("GWFD-010108", "用户面地址自动检测", "UDG", "地址分配", 5, "UPF地址探测", "辅助"),
    Feature("GWFD-010107", "静态地址用户路由冗余", "UDG", "地址分配", 9, "静态地址路由冗余", "辅助"),
    Feature("GWFD-020412", "L2TP VPN", "UDG", "地址分配", 15, "LNS分配(UPF侧)", "★核心"),
    Feature("WSFD-010502", "地址分配方式", "UNC", "地址分配", 5, "SMF/UDM/Radius/DHCP分配", "★核心"),
    Feature("WSFD-010504", "控制面地址分配方式", "UNC", "地址分配", 2, "控制面地址分配(SMF)", "★核心"),
    Feature("WSFD-104410", "L2TP VPN", "UNC", "地址分配", 5, "LNS分配(SMF侧)", "★核心"),
    Feature("WSFD-107021", "静态地址用户路由冗余", "UNC", "地址分配", 5, "静态地址路由冗余(SMF)", "辅助"),
    Feature("GWFD-020403", "IPv4v6双栈接入", "UDG", "地址分配", 5, "IPv4v6双栈(补全)★", "★核心"),
    Feature("WSFD-104002", "IPv4v6双栈接入", "UNC", "地址分配", 12, "IPv4v6双栈(SMF)★", "★核心"),
    Feature("GWFD-020401", "IPv6承载上下文", "UDG", "地址分配", 5, "IPv6承载上下文", "★核心"),
    Feature("WSFD-104001", "IPv6承载上下文", "UNC", "地址分配", 16, "IPv6承载上下文(SMF)", "★核心"),
    Feature("GWFD-020406", "IPv6 Prefix Delegation", "UDG", "地址分配", 12, "IPv6前缀代理", "★核心"),
    Feature("WSFD-104004", "IPv6前缀代理", "UNC", "地址分配", 8, "IPv6前缀代理(SMF)", "★核心"),
    Feature("WSFD-104413", "DHCP功能", "UNC", "地址分配", 2, "DHCPv4分配", "★核心"),
    Feature("WSFD-104005", "DHCPv6地址分配", "UNC", "地址分配", 2, "DHCPv6分配", "★核心"),
    # 鉴权计费(AND)
    Feature("WSFD-011305", "Radius鉴权接入", "UNC", "鉴权计费", 9, "AUTHMODE鉴权方式", "★核心"),
    Feature("WSFD-011306", "Radius功能", "UNC", "鉴权计费", 12, "Radius服务器配置", "★核心"),
    Feature("WSFD-010301", "鉴权功能", "UNC", "鉴权计费", 16, "基础鉴权功能(补全)", "★核心"),
    Feature("WSFD-108007", "终端二次鉴权", "UNC", "鉴权计费", 4, "终端二次鉴权", "辅助"),
    Feature("WSFD-011307", "Radius抄送功能", "UNC", "鉴权计费", 5, "Radius计费抄送", "辅助"),
    # 接入方式(OR)
    Feature("IPFD-015002", "GRE", "UDG+UNC", "接入方式", 8, "GRE隧道(SMF+UPF)", "★核心"),
    Feature("IPFD-015004", "IPSec功能", "UDG", "接入方式", 24, "IPSec隧道(UPF侧)", "★核心"),
    Feature("IPFD-016000", "IPSec功能", "UNC", "接入方式", 24, "IPSec隧道(SMF侧)", "★核心"),
    Feature("GWFD-020411", "MPLS VPN", "UDG", "接入方式", 9, "MPLS VPN(补全)", "★核心"),
    Feature("WSFD-104411", "MPLS VPN", "UNC", "接入方式", 9, "MPLS VPN(SMF)", "★核心"),
    # 网元选择
    Feature("WSFD-107010", "UPF选择", "UNC", "网元选择", 1, "SMF选UPF★", "★核心"),
    Feature("WSFD-010202", "基于位置区域对等网元选择", "UNC", "网元选择", 5, "位置区域对等网元选择", "辅助"),
    # 接入控制
    Feature("WSFD-106003", "用户接入控制功能", "UNC", "接入控制", 14, "用户接入控制(APN权限)", "★核心"),
    Feature("GWFD-010151", "接入控制", "UDG", "接入控制", 3, "接入控制(UPF侧)", "★核心"),
)

# 4个APN核心业务专题(其他场景排除、属于接入与会话管理域)
TOPICS: Tuple[Topic, ...] = (
    Topic("UDG", "5G Core 用户IP地址管理解决方案",
          os.path.join(UDG_ROOT, "特性部署", "业务专题", "5G Core 用户IP地址管理解决方案"),
          "★地址分配核心:UPF/SMF/UDM/Radius/DHCP地址管理方案"),
    Topic("UNC", "5G Core 用户IP地址管理解决方案",
          os.path.join(UNC_ROOT, "网络部署", "业务专题", "5G Core 用户IP地址管理解决方案"),
          "★地址分配核心(控制面视角)"),
    Topic("UNC", "UNC UPF选择专题",
          os.path.join(UNC_ROOT, "网络部署", "业务专题", "UNC UPF选择专题"),
          "★UPF选择:SMF为会话选择UPF"),
    Topic("UNC", "UNC接入控制专题",
          os.path.join(UNC_ROOT, "网络部署", "业务专题", "UNC接入控制专题"),
          "★接入控制:APN/DNN接入控制"),
    Topic("UNC", "UNC网元选择专题",
          os.path.join(UNC_ROOT, "网络部署", "业务专题", "UNC网元选择专题"),
          "★网元选择:AMF/SMF/UPF选择机制"),
)

# APN相关5G基础概念(UDG/UNC对称)
CONCEPTS: Tuple[Concept, ...] = (
    Concept("UDG", "地址分配",
            os.path.join(UDG_ROOT, "5G基础知识", "一望5G", "5G Core业务解决方案解读 - 地址分配")),
    Concept("UDG", "会话管理",
            os.path.join(UDG_ROOT, "5G基础知识", "一望5G", "会话管理")),
    Concept("UDG", "用户面网元选择",
            os.path.join(UDG_ROOT, "5G基础知识", "一望5G",
                         "5G Core业务解决方案解读 - 5G Core用户面网元选择")),
    Concept("UDG", "网元选择",
            os.path.join(UDG_ROOT, "5G基础知识", "一望5G",
                         "5G Core业务解决方案解读 - 5G Core网元选择")),
    Concept("UDG", "5G Core网络架构",
            os.path.join(UDG_ROOT, "5G基础知识", "一望5G", "5G Core网络架构")),
    Concept("UNC", "地址分配",
            os.path.join(UNC_ROOT, "5G基础知识", "一望5G", "5G Core业务解决方案解读 - 地址分配")),
    Concept("UNC", "会话管理",
            os.path.join(UNC_ROOT, "5G基础知识", "一望5G", "会话管理")),
    Concept("UNC", "用户面网元选择",
            os.path.join(UNC_ROOT, "5G基础知识", "一望5G",
                         "5G Core业务解决方案解读 - 5G Core用户面网元选择")),
    Concept("UNC", "网元选择",
            os.path.join(UNC_ROOT, "5G基础知识", "一望5G",
                         "5G Core业务解决方案解读 - 5G Core网元选择")),
    Concept("UNC", "5G Core网络架构",
            os.path.join(UNC_ROOT, "5G基础知识", "一望5G", "5G Core网络架构")),
)


def collect_md(abs_path: str) -> List[str]:
    """递归收集目录下所有md文件,返回相对ROOT的路径列表(排序)。"""
    result: List[str] = []
    if not os.path.exists(abs_path):
        return result
    for root, _dirs, files in os.walk(abs_path):
        for f in files:
            if f.endswith(".md"):
                rel = os.path.relpath(os.path.join(root, f), ROOT).replace(os.sep, "/")
                result.append(rel)
    return sorted(result)


def main() -> None:
    out: List[str] = []
    out.append("# APN业务域文档清单")
    out.append("")
    out.append("> 业务域: APN(接入与会话管理)")
    out.append("> 数据来源: UDG + UNC 产品文档")
    out.append("> 特性: 仅定位特性ID(用户后续单独阅读,详见 apn-feature-doc-list.md),按配置树三大类")
    out.append("> 业务专题、概念文档: 列出所有md文件,等权重")
    out.append("> 排除: MML命令文档、其他场景已纳入的业务专题、与APN无关的功能专题")
    out.append("")

    # 统计
    feat_files = sum(f.fcount for f in FEATURES)
    topic_md = {t: collect_md(t.abs_path) for t in TOPICS}
    topic_files = sum(len(v) for v in topic_md.values())
    concept_md = {c: collect_md(c.abs_path) for c in CONCEPTS}
    concept_files = sum(len(v) for v in concept_md.values())
    total = feat_files + topic_files + concept_files

    out.append("## 总览")
    out.append("")
    out.append("| 类别 | UDG | UNC | 合计 |")
    out.append("|------|-----|-----|------|")
    udg_only = sum(1 for f in FEATURES if "UDG" in f.product and "UNC" not in f.product)
    unc_only = sum(1 for f in FEATURES if "UNC" in f.product and "UDG" not in f.product)
    both = sum(1 for f in FEATURES if "UDG" in f.product and "UNC" in f.product)
    out.append(f"| 特性({len(FEATURES)}个,仅ID) | 独占{udg_only}+共享{both} | 独占{unc_only}+共享{both} | {len(FEATURES)}个 / {feat_files}文件 |")
    ut = sum(len(v) for t, v in topic_md.items() if t.product == "UDG")
    un = sum(len(v) for t, v in topic_md.items() if t.product == "UNC")
    out.append(f"| 业务专题(4个专题,5个目录) | {sum(1 for t in TOPICS if t.product=='UDG')}个 / {ut}文件 | {sum(1 for t in TOPICS if t.product=='UNC')}个 / {un}文件 | {len(TOPICS)}个 / {topic_files}文件 |")
    uc = sum(len(v) for c, v in concept_md.items() if c.product == "UDG")
    un_c = sum(len(v) for c, v in concept_md.items() if c.product == "UNC")
    out.append(f"| 5G基础知识概念(5个目录) | {sum(1 for c in CONCEPTS if c.product=='UDG')}个 / {uc}文件 | {sum(1 for c in CONCEPTS if c.product=='UNC')}个 / {un_c}文件 | {len(set(c.name for c in CONCEPTS))}个 / {concept_files}文件 |")
    out.append(f"| **合计** | - | - | **{total} md文件** |")
    out.append("")
    out.append("---")
    out.append("")

    # Section 1: 特性清单(按6大类)
    out.append("## Section 1: 特性清单(仅ID,按6大类)")
    out.append("")
    out.append("> 用户后续单独指定特性阅读,完整文件清单见 `apn-feature-doc-list.md`。")
    out.append("> 配置树主线: APN开通(AND) → [APN基础, 地址分配(OR), 鉴权计费(AND), 接入方式(OR)]; 补全: 网元选择, 接入控制")
    out.append("")
    cat_list = ("APN基础", "地址分配", "鉴权计费", "接入方式", "网元选择", "接入控制")
    node_map = {"APN基础": "AND(开通底座)", "地址分配": "OR(选其一)", "鉴权计费": "AND(必选)",
                "接入方式": "OR(选其一)", "网元选择": "必选", "接入控制": "必选"}
    for cat in cat_list:
        out.append(f"### 1.{cat_list.index(cat)+1} {cat} [{node_map[cat]}]")
        out.append("")
        out.append("| 特性ID | 特性名称 | 产品 | 文件数 | 优先级 | 说明 |")
        out.append("|--------|---------|------|--------|--------|------|")
        for f in FEATURES:
            if f.category == cat:
                out.append(f"| {f.fid} | {f.name} | {f.product} | {f.fcount} | {f.priority} | {f.desc} |")
        out.append("")
    out.append("---")
    out.append("")

    # Section 2: 业务专题
    out.append("## Section 2: 业务专题(展开md文件,等权重)")
    out.append("")
    batch = 1
    for t in TOPICS:
        mds = topic_md[t]
        out.append(f"### Batch-{batch:02d}: {t.name} ({t.product}, {len(mds)} files)")
        out.append("")
        out.append(f"> {t.desc}")
        out.append("")
        out.append("```")
        out.extend(mds)
        out.append("```")
        out.append("")
        out.append("---")
        out.append("")
        batch += 1

    # Section 3: 5G基础知识概念
    out.append("## Section 3: 5G基础知识概念文档(APN相关,等权重)")
    out.append("")
    for c in CONCEPTS:
        mds = concept_md[c]
        out.append(f"### {c.product} - {c.name} ({len(mds)} files)")
        out.append("")
        out.append("```")
        out.extend(mds)
        out.append("```")
        out.append("")
        out.append("---")
        out.append("")

    # Section 4: 排除说明
    out.append("## Section 4: 排除说明")
    out.append("")
    out.append("### 4.1 命令文档(不单独读取)")
    out.append("")
    out.append("- `output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/`")
    out.append("- `output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/`")
    out.append("- 说明: 命令细节从特性文档中提取。")
    out.append("")
    out.append("### 4.2 其他场景已纳入的业务专题(不重复)")
    out.append("")
    out.append("- 5G Core 计费解决方案 → 计费场景")
    out.append("- 5G Core FUP/重点业务保障/体验感知解决方案、5G PCC之SM策略解决方案 → 带宽控制场景")
    out.append("- 5G Core ULCL分流解决方案、UDG业务感知专题(访问限制部分) → 访问限制场景")
    out.append("")
    out.append("### 4.3 与APN无关的业务专题/功能专题")
    out.append("")
    out.append("UDG排除: IPv6组网/国际漫游/媒体中继/容灾/流控/智家随行 解决方案; UDG NAT/SFIP/vTCP_OPT/头增强/报表/防欺诈 功能专题")
    out.append("")
    out.append("UNC排除: 4_5G互操作/IPv6组网/NRF/容灾/流控 解决方案")
    out.append("")
    out.append("### 4.4 边缘相关(本次暂不纳入主体,按需补充)")
    out.append("")
    out.append("- UDG NAT功能专题(66文件): NAT涉及APN用户面地址转换,与地址分配边缘相关")
    out.append("- 5G Core 4_5G互操作解决方案: APN在4/5G互操作场景的地址保持行为")
    out.append("")
    out.append("### 4.5 边界判断")
    out.append("")
    out.append("**纳入APN业务域**: APN/DNN开通配置、地址分配(UPF/SMF/UDM/Radius/DHCP/LNS)、鉴权计费(Radius)、接入方式(GRE/IPSec/直连)、UPF/网元选择")
    out.append("")
    out.append("**未纳入(属于其他域)**: 业务感知后执行动作(计费/带宽/访问限制) → 业务感知域各场景")

    out_path = os.path.join(OUT_DIR, "apn-doc-list.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"Generated: {out_path}")
    print(f"Features: {len(FEATURES)} ({feat_files} files)")
    print(f"Topic files: {topic_files}")
    print(f"Concept files: {concept_files}")
    print(f"Grand total: {total} md files")


if __name__ == "__main__":
    main()
