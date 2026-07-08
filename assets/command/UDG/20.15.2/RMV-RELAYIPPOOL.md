---
id: UDG@20.15.2@MMLCommand@RMV RELAYIPPOOL
type: MMLCommand
name: RMV RELAYIPPOOL（删除媒体中继IP池）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RELAYIPPOOL
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继回源IP池配置
status: active
---

# RMV RELAYIPPOOL（删除媒体中继IP池）

## 功能

**适用NF：UPF**

该命令用于删除媒体中继IP池。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | IP池名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置媒体中继IP池名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [媒体中继IP池（RELAYIPPOOL）](configobject/UDG/20.15.2/RELAYIPPOOL.md)

## 使用实例

假设需要删除媒体中继IP池，则命令如下：

```
RMV RELAYIPPOOL: POOLNAME="pool_relay";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除媒体中继IP池（RMV-RELAYIPPOOL）_24142603.md`
