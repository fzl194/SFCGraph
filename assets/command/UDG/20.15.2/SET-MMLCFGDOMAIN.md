---
id: UDG@20.15.2@MMLCommand@SET MMLCFGDOMAIN
type: MMLCommand
name: SET MMLCFGDOMAIN（批量设置绑定域信息）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: MMLCFGDOMAIN
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1000
category_path:
- 用户面服务管理
- 业务运维
- 集中配置管理
- 公共命令配置域信息管理
status: active
---

# SET MMLCFGDOMAIN（批量设置绑定域信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](批量设置绑定域信息（SET MMLCFGDOMAIN）_56064769.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行本命令后将批量修改配置的域信息，且无法回退。

本命令用于批量设置或修改网元配置的域信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CMDNAME | NEWDOMAINNAME | OLDDOMAINNAME |
| --- | --- | --- | --- |
| 初始值 | ADD APN | 0x0b4c0dbb | 0x0b4c0b9c |
| 初始值 | SET ApnSoftPara | 0x0b580dd2 | 0x0b584718 |
| 初始值 | SET ApnDLBufTime | 0x0b580dd5 | 0x0b580c04 |
| 初始值 | SET ApnAddressAttr | 0x0b580dd6 | 0x0b580ba6 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMDNAME | 公共配置命令名称 | 可选必选说明：必选参数<br>参数含义：公共配置命令名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| NEWDOMAINNAME | 域名称 | 可选必选说明：必选参数<br>参数含义：New Domain Name。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| OLDDOMAINNAME | 原始配置域名称 | 可选必选说明：可选参数<br>参数含义：原始配置域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 原始配置域名称可通过LST PUBCFGDOMAIN命令查询。 |

## 操作的配置对象

- [批量设置绑定域信息（MMLCFGDOMAIN）](configobject/UDG/20.15.2/MMLCFGDOMAIN.md)

## 使用实例

将ADD APN所配的原始域名为domain_b的配置的域信息批量修改为domain_a：

```
SET MMLCFGDOMAIN: CMDNAME="ADD APN", NEWDOMAINNAME="domain_a", OLDDOMAINNAME="domain_b";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/批量设置绑定域信息（SET-MMLCFGDOMAIN）_56064769.md`
