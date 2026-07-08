---
id: UDG@20.15.2@MMLCommand@MOD MULTICASTGRP
type: MMLCommand
name: MOD MULTICASTGRP（修改组播组配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: MULTICASTGRP
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN静态组播配置
- 组播组配置
status: active
---

# MOD MULTICASTGRP（修改组播组配置）

## 功能

**适用NF：UPF**

该命令用于修改静态组播组配置。

## 注意事项

- 该命令执行后立即生效。
- 该组播组记录必须已经存在。
- 该组播组如果与5G LAN会话实例绑定，则不能修改。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCASTGRPNAME | 组播组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置组播组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63，区分大小写。<br>默认值：无<br>配置原则：无 |
| MCASTMACADDR | 组播MAC地址 | 可选必选说明：必选参数<br>参数含义：该参数用于配置组播MAC地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度为17位。字符串应符合MAC地址格式，如11-11-11-11-11-11。组播类型的MAC地址从左到右第一个字节的最后一个bit为1。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MULTICASTGRP]] · 组播组配置（MULTICASTGRP）

## 使用实例

修改静态组播组配置：

```
MOD MULTICASTGRP: MCASTGRPNAME="group", MCASTMACADDR="11-11-11-11-11-11";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改组播组配置（MOD-MULTICASTGRP）_15869841.md`
