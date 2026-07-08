---
id: UDG@20.15.2@MMLCommand@RMV ICAPLOCALINFO
type: MMLCommand
name: RMV ICAPLOCALINFO（删除ICAP本端信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ICAPLOCALINFO
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- ICAPC管理
- ICAP本端信息
status: active
---

# RMV ICAPLOCALINFO（删除ICAP本端信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除ICAP本端信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSERVERTYPE | ICAP服务器类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- URL_FILTERING：支持URL过滤的ICAP服务器。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ICAPLOCALINFO]] · ICAP本端信息（ICAPLOCALINFO）

## 使用实例

删除一条ICAP本端信息，ICAPSERVERTYPE为URL_FILTERING的记录：

```
RMV ICAPLOCALINFO: ICAPSERVERTYPE=URL_FILTERING;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-ICAPLOCALINFO.md`
