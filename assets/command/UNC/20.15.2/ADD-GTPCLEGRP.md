---
id: UNC@20.15.2@MMLCommand@ADD GTPCLEGRP
type: MMLCommand
name: ADD GTPCLEGRP（增加GTP-C本地实体组）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD GTPCLEGRP（增加GTP-C本地实体组）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于增加一个GTP-C本地实体组，一个实体组内可以包含多个实体，便于管理。实体组配合ADD GTPCLEGRPMEM使用生成WLR路由。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入32条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | 组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C本地实体所属的组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~31。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTP-C本地实体组的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTPCLEGRP]] · GTP-C本地实体组（GTPCLEGRP）

## 使用实例

增加一个组号为0的GTP-C本地实体组：

```
ADD GTPCLEGRP:GROUPID=0,DESC="for s11";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-GTPCLEGRP.md`
