---
id: UNC@20.15.2@MMLCommand@SET APNPCSCFSRVPRI
type: MMLCommand
name: SET APNPCSCFSRVPRI（设置APN P-CSCF地址获取方式的优先级配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: APNPCSCFSRVPRI
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- P-CSCF管理
- APN P-CSCF服务器优先级属性
status: active
---

# SET APNPCSCFSRVPRI（设置APN P-CSCF地址获取方式的优先级配置）

## 功能

**适用NF：PGW-C**

该命令用来配置获取P-CSCF方式的优先级，当用户既从DHCP服务器获取了P-CSCF地址，本地也配置了P-CSCF地址时，通过此命令配置本地P-CSCF地址优先或DHCP P-CSCF地址优先。

## 注意事项

- 该命令执行后立即生效。

- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：FIRMODEV4：DHCP，SECMODEV4：LOCAL，FIRMODEV6：DHCP，SECMODEV6：LOCAL。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无。<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| FIRMODEV4 | IPv4 第一优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4第一优先级选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的P-CSCF服务器属性优先。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNPCSCFSRVPRI查询当前参数配置值。<br>配置原则：无 |
| SECMODEV4 | IPv4 第二优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4第二优先级选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的P-CSCF服务器属性优先。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNPCSCFSRVPRI查询当前参数配置值。<br>配置原则：无 |
| FIRMODEV6 | IPv6 第一优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6第一优先级选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的P-CSCF服务器属性优先。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNPCSCFSRVPRI查询当前参数配置值。<br>配置原则：无 |
| SECMODEV6 | IPv6 第二优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6第二优先级选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的P-CSCF服务器属性优先。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNPCSCFSRVPRI查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNPCSCFSRVPRI]] · APN P-CSCF地址获取方式的优先级配置（APNPCSCFSRVPRI）

## 使用实例

配置APN名称为“huawei.com”的IPv4第一优先级选择模式为“LOCAL”，IPv4第二优先级选择模式为“DHCP”，IPv6第一优先级选择模式为“LOCAL”，IPv6第二优先级选择模式为“DHCP”：

```
SET APNPCSCFSRVPRI:APN="huawei.com",FIRMODEV4=LOCAL,SECMODEV4=DHCP,FIRMODEV6=LOCAL,SECMODEV6=DHCP;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置APN-P-CSCF地址获取方式的优先级配置（SET-APNPCSCFSRVPRI）_33845577.md`
