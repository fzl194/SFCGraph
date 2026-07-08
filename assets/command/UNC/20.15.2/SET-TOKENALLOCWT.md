---
id: UNC@20.15.2@MMLCommand@SET TOKENALLOCWT
type: MMLCommand
name: SET TOKENALLOCWT（设置服务类型分配权重的管理策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: TOKENALLOCWT
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 权重分配管理
- 权重分配策略
status: active
---

# SET TOKENALLOCWT（设置服务类型分配权重的管理策略）

## 功能

![](设置服务类型分配权重的管理策略（SET TOKENALLOCWT）_23736568.assets/notice_3.0-zh-cn_2.png)

该命令会调整不同Pod间的会话资源，调整过程中会导致容器短暂的内存升高和少量呼损。忙时操作会造成内存持续过载甚至流控，务必谨慎使用。配置该命令时，请联系华为技术支持。

**适用NF：SGW-C、PGW-C、SMF、GGSN、AMF**

该命令用于设置服务类型的负载均衡方式。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SERVICETYPE | WEIGHTPOLICY |
| --- | --- |
| UAM_0 | DEFAULT |
| USM_0 | DEFAULT |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务类型，开启对应的负载均衡策略。<br>数据来源：本端规划<br>取值范围：1、UAM会话管理组（UEAM与UEM） 2、USM会话管理服务（UESM、SMC、UPC、SM5GCM、STG、SM5GPOLICY）<br>- “UAM_0（UAM_0）”：涉及如下类型POD：接入/移动性管理POD。<br>- “USM_0（USM_0）”：涉及如下类型POD：会话管理POD。<br>默认值：无。<br>配置原则：无 |
| WEIGHTPOLICY | 权重策略 | 可选必选说明：必选参数<br>参数含义：该参数用于配置指定服务类型的负载均衡策略。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（默认策略）”：同类型POD按照同等比例进行业务分配。<br>- “STATIC（静态策略）”：支持人工指定POD NAME实例配置差异化的静态权重，开启后动态权重不生效。<br>- “DYNAMIC（动态策略）”：开启之后系统可以根据CPU利用率进行均衡调整，适用于SMF。<br>- “DEFAULTHET（默认异构策略）”：开启之后可根据CPU硬件能力进行业务分配。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TOKENALLOCWT]] · 服务类型分配权重的管理策略（TOKENALLOCWT）

## 使用实例

服务类型为USM_0，开启静态权重策略：

```
SET TOKENALLOCWT:SERVICETYPE=USM_0,WEIGHTPOLICY=STATIC;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-TOKENALLOCWT.md`
