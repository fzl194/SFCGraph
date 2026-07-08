---
id: UNC@20.15.2@MMLCommand@ADD NRFPMNINTERFUNC
type: MMLCommand
name: ADD NRFPMNINTERFUNC（增加基于对端PLMN国际漫游功能参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFPMNINTERFUNC
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# ADD NRFPMNINTERFUNC（增加基于对端PLMN国际漫游功能参数）

## 功能

**适用NF：NRF**

此命令用于新增基于对端PLMN的国际漫游功能参数。

## 注意事项

- 该命令执行后立即生效。

- 若对某PLMN没有配置本命令中的策略，以SET NRFINTERFUNC配置的策略为准。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定对端PLMN的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定对端PLMN的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| INRF | 本NRF是否是国际漫游关口局NRF | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF基于指定的PLMN是否是漫游关口局NRF。<br>数据来源：全网规划<br>取值范围：<br>- YES（是）<br>- NO（否）<br>默认值：无<br>配置原则：<br>本NRF基于该PLMN是漫游关口局NRF时，需要配置为“YES”，一般用于异网漫游定制场景。 |
| PLMNNFSELPLY | 关口局NF选择策略 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF作为关口局NRF收到漫游服务发现请求时，对于关口局NF的选择策略。<br>数据来源：本端规划<br>取值范围：<br>- “PREFERED（优选关口局NF）”：服务发现结果中优选关口局NF<br>- “FILTER（排除关口局NF）”：服务发现结果中排除关口局NF<br>默认值：无<br>配置原则：<br>当运营商希望关口局NRF对于漫游发现请求回到归属省份NRF处理而不是关口局NRF直接处理时，需要将该参数配置为FILTER，否则配置为PREFERED。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFPMNINTERFUNC]] · 基于对端PLMN国际漫游功能参数（NRFPMNINTERFUNC）

## 使用实例

使用以下命令对移动国家码为123，移动网号为33的PLMN，配置本NRF为国际漫游关口局NRF，关口局NF的选择策略为PREFERED。

```
ADD NRFPMNINTERFUNC: MCC="123", MNC="33", INRF=YES, PLMNNFSELPLY=PREFERED;  
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NRFPMNINTERFUNC.md`
