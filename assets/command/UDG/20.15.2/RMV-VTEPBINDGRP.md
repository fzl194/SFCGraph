---
id: UDG@20.15.2@MMLCommand@RMV VTEPBINDGRP
type: MMLCommand
name: RMV VTEPBINDGRP（删除VXLAN隧道端点绑定隧道组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: VTEPBINDGRP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VTEP绑定VXLAN隧道组
status: active
---

# RMV VTEPBINDGRP（删除VXLAN隧道端点绑定隧道组）

## 功能

**适用NF：PGW-U、UPF**

![](删除VXLAN隧道端点绑定隧道组（RMV VTEPBINDGRP）_68194507.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除最后一个VTEP时，会导致使用该Vxlan组的数据业务不通。

该命令用于删除VXLAN隧道端点与隧道组的绑定关系。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令时，如果删除的是最后一个VTEP，会导致使用该Vxlan组的数据业务不通。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VXLANGRPNAME | VXLAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VXLAN隧道组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用 ADD VXLANGRP命令配置生成。 |
| VTEPNAME | VTEP名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VXLAN隧道端点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用 ADD VTEP命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VTEPBINDGRP]] · VXLAN隧道端点绑定隧道组（VTEPBINDGRP）

## 使用实例

删除所有隧道端点与VXLAN隧道组vxlangrp的绑定关系：

```
RMV VTEPBINDGRP: VXLANGRPNAME="vxlangrp";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-VTEPBINDGRP.md`
