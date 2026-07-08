---
id: UNC@20.15.2@MMLCommand@RMV GGSNCAUSECTRL
type: MMLCommand
name: RMV GGSNCAUSECTRL（删除GGSN-C原因值控制参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GGSNCAUSECTRL
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- SM原因值管理
- GTPv1 PDP流程原因值控制
status: active
---

# RMV GGSNCAUSECTRL（删除GGSN-C原因值控制参数）

## 功能

**适用NF：GGSN**

该命令用于删除GGSN-C的原因值控制参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCEDURETYPE | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程类型，要根据场景来配置相应的流程。<br>数据来源：本端规划<br>取值范围：<br>- CRT_PDP_PROC（创建PDP流程）<br>- UPD_PDP_PROC（更新PDP流程）<br>默认值：无<br>配置原则：无 |
| CAUSESOURCE | 异常来源 | 可选必选说明：必选参数<br>参数含义：该参数用于描述发生异常的来源。<br>数据来源：本端规划<br>取值范围：<br>- UPF（UPF）<br>- POLICY_PCRF（PCRF策略）<br>- CHG_3GPP（3GPP计费）<br>- RADIUS_AUTH（Radius鉴权）<br>- INNER（内部异常）<br>- RADIUS_CHG（Radius计费）<br>- POLICY_PCF（PCF策略）<br>- CHF_3GPP（3GPP CHF）<br>默认值：无<br>配置原则：<br>POLICY_PCF以及CHF_3GPP网元类型仅在2G用户下生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GGSNCAUSECTRL]] · GGSN-C原因值控制参数（GGSNCAUSECTRL）

## 使用实例

删除创建PDP流程UPF异常的流程控制配置。

```
RMV GGSNCAUSECTRL: PROCEDURETYPE=CRT_PDP_PROC, CAUSESOURCE=UPF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GGSN-C原因值控制参数（RMV-GGSNCAUSECTRL）_25121201.md`
