---
id: UDG@20.15.2@MMLCommand@ADD NGBINDMCASTGRP
type: MMLCommand
name: ADD NGBINDMCASTGRP（增加5G LAN实例绑定组播组配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: NGBINDMCASTGRP
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 8192
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN静态组播配置
- 5G LAN实例绑定组播组
status: active
---

# ADD NGBINDMCASTGRP（增加5G LAN实例绑定组播组配置）

## 功能

**适用NF：UPF**

该命令用于把静态组播组绑定到5G LAN会话实例。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8192。
- 5G LAN组会话和静态组播组记录必须存在。
- 一个静态组播组只能绑定到一个5G LAN组会话实例。
- 同一个5G LAN组会话实例下绑定的静态组播组的组播MAC地址各不相同。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为18～37。<br>默认值：无<br>配置原则：无 |
| MCASTGRPNAME | 组播组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置组播组的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63，区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G LAN实例绑定组播组配置（NGBINDMCASTGRP）](configobject/UDG/20.15.2/NGBINDMCASTGRP.md)

## 使用实例

增加静态组播组和5G LAN会话实例绑定关系：

```
ADD NGBINDMCASTGRP: VNINSTANCE="a0000001-460-003-01", MCASTGRPNAME="group2";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加5G-LAN实例绑定组播组配置（ADD-NGBINDMCASTGRP）_15669945.md`
