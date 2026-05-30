# UNC L1 抽取结果审查报告

审查日期: 2026-05-25
审查范围: 5个代表性UNC特性的L1属性抽取准确性
审查文件:
- `l1_unc_feature_attributes.csv` (属性)
- `l1_unc_feature_dependency.csv` (依赖)
- `l1_unc_feature_license.csv` (License)
- `UNC_feature_files.csv` (文件路径)

---

## 1. WSFD-225003 (5G LAN业务基本功能)

**特性类型**: 无"概述"文件名但有完整overview内容的特性，7个关联文件

| 字段 | 抽取值 | 原文 | 判定 |
|------|--------|------|------|
| applicable_nf | AMF、SMF | "AMF、SMF" | ✅ 正确 |
| definition | 企业传统组网中...5G LAN解决方案正是为企业解决痛点应运而生。 | 第1段匹配 | ✅ 正确 |
| standards | 3GPP 23.501; 3GPP 23.502 | 表格中2条标准 | ✅ 正确 |
| first_release_version | 20.8.0 | 发布历史"20.8.0 首次发布" | ✅ 正确 |
| feature_type | business_policy | 涉及策略控制、有规格限制的特性 | ✅ 合理 |

**依赖检查** (l1_unc_feature_dependency.csv):

| source | target | type | 判定 |
|--------|--------|------|------|
| WSFD-225003 | WSFD-107010 | depends_on | ✅ 正确，原文"依赖该特性实现选择支持5G LAN的锚点UPF"一致 |

**License检查** (l1_unc_feature_license.csv):

❌ **缺失!** 原文明确记录:
> "82200EDD LKV2SALANSM01 5G LAN业务基本功能-USM"

但 `l1_unc_feature_license.csv` 中 **没有 WSFD-225003 的任何记录**。

**严重程度**: HIGH -- License信息完全缺失

---

## 2. WSFD-104001 (IPv6承载上下文)

**特性类型**: 多overview文件(AMF/SMF, MME/SGW-C/PGW-C, SGSN/GGSN三个NF视角)

| 字段 | 抽取值 | 原文 (AMF/SMF视角) | 判定 |
|------|--------|------|------|
| applicable_nf | AMF、SMF | "AMF、SMF" (AMF/SMF概述) | ✅ 正确 |
| definition | 本特性支持在5G网络的PDU会话建立流程中为UE分配IPv6前缀类型的地址... | AMF/SMF概述第1段匹配 | ✅ 正确 |
| standards | 3GPP 23.502 | AMF/SMF概述仅有23.502 | ✅ 正确 |
| first_release_version | 20.0.0 | AMF/SMF概述"20.0.0 首次发布" | ✅ 正确 |
| feature_type | config_enable | 功能激活类特性 | ✅ 合理 |

**注意**: 该特性有3个NF视角的overview文件，抽取结果基于AMF/SMF视角。MME/SGW-C/PGW-C和SGSN/GGSN视角的内容(不同NF、不同定义、不同License)未体现。这是设计选择，不是错误。

**License检查** (l1_unc_feature_license.csv):

| license_code | license_name | applicable_nf | 判定 |
|--------------|-------------|---------------|------|
| LKV2IPV6AM01 | IPv6承载上下文-UAM \| | (空) | ❌ 异常行 |
| LKV2IPV6AM01 | IPv6承载上下文-UAM | AMF | ✅ 正确 |
| LKV2IPV6SM01 | IPv6承载上下文-USM | SMF | ✅ 正确 |

**问题**: 第1行是冗余/错误行 -- license_name末尾有多余的 " |"，applicable_nf为空。原文AMF/SMF License表只有2行数据。

**严重程度**: MEDIUM -- 存在脏数据行(License名称带管道符后缀，NF为空)

---

## 3. WSFD-106403 (小区位置信息上报功能 S11接口)

**特性类型**: 多级目录嵌套特性（智能PCC解决方案 > 基于实时位置的策略控制 > 相关特性）

| 字段 | 抽取值 | 原文 | 判定 |
|------|--------|------|------|
| applicable_nf | MME | "MME" | ✅ 正确 |
| definition | 小区位置信息上报功能是指MME基于S-GW/P-GW下发的策略向RAN侧发起位置订阅... | 第1段完全匹配 | ✅ 正确 |
| standards | 3GPP 29.212; 3GPP 32.299; 3GPP 32.298; 3GPP 23.203; 3GPP 23.401; 3GPP 29.272; 3GPP 29.274 | 表格中7条标准完全一致 | ✅ 正确 |
| first_release_version | 20.0.0 | "20.0.0 首次发布" | ✅ 正确 |
| feature_type | business_policy | 策略驱动类特性 | ✅ 合理 |

**License检查**:

| license_code | license_name | applicable_nf | 判定 |
|--------------|-------------|---------------|------|
| LKV2LCR01 | 小区位置信息上报功能（S11接口） | (空) | ⚠️ 不完整 |

原文License写法是纯文本而非表格:
> "82207550 LKV2LCR01 小区位置信息上报功能（S11接口）"

