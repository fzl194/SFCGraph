---
id: UDG@20.15.2@MMLCommand@SET GLBDLBUFTIME
type: MMLCommand
name: SET GLBDLBUFTIME（设置全局下行数据缓存时长）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLBDLBUFTIME
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- GTP隧道管理
- 全局下行数据缓存时长
status: active
---

# SET GLBDLBUFTIME（设置全局下行数据缓存时长）

## 功能

**适用NF：UPF**

此命令用来配置全局的用户下行报文缓存时长。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令在不配置APN场景下生效。
- 下行数据报文缓存时长设置过大可能导致性能下降。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | NORMALUSER | NBIoTUser | REDCAPNRUSER |
| --- | --- | --- | --- |
| 初始值 | 6 | 6 | 6 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NORMALUSER | 普通用户下行数据缓存时长 | 可选必选说明：可选参数<br>参数含义：全局的普通用户下行报文缓存时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～15，单位是秒。<br>默认值：无<br>配置原则：无 |
| NBIOTUSER | NB-IoT用户下行数据缓存时长 | 可选必选说明：可选参数<br>参数含义：全局的NB-IoT用户下行报文缓存时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～200，单位是秒。<br>默认值：无<br>配置原则：无 |
| REDCAPNRUSER | RedCap-NR用户下行数据缓存时长 | 可选必选说明：可选参数<br>参数含义：全局的RedCap-NR用户下行报文缓存时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～200，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [全局下行数据缓存时长配置（GLBDLBUFTIME）](configobject/UDG/20.15.2/GLBDLBUFTIME.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00172]]

## 使用实例

配置全局普通用户下行报文缓存时长：

```
SET GLBDLBUFTIME: NORMALUSER=9;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置全局下行数据缓存时长（SET-GLBDLBUFTIME）_82837186.md`
