---
id: UNC@20.15.2@MMLCommand@ADD NGPRA
type: MMLCommand
name: ADD NGPRA（增加5G PRA）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NGPRA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 网络开放管理
- 5G PRA管理
- 5G PRA标识管理
status: active
---

# ADD NGPRA（增加5G PRA）

## 功能

**适用NF：AMF**

该命令用于配置5G PRA（Presence Reporting Area）基本信息。PRA可分为核心网预定义PRA（Core Network predefined PRA）和UE专属PRA（UE-dedicated PRA）两种，其中在AMF上配置的PRA属于核心网预定义PRA。

## 注意事项

- 该命令执行后立即生效。

- 核心网预定义PRA的标识及其区域组成成员需要AMF与周边NF（如SMF、PCF）对齐规划后进行配置。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRAID | PRA标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示PRA区域的标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是8388608~16777215。<br>默认值：无<br>配置原则：无 |
| AREATYPE | 区域类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前PRA区域的区域类型。<br>数据来源：全网规划<br>取值范围：<br>- PUBLIC_AREA（公网区域）<br>- HIGH_RAIL_AREA（高铁区域）<br>默认值：PUBLIC_AREA<br>配置原则：<br>若本参数发生变更，可能会影响AMF向PCF上报的PRA状态。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于描述PRA。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGPRA]] · 5G PRA（NGPRA）

## 使用实例

运营商A需要在东湖大学校园部署PRA，其中PRA ID为8388616，执行如下命令：

```
ADD NGPRA: PRAID=8388616, DESC="for EastLake Campus";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NGPRA.md`
