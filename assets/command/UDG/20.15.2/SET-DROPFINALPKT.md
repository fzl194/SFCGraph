---
id: UDG@20.15.2@MMLCommand@SET DROPFINALPKT
type: MMLCommand
name: SET DROPFINALPKT（设置配额耗尽末包动作）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DROPFINALPKT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 配额耗尽末包动作
status: active
---

# SET DROPFINALPKT（设置配额耗尽末包动作）

## 功能

**适用NF：PGW-U、UPF**

本命令用于配置当配额耗尽时，UPF是否阻塞最后一个超出配额范围的数据报文。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH |
| --- | --- |
| 初始值 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 开关标识 | 可选必选说明：必选参数<br>参数含义：该参数用来配置配额耗尽时，UPF是否阻塞最后一个报文。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：最后一个报文不阻塞。<br>- ENABLE：最后一个报文阻塞。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DROPFINALPKT]] · 配额耗尽末包动作（DROPFINALPKT）

## 使用实例

若要配置UPF不阻塞最后一个超出配额范围的数据报文：

```
SET DROPFINALPKT: SWITCH=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-DROPFINALPKT.md`
