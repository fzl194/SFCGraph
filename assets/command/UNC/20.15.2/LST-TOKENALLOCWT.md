---
id: UNC@20.15.2@MMLCommand@LST TOKENALLOCWT
type: MMLCommand
name: LST TOKENALLOCWT（查询服务类型分配权重的管理策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TOKENALLOCWT
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 权重分配管理
- 权重分配策略
status: active
---

# LST TOKENALLOCWT（查询服务类型分配权重的管理策略）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN、AMF**

该命令用于查询负载均衡策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务类型，开启对应的负载均衡策略。<br>数据来源：本端规划<br>取值范围：1、UAM会话管理组（UEAM与UEM） 2、USM会话管理服务（UESM、SMC、UPC、SM5GCM、STG、SM5GPOLICY）<br>- “UAM_0（UAM_0）”：涉及如下类型POD：接入/移动性管理POD。<br>- “USM_0（USM_0）”：涉及如下类型POD：会话管理POD。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [服务类型分配权重的管理策略（TOKENALLOCWT）](configobject/UNC/20.15.2/TOKENALLOCWT.md)

## 使用实例

查询所有服务类型的负载均衡策略：

```
LST TOKENALLOCWT:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务类型分配权重的管理策略（LST-TOKENALLOCWT）_24015940.md`
