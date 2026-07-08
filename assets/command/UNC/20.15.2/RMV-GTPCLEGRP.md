---
id: UNC@20.15.2@MMLCommand@RMV GTPCLEGRP
type: MMLCommand
name: RMV GTPCLEGRP（删除GTP-C本地实体组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPCLEGRP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C本地实体组
status: active
---

# RMV GTPCLEGRP（删除GTP-C本地实体组）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于删除GTP-C本地实体组。

## 注意事项

- 该命令执行后立即生效。

- 如果需要删除本地实体组，需要删除该组号对应的接口和本地实体组成员，当组号被ADD GTPCINTF或者ADD GTPCLEGRPMEM引用时，先删除其引用关系再删除本地实体组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | 组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C本地实体所属的组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCLEGRP]] · GTP-C本地实体组（GTPCLEGRP）

## 使用实例

删除0号GTP-C本地实体组：

```
RMV GTPCLEGRP:GROUPID=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GTP-C本地实体组（RMV-GTPCLEGRP）_09653192.md`