未标注适用NF，抽取结果与原文一致。但基于 applicable_nf=MME，此处 applicable_nf 应补充为 MME。

**严重程度**: LOW -- License未解析出NF信息（原文格式为纯文本，非表格，导致NF无法自动提取）

---

## 4. WSFD-227102 (支持灰度拨测和发布)

**特性类型**: 简单的2文件特性(overview + 参考信息)

| 字段 | 抽取值 | 原文 | 判定 |
|------|--------|------|------|
| applicable_nf | (空) | "MME、SGW-C、PGW-C、AMF、SMF" | ❌ **严重缺失** |
| definition | 在完成首批次业务POD升级后，暂停升级过程... | 第1段匹配 | ✅ 正确 |
| standards | (空) | "本特性不涉及标准约束" | ✅ 正确(空值合理) |
| first_release_version | 20.12.0 | "20.12.0 首次发布" | ✅ 正确 |
| feature_type | config_enable | 操作维护类特性 | ✅ 合理 |

**applicable_nf 分析**: 原文"适用NF"部分明确列出 "MME、SGW-C、PGW-C、AMF、SMF"。抽取结果为空，说明解析失败。

原文格式为 `适用 N F`（N和F之间有空格），这可能导致正则匹配失败。

**严重程度**: CRITICAL -- 核心字段applicable_nf完全缺失

**License检查**:

| license_code | license_name | applicable_nf | 判定 |
|--------------|-------------|---------------|------|
| LKV2DTRABAM01 | 支持灰度拨测和发布-UAM \| | (空) | ❌ 异常行 |
| LKV2DTRABAM01 | 支持灰度拨测和发布-UAM | AMF | ✅ 正确 |
| LKV2DTRABSM01 | 支持灰度拨测和发布-USM | SMF | ✅ 正确 |

同WSFD-104001，存在一条脏数据行(名称带" |"，NF为空)。

**严重程度**: MEDIUM -- License存在脏数据行

---

## 5. WSFD-225001 (5G LAN组会话管理)

**特性类型**: 单文件特性(overview本身即是特性入口文件)

| 字段 | 抽取值 | 原文 | 判定 |
|------|--------|------|------|
| applicable_nf | SMF | "SMF" | ✅ 正确 |
| definition | 5G LAN是3GPP标准定义的针对企业用户2层组网需求的解决方案，在5G网络中原生虚拟了以太局域网，其应用和有线局域网网络一样广泛。 | 第1段匹配，但原文有4段定义 | ⚠️ 不完整(仅取首段) |
| standards | 3GPP 23.501; 3GPP 23.502 | 表格中2条标准 | ✅ 正确 |
| first_release_version | 20.8.0 | "20.8.0 首次发布" | ✅ 正确 |
| feature_type | config_enable | 功能配置类特性 | ✅ 合理 |

**严重程度**: LOW -- Definition仅抽取首段，丢失后续补充说明段落

---

## 汇总统计

| 特性 | applicable_nf | definition | standards | first_release | feature_type | 整体 |
|------|--------------|------------|-----------|---------------|-------------|------|
| WSFD-225003 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (License缺失) |
| WSFD-104001 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (License脏数据) |
| WSFD-106403 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (License缺NF) |
| WSFD-227102 | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ (NF缺失) |
| WSFD-225001 | ✅ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ |

## 发现的问题清单

### CRITICAL

| # | 问题 | 影响特性 | 根因分析 |
|---|------|---------|---------|
| C1 | applicable_nf 完全缺失 | WSFD-227102 | 原文标题格式为"适用 N F"（N和F之间有空格），正则匹配失败 |

### HIGH

| # | 问题 | 影响特性 | 根因分析 |
|---|------|---------|---------|
| H1 | License 信息完全缺失 | WSFD-225003 | License在原文"可获得性"章节中以纯文本描述(非表格)，可能未被解析到 |

### MEDIUM

| # | 问题 | 影响特性 | 根因分析 |
|---|------|---------|---------|
| M1 | License存在冗余脏数据行(name带"|"后缀，NF为空) | WSFD-104001, WSFD-227102 | 表格解析时将表头行或格式标记行一并抽取 |

### LOW

| # | 问题 | 影响特性 | 根因分析 |
|---|------|---------|---------|
| L1 | Definition 仅取首段，丢失补充说明 | WSFD-225001 | 只提取第一个段落作为definition |
| L2 | License 的 applicable_nf 为空 | WSFD-106403 | 原文License为纯文本格式，未包含NF表格 |

## 建议修复优先级

1. **C1**: 修复"适用NF"字段解析，增加对"适用 N F"等变体格式的兼容（有空格/换行）
2. **H1**: 增强License解析能力，支持纯文本格式的License描述（如"对应的License控制项为..."）
3. **M1**: 在License解析后去重，过滤 license_name 末尾带管道符的异常行，或检查表格解析是否多提取了一行
4. **L1/L2**: 属于已知的信息压缩取舍，可后续优化
