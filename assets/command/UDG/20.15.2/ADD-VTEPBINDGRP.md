---
id: UDG@20.15.2@MMLCommand@ADD VTEPBINDGRP
type: MMLCommand
name: ADD VTEPBINDGRP（增加VXLAN隧道端点绑定隧道组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: VTEPBINDGRP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 512
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VTEP绑定VXLAN隧道组
status: active
---

# ADD VTEPBINDGRP（增加VXLAN隧道端点绑定隧道组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于添加VXLAN隧道端点与VXLAN隧道组的绑定关系。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为512。
- 每个VXLAN组最多可以配置8个主隧道端点和8个备隧道端点。
- VXLAN隧道组和IPFARM开启心跳检测的链路，共可以配置512个，超出规格的链路，心跳检测失效，并且不会自动开启，链路为断开状态。
- 如果VXLAN隧道组已经被5G LAN会话实例绑定，要确保不同5G LAN会话实例不能使用相同的VNI和VTEP，否则会配置失败。
- 绑定到同一个VXLAN组的隧道端点要确保业务处理能力一致，如果隧道端点的业务处理能力不一致，则应新增VXLAN组绑定该隧道端点承载业务。
- 配置该命令时，若新加的VTEP和本组内的已有VTEP业务处理能力相同，则增加到本VxLAN组；若不一样，需要绑定到新的VxLAN组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VXLANGRPNAME | VXLAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VXLAN隧道组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用 ADD VXLANGRP命令配置生成。 |
| VTEPNAME | VTEP名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VXLAN隧道端点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用 ADD VTEP命令配置生成。 |
| PRIFLAG | 主备用类型 | 可选必选说明：可选参数<br>参数含义：指定VXLAN隧道端点主备用类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PRIMARY：主用。<br>- SECONDARY：备用。<br>默认值：PRIMARY<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VTEPBINDGRP]] · VXLAN隧道端点绑定隧道组（VTEPBINDGRP）

## 使用实例

配置隧道端点vtep1绑定在VXLAN隧道组vxlangrp上，且设置为主用类型：

```
ADD VTEPBINDGRP: VXLANGRPNAME="vxlangrp", VTEPNAME="vtep1", PRIFLAG=PRIMARY;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-VTEPBINDGRP.md`
