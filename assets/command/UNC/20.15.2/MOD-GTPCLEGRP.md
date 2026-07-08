---
id: UNC@20.15.2@MMLCommand@MOD GTPCLEGRP
type: MMLCommand
name: MOD GTPCLEGRP（修改GTP-C本地实体组）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD GTPCLEGRP（修改GTP-C本地实体组）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于修改GTP-C本地实体组的描述信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | 组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C本地实体所属的组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~31。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTP-C本地实体组的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCLEGRP]] · GTP-C本地实体组（GTPCLEGRP）

## 使用实例

修改0号GTP-C本地实体组的描述信息：

```
MOD GTPCLEGRP:GROUPID=0,DESC="for s5";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-GTPCLEGRP.md`
