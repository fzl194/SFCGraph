---
id: UDG@20.15.2@MMLCommand@MOD VTEPBINDGRP
type: MMLCommand
name: MOD VTEPBINDGRP（修改VXLAN隧道端点绑定隧道组）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: VTEPBINDGRP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VTEP绑定VXLAN隧道组
status: active
---

# MOD VTEPBINDGRP（修改VXLAN隧道端点绑定隧道组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改VXLAN隧道端点与隧道组的绑定关系的主备用类型。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VXLANGRPNAME | VXLAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VXLAN隧道组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用 ADD VXLANGRP命令配置生成。 |
| VTEPNAME | VTEP名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VXLAN隧道端点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用 ADD VTEP命令配置生成。 |
| PRIFLAG | 主备用类型 | 可选必选说明：必选参数<br>参数含义：指定VXLAN隧道端点主备用类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PRIMARY：主用。<br>- SECONDARY：备用。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VTEPBINDGRP]] · VXLAN隧道端点绑定隧道组（VTEPBINDGRP）

## 使用实例

将绑定在VXLAN隧道组vxlangrp的隧道端点vtep1修改为备用：

```
MOD VTEPBINDGRP: VXLANGRPNAME="vxlangrp", VTEPNAME="vtep1", PRIFLAG=SECONDARY;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改VXLAN隧道端点绑定隧道组（MOD-VTEPBINDGRP）_81234592.md`
