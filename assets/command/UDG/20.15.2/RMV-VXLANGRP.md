---
id: UDG@20.15.2@MMLCommand@RMV VXLANGRP
type: MMLCommand
name: RMV VXLANGRP（删除VXLAN组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: VXLANGRP
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
- VXLAN组信息
status: active
---

# RMV VXLANGRP（删除VXLAN组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除VXLAN隧道组。

## 注意事项

- 该命令执行后立即生效。
- 当要被删除的VXLAN隧道组被VTEP绑定时，VXLAN隧道组不能被删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPNAME | VXLAN隧道组名称 | 可选必选说明：可选参数<br>参数含义：VXLAN隧道组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [VXLAN组（VXLANGRP）](configobject/UDG/20.15.2/VXLANGRP.md)

## 使用实例

将名为vxlangrp的VXLAN隧道组删除：

```
RMV VXLANGRP: GRPNAME="vxlangrp";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除VXLAN组（RMV-VXLANGRP）_68194503.md`
