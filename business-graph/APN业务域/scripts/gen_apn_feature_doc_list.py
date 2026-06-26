#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从CSV提取APN业务域11个特性的所有md路径，按配置树三大类(地址分配/鉴权计费/接入方式)
生成 apn-feature-doc-list.md。

参考: 带宽控制场景 scripts/gen_bandwidth_feature_doc_list.py
数据源: feature-graph/data/{UDG,UNC}_feature_files.csv
特性来源: APN配置树.md (专家梳理的配置树叶子节点)
"""
from __future__ import annotations

import csv
import os
import re
import sys
from dataclasses import dataclass
from typing import Dict, List, Tuple

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"D:\mywork\KnowledgeBase\SFCGraph"
OUT_DIR = os.path.join(ROOT, "业务图谱体系", "APN业务域")


@dataclass(frozen=True)
class Feature:
    """APN特性元数据。products 标注该特性归属的产品(UDG=UPF侧 / UNC=SMF侧)。"""

    fid: str
    name: str
    products: Tuple[str, ...]  # ('UDG',) | ('UNC',) | ('UDG','UNC')
    category: str  # 地址分配 | 鉴权计费 | 接入方式
    desc: str
    priority: str  # ★核心 | 辅助


# 37个特性(配置树11个 + T1核心补全26个),按6大类组织
# 补全来源:全量特性库扫描(UDG303+UNC595),T1核心为APN域主体(双栈/会话管理/IPv6/UPF选择等)
FEATURES: Tuple[Feature, ...] = (
    # === APN基础(会话管理+用户数据+APN专项,开通底座) ===
    Feature("GWFD-010101", "会话管理", ("UDG",), "APN基础",
            "会话管理基础(UPF侧,PDU会话建立/释放)", "★核心"),
    Feature("WSFD-010501", "会话管理", ("UNC",), "APN基础",
            "会话管理基础(SMF侧,PDU会话建立/释放)", "★核心"),
    Feature("WSFD-010503", "多PDN/PDU功能", ("UNC",), "APN基础",
            "支持多PDN/PDU并发会话", "★核心"),
    Feature("WSFD-010400", "用户数据管理", ("UNC",), "APN基础",
            "用户签约数据管理(UDM/UDR交互)", "★核心"),
    Feature("WSFD-106203", "别名APN", ("UNC",), "APN基础",
            "别名APN/虚拟APN(APN聚合与重定向)", "★核心"),
    # === 地址分配信息 (OR节点,选其一) ===
    Feature("GWFD-010105", "用户面地址分配", ("UDG",), "地址分配",
            "UPF分配:基于APN/DNN、基于SMF", "★核心"),
    Feature("GWFD-010104", "地址分配方式", ("UDG",), "地址分配",
            "用户面地址分配方式总览(配置树补全)", "★核心"),
    Feature("GWFD-020421", "基于位置的地址分配", ("UDG",), "地址分配",
            "UPF分配:基于位置区(需License LKV3G5LBAA01)", "★核心"),
    Feature("GWFD-010108", "用户面地址自动检测", ("UDG",), "地址分配",
            "UPF地址探测可靠性(PING/DNS/Tracert)", "辅助"),
    Feature("GWFD-010107", "静态地址用户路由冗余", ("UDG",), "地址分配",
            "静态地址用户路由冗余保护", "辅助"),
    Feature("GWFD-020412", "L2TP VPN", ("UDG",), "地址分配",
            "LNS分配(UPF侧,L2TP隧道PPP协商)", "★核心"),
    Feature("WSFD-010502", "地址分配方式", ("UNC",), "地址分配",
            "SMF分配/UDM静态/Radius/DHCP分配", "★核心"),
    Feature("WSFD-010504", "控制面地址分配方式", ("UNC",), "地址分配",
            "控制面地址分配方式(SMF侧)", "★核心"),
    Feature("WSFD-104410", "L2TP VPN", ("UNC",), "地址分配",
            "LNS分配(SMF侧,L2TP隧道PPP协商)", "★核心"),
    Feature("WSFD-107021", "静态地址用户路由冗余", ("UNC",), "地址分配",
            "静态地址用户路由冗余保护(SMF侧)", "辅助"),
    Feature("GWFD-020403", "IPv4v6双栈接入", ("UDG",), "地址分配",
            "IPv4v6双栈接入(配置树遗漏补全)★", "★核心"),
    Feature("WSFD-104002", "IPv4v6双栈接入", ("UNC",), "地址分配",
            "IPv4v6双栈接入(SMF侧)★", "★核心"),
    Feature("GWFD-020401", "IPv6承载上下文", ("UDG",), "地址分配",
            "IPv6承载上下文管理", "★核心"),
    Feature("WSFD-104001", "IPv6承载上下文", ("UNC",), "地址分配",
            "IPv6承载上下文管理(SMF侧)", "★核心"),
    Feature("GWFD-020406", "IPv6 Prefix Delegation", ("UDG",), "地址分配",
            "IPv6前缀代理(PD)", "★核心"),
    Feature("WSFD-104004", "IPv6前缀代理", ("UNC",), "地址分配",
            "IPv6前缀代理(SMF侧)", "★核心"),
    Feature("WSFD-104413", "DHCP功能", ("UNC",), "地址分配",
            "DHCPv4地址分配(SMF作DHCP Client)", "★核心"),
    Feature("WSFD-104005", "DHCPv6地址分配", ("UNC",), "地址分配",
            "DHCPv6地址分配", "★核心"),
    # === 鉴权计费信息 (AND节点,必选) ===
    Feature("WSFD-011305", "Radius鉴权接入", ("UNC",), "鉴权计费",
            "AUTHMODE鉴权方式(透明/透明鉴权/不透明/本地)", "★核心"),
    Feature("WSFD-011306", "Radius功能", ("UNC",), "鉴权计费",
            "Radius服务器配置(透明鉴权/不透明接入时必配)", "★核心"),
    Feature("WSFD-010301", "鉴权功能", ("UNC",), "鉴权计费",
            "基础鉴权功能(配置树补全)", "★核心"),
    Feature("WSFD-108007", "终端二次鉴权", ("UNC",), "鉴权计费",
            "终端二次鉴权(企业AAA场景)", "辅助"),
    Feature("WSFD-011307", "Radius抄送功能", ("UNC",), "鉴权计费",
            "Radius计费抄送", "辅助"),
    # === 接入方式信息 (OR节点,选其一) ===
    Feature("IPFD-015002", "GRE", ("UDG", "UNC"), "接入方式",
            "GRE隧道(SMF+UPF,轻量封装不加密,最多两层嵌套)", "★核心"),
    Feature("IPFD-015004", "IPSec功能", ("UDG",), "接入方式",
            "IPSec隧道(UPF侧,加密+认证)", "★核心"),
    Feature("IPFD-016000", "IPSec功能", ("UNC",), "接入方式",
            "IPSec隧道(SMF侧,加密+认证)", "★核心"),
    Feature("GWFD-020411", "MPLS VPN", ("UDG",), "接入方式",
            "MPLS VPN隧道(配置树补全)", "★核心"),
    Feature("WSFD-104411", "MPLS VPN", ("UNC",), "接入方式",
            "MPLS VPN隧道(SMF侧)", "★核心"),
    # === 网元选择 (APN会话选网元) ===
    Feature("WSFD-107010", "UPF选择", ("UNC",), "网元选择",
            "SMF为PDU会话选择UPF★", "★核心"),
    Feature("WSFD-010202", "基于位置区域对等网元选择", ("UNC",), "网元选择",
            "基于位置区域的对等网元选择", "辅助"),
    # === 接入控制 (APN接入权限) ===
    Feature("WSFD-106003", "用户接入控制功能", ("UNC",), "接入控制",
            "用户接入控制(APN接入权限)", "★核心"),
    Feature("GWFD-010151", "接入控制", ("UDG",), "接入控制",
            "接入控制(UPF侧)", "★核心"),
)


def load_feature_files(product: str) -> Dict[str, List[str]]:
    """读取 {product}_feature_files.csv,返回 {feature_id: [file_path,...]}。

    CSV 含 BOM 前缀,首列为 feature_id,file_path 列含 'path'。
    """
    csv_path = os.path.join(ROOT, "feature-graph", "data", f"{product}_feature_files.csv")
    result: Dict[str, List[str]] = {}
    with open(csv_path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fid_col = reader.fieldnames[0]
        path_col = next(
            (c for c in reader.fieldnames if "path" in c.lower()),
            reader.fieldnames[1],
        )
        for row in reader:
            fid = (row[fid_col] or "").strip()
            path = (row[path_col] or "").strip()
            if fid and path:
                result.setdefault(fid, []).append(path)
    return result


def extract_hash(path: str) -> str:
    """从文件路径提取末尾的数字hash,作为UDG/UNC同文档去重key。

    例: '.../GWFD-010105 用户面地址分配特性概述_68664421.md' -> '68664421'
    """
    m = re.search(r"_(\d+)\.md$", path)
    return m.group(1) if m else path


def collect_files(feat: Feature, udg_csv: Dict[str, List[str]],
                  unc_csv: Dict[str, List[str]]) -> List[str]:
    """收集特性文档,跨产品时合并UDG+UNC并按hash去重(保留UNC版,遵循SOP去重规则)。"""
    seen: Dict[str, str] = {}
    # UNC 优先录入(去重时保留UNC版),再补UDG独有
    for product, csv_data in (("UNC", unc_csv), ("UDG", udg_csv)):
        if product not in feat.products:
            continue
        for path in csv_data.get(feat.fid, []):
            key = extract_hash(path)
            if key not in seen:
                seen[key] = path
    return sorted(seen.values())


def build_markdown(udg_csv: Dict[str, List[str]],
                   unc_csv: Dict[str, List[str]]) -> Tuple[str, int]:
    out: List[str] = []
    out.append("# APN业务域特性文档清单")
    out.append("")
    out.append("> 业务域: APN(接入与会话管理)")
    out.append("> 从 `feature-graph/data/UDG_feature_files.csv` 和 `UNC_feature_files.csv` 提取")
    out.append(f"> 共 {len(FEATURES)} 个特性(配置树11 + T1核心补全26),按6大类组织(APN基础/地址分配/鉴权计费/接入方式/网元选择/接入控制)")
    out.append("> 特性来源: `APN配置树.md`(专家梳理的配置树叶子节点)")
    out.append("")

    # 总览表
    out.append("## 总览")
    out.append("")
    out.append("| # | 特性ID | 特性名称 | 产品 | 类别 | 文件数 | 优先级 | 说明 |")
    out.append("|---|--------|---------|------|------|--------|--------|------|")
    total = 0
    for idx, feat in enumerate(FEATURES, 1):
        files = collect_files(feat, udg_csv, unc_csv)
        total += len(files)
        prod = "+".join(feat.products)
        out.append(
            f"| {idx} | {feat.fid} | {feat.name} | {prod} | {feat.category} "
            f"| {len(files)} | {feat.priority} | {feat.desc} |"
        )
    out.append(f"| | | **合计** | | | **{total}** | | |")
    out.append("")
    out.append("---")
    out.append("")

    # 按类别分组的特性详情(6大类:配置树3类 + APN基础/网元选择/接入控制)
    categories = ("APN基础", "地址分配", "鉴权计费", "接入方式", "网元选择", "接入控制")
    batch_no = 0
    for cat in categories:
        out.append(f"## {cat}特性")
        out.append("")
        for feat in FEATURES:
            if feat.category != cat:
                continue
            batch_no += 1
            files = collect_files(feat, udg_csv, unc_csv)
            prod = "+".join(feat.products)
            nf = "/".join("UPF" if p == "UDG" else "SMF" for p in feat.products)
            out.append(
                f"### Batch-{batch_no:02d}: {feat.fid} {feat.name} "
                f"({prod}/{nf}, {len(files)} files) [{feat.priority}]"
            )
            out.append("")
            out.append(f"> {feat.desc}")
            out.append("")
            out.append("```")
            out.extend(files)
            out.append("```")
            out.append("")
            out.append("---")
            out.append("")

    return "\n".join(out), total


def main() -> None:
    udg_csv = load_feature_files("UDG")
    unc_csv = load_feature_files("UNC")
    md, total = build_markdown(udg_csv, unc_csv)
    out_path = os.path.join(OUT_DIR, "apn-feature-doc-list.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Generated: {out_path}")
    print(f"Total features: {len(FEATURES)}")
    print(f"Total md files: {total}")


if __name__ == "__main__":
    main()
