"""组装 Feature 节点 + feature_category/config_relevance 规则推断。

对齐 schema §2.1 三类字段：原始md字段(*_raw) + 抽取归一化字段 + 来源上下文字段。
feature_category：catalog_section 查表（35 分区精确映射）+ 兜底关键词。
config_relevance：has_activation_doc + section(ops) + no_config + dep_count 多规则。
"""
from __future__ import annotations

# catalog_section → feature_category 精确映射表（UDG 35 分区，来自 xlsx 产品清单）
# 划分依据：基本特性/底座→base；增值/增强能力→enhanced；运维/网管/可靠性→operations；
#          协议接入/承载→protocol；集成/第三方→integration
UDG_SECTION_CATEGORY: dict[str, str] = {
    "2/3/4G/5G业务基本特性": "base",
    "IP基本特性": "base",
    "NFV基本特性": "base",
    "年费基本包-组网演进基本包": "base",
    "年费基本包-分布式解决方案基本包": "base",
    "年费基本包-语音基本包": "base",
    "年费增值包-云化特性增值包": "base",
    "高性能解决方案基本包": "base",
    "年费增值包-业务感知解决方案增值包": "enhanced",
    "年费基本包-智能策略控制&计费基本包": "enhanced",
    "年费增值包-MBB可视化解决方案增值包": "enhanced",
    "年费增值包-PCC解决方案增值包": "enhanced",
    "GWFD-110400 智能计费防欺诈": "enhanced",
    "年费增值包-组网演进解决方案增值包": "enhanced",
    "移动VPN解决方案": "enhanced",
    "重点业务体验保障增值包": "enhanced",
    "年费增值包-安全解决方案增值包": "enhanced",
    "网络增值解决方案基本包": "enhanced",
    "国际漫游解决方案增值包": "enhanced",
    "网络加速卡流量加速单元": "enhanced",
    "绿色上网解决方案增值包": "enhanced",
    "拥塞小区分析增值包": "enhanced",
    "智能转发增值包": "enhanced",
    "智家随行增值包": "enhanced",
    "网管特性": "operations",
    "年费增值包-NB-IoT解决方案增值包": "operations",
    "灰度升级解决方案增值包": "operations",
    "SA特征库更新管控方案增值包": "operations",
    "双故障bypass增值包": "operations",
    "年费增值包-5G高速承载增值包": "protocol",
    "年费增值包-eMTC解决方案增值包": "protocol",
    "年费增值包-RedCap解决方案增值包": "protocol",
    "5G高速连接承载保障增值包": "protocol",
    "Proxy UPF漫游功能增值包": "protocol",
    "年费基本包-网络QoS管理基本包": "enhanced",   # QoS 管理是增强能力
}

# 兜底关键词（UNC 或 UDG 新分区未在表里时）
_SECTION_CATEGORY_FALLBACK = [
    (["计费", "策略控制", "PCC", "FUP"], "enhanced"),
    (["MBB", "可视化", "增值", "体验保障", "VPN", "安全", "漫游", "加速", "转发", "绿色上网"], "enhanced"),
    (["接入", "会话", "eMTC", "RedCap", "NB-IoT"], "protocol"),
    (["IP", "双栈", "地址"], "protocol"),
    (["QoS", "拥塞"], "enhanced"),
    (["可靠性", "故障", "自愈", "扩容", "缩容", "网管", "灰度", "升级", "bypass", "特征库"], "operations"),
    (["架构", "服务化", "NFV", "底座", "SA-Basic", "分布式", "语音", "高性能", "组网"], "base"),
    (["SFIP", "第三方", "集成"], "integration"),
]

# config_relevance: 网管/灰度/可靠性/特征库更新类 → ops_only
_OPS_SECTIONS = {
    "网管特性",
    "年费增值包-NB-IoT解决方案增值包",
    "灰度升级解决方案增值包",
    "SA特征库更新管控方案增值包",
    "双故障bypass增值包",
}


def infer_feature_category(catalog_section: str, definition: str, nf: str = "UDG") -> str:
    """优先查 nf 对应分区表；未命中走关键词兜底；都没命中默认 enhanced。"""
    table = UDG_SECTION_CATEGORY if nf == "UDG" else {}
    if catalog_section and catalog_section in table:
        return table[catalog_section]
    text = (catalog_section or "") + " " + (definition or "")
    for keywords, cat in _SECTION_CATEGORY_FALLBACK:
        if any(kw in text for kw in keywords):
            return cat
    return "enhanced"


def infer_config_relevance(has_activation: bool, no_config_needed: bool,
                           catalog_section: str = "", dep_count: int = 0) -> str:
    """多规则推断：ops section → ops_only；声明无需配置 → none；无激活但有依赖 → indirect；其余 required。"""
    if catalog_section in _OPS_SECTIONS:
        return "ops_only"
    if no_config_needed and not has_activation:
        return "none"
    if not has_activation and dep_count > 0:
        return "indirect"
    return "required"


def build_feature_node(seed: dict, raw_fields: dict, *, applicable_nf: list,
                       first_release: str, standards: list, overview_path: str | None,
                       nf: str, version: str, has_overview: str = "yes",
                       config_relevance: str = "required") -> dict:
    """组装单个 Feature 节点（四段式 id + 全部 *_raw + 归一化 + 上下文，不可变合并）。"""
    code = seed["feature_code"]
    node = {
        "id": f"{nf}@{version}@Feature@{code}",
        "feature_code": code,
        "name": seed.get("name", ""),
        "is_directory": seed.get("is_directory", False),
        "catalog_section": seed.get("catalog_section", ""),
        "parent_feature_code": seed.get("parent_feature_code", ""),
        "applicable_nf": applicable_nf,
        "nf_support_map": seed.get("nf_support_map", ""),
        "first_release_version": first_release,
        "standards": standards,
        "feature_category": infer_feature_category(seed.get("catalog_section", ""),
                                                    raw_fields.get("definition_raw", ""), nf=nf),
        "config_relevance": config_relevance,
        "nf": nf,
        "version": version,
        "source_path": overview_path or "",
        "has_overview": has_overview,
        "variant_dimensions": [],
    }
    return {**node, **raw_fields}
