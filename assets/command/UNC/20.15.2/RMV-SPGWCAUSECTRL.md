---
id: UNC@20.15.2@MMLCommand@RMV SPGWCAUSECTRL
type: MMLCommand
name: RMV SPGWCAUSECTRL（删除SGW-C/PGW-C原因值控制参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SPGWCAUSECTRL
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- SM原因值管理
- GTPv2会话流程原因值控制
status: active
---

# RMV SPGWCAUSECTRL（删除SGW-C/PGW-C原因值控制参数）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于删除PGW-C或融合的SGW-C/PGW-C的原因值控制参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCEDURETYPE | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程类型。<br>数据来源：本端规划<br>取值范围：<br>- CRT_SES_PROC（初始会话创建流程）<br>- MOD_BR_PROC（承载修改流程）<br>默认值：无<br>配置原则：无 |
| CAUSESOURCE | 异常来源 | 可选必选说明：必选参数<br>参数含义：该参数用于指定发生异常的来源。<br>数据来源：本端规划<br>取值范围：<br>- UPF（UPF）<br>- POLICY_PCF（PCF策略）<br>- CHG_3GPP（3GPP计费）<br>- POLICY_PCRF（PCRF策略）<br>- RADIUS_AUTH（Radius鉴权）<br>- INNER（内部异常）<br>- RADIUS_CHG（Radius计费）<br>- DIAMETER_AAA（Diameter AAA）<br>- CHF_3GPP（3GPP CHF）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SPGWCAUSECTRL]] · SGW-C/PGW-C原因值控制参数（SPGWCAUSECTRL）

## 使用实例

删除会话创建流程中UPF异常的流程控制配置，执行如下命令：

```
RMV SPGWCAUSECTRL: PROCEDURETYPE=CRT_SES_PROC, CAUSESOURCE=UPF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SPGWCAUSECTRL.md`
