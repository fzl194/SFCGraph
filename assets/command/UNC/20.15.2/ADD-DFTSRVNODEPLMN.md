---
id: UNC@20.15.2@MMLCommand@ADD DFTSRVNODEPLMN
type: MMLCommand
name: ADD DFTSRVNODEPLMN（增加默认PLMN）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DFTSRVNODEPLMN
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 缺省服务节点PLMN
status: active
---

# ADD DFTSRVNODEPLMN（增加默认PLMN）

## 功能

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于配置UNC设备默认的PLMN，PLMN由MCC（Mobile Country Code，移动国家代码）和MNC（Mobile Network Code，移动网络码）组成。

## 注意事项

- 该命令执行后立即生效。

- 在判断接入用户为拜访或者漫游用户时，通过IP映射的方式获取不到用户接入的对端PLMN标识时，会获取该命令配置的默认PLMN标识作为该IP对应的PLMN标识。

- 最多可输入3条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 结点类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网元类型。<br>数据来源：本端规划<br>取值范围：<br>- SGSN（SGSN）<br>- SGW（SGW）<br>- PGW（PGW）<br>默认值：无<br>配置原则：无 |
| PLMNCODE | PLMN标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PLMN标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~6。PLMN字符串的格式为长度5-6的MCC+MNC，MCC长度为3个字符，MNC长度为2或者3个字符。字符：0~9。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DFTSRVNODEPLMN]] · 默认PLMN（DFTSRVNODEPLMN）

## 使用实例

设置PGW默认所属的PLMN为46001（MCC=460, MNC=01）：

```
ADD DFTSRVNODEPLMN:NODETYPE=PGW,PLMNCODE="46001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DFTSRVNODEPLMN.md`
