---
id: UNC@20.15.2@MMLCommand@MOD NGPAGINGRULE
type: MMLCommand
name: MOD NGPAGINGRULE（修改5G寻呼规则）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGPAGINGRULE
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP接口寻呼管理
- NG寻呼规则管理
status: active
---

# MOD NGPAGINGRULE（修改5G寻呼规则）

## 功能

**适用NF：AMF**

此命令用于修改5G寻呼规则。通过此命令可以修改指定5G寻呼规则的“匹配优先级”、“寻呼动作组合”和“规则描述”。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULEIDX | 规则索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G寻呼规则的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 匹配优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本寻呼规则的匹配优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>优先级数值越小，代表优先级越高。<br>在业务匹配多条寻呼规则的场景下，优先级高的寻呼规则优先匹配。 |
| ACTGRP | 寻呼动作组合 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本寻呼规则使用的寻呼动作组合。<br>数据来源：本端规划<br>取值范围：<br>- “LAST_GNB（最近访问GNB）”：最近访问GNB<br>- “NEIGH_GNB（邻接GNB）”：邻接GNB<br>- “LAST_TA（最近访问TA）”：最近访问TA<br>- “NEIGH_TA（邻接TA ）”：邻接TA<br>默认值：无<br>配置原则：无 |
| DESC | 规则描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定寻呼规则的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPAGINGRULE]] · 5G寻呼规则（NGPAGINGRULE）

## 使用实例

修改“规则索引”为“1”的5G寻呼规则，将该5G寻呼规则的“匹配优先级”修改为“100”，“寻呼动作组合”修改为“LAST_GNB”，执行如下命令：

```
MOD NGPAGINGRULE: RULEIDX=1, PRIORITY=100, ACTGRP=LAST_GNB-1&NEIGH_GNB-0&LAST_TA-0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改5G寻呼规则（MOD-NGPAGINGRULE）_09652703.md`
