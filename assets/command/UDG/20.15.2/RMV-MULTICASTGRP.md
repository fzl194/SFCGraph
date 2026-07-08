---
id: UDG@20.15.2@MMLCommand@RMV MULTICASTGRP
type: MMLCommand
name: RMV MULTICASTGRP（删除组播组配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: MULTICASTGRP
command_category: 配置类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN静态组播配置
- 组播组配置
status: active
---

# RMV MULTICASTGRP（删除组播组配置）

## 功能

**适用NF：UPF**

该命令用于删除静态组播组配置。

## 注意事项

- 该组播组记录必须已经存在。
- 该组播组内如果有IMSI或与5G LAN会话实例绑定，则不能删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCASTGRPNAME | 组播组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置组播组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63，区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MULTICASTGRP]] · 组播组配置（MULTICASTGRP）

## 使用实例

删除一个静态组播组配置：

```
RMV MULTICASTGRP: MCASTGRPNAME="group";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-MULTICASTGRP.md`
