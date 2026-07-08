---
id: UDG@20.15.2@MMLCommand@RMV DFSRPAIR
type: MMLCommand
name: RMV DFSRPAIR（删除双发选收结对配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: DFSRPAIR
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN双发选收配置
- 双发选收结对配置
status: active
---

# RMV DFSRPAIR（删除双发选收结对配置）

## 功能

**适用NF：UPF**

该命令用于删除双发选收结对配置。

## 注意事项

- 该命令执行后立即生效。
- 该记录必须已经存在。
- 该双发选收结对内如果有IMSI或与5G LAN会话实例绑定，则不能删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DFSRPAIRID | 双发选收结对ID | 可选必选说明：必选参数<br>参数含义：该参数用于配置双发选收结对ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1-2048。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DFSRPAIR]] · 双发选收结对配置（DFSRPAIR）

## 使用实例

删除双发选收结对1：

```
RMV DFSRPAIR: DFSRPAIRID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-DFSRPAIR.md`
