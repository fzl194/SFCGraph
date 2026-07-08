---
id: UDG@20.15.2@MMLCommand@ADD VXLANBINDAPN
type: MMLCommand
name: ADD VXLANBINDAPN（新增VXLAN隧道组绑定APN）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: VXLANBINDAPN
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 1000
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VXLAN隧道绑定APN
status: active
---

# ADD VXLANBINDAPN（新增VXLAN隧道组绑定APN）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置VXLAN隧道组与APN的绑定关系。

## 注意事项

- 该命令最大记录数为1000。
- 执行该命令时，新增Vxlan组绑定APN会改变业务数据转发流程，数据报文会转发到MEP。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数必须已经通过ADD APN命令配置。 |
| VXLANGRPNAME | VXLAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VXLAN隧道组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数必须已经通过ADD VXLANGRP命令配置。 |

## 操作的配置对象

- [VXLAN隧道组绑定APN（VXLANBINDAPN）](configobject/UDG/20.15.2/VXLANBINDAPN.md)

## 使用实例

配置VXLAN隧道组与APN的绑定关系，执行如下命令：

```
ADD VXLANBINDAPN: APN="apn1", VXLANGRPNAME="vxlangrp";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/新增VXLAN隧道组绑定APN（ADD-VXLANBINDAPN）_68354109.md`
