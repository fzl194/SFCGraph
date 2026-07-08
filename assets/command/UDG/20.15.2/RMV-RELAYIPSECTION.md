---
id: UDG@20.15.2@MMLCommand@RMV RELAYIPSECTION
type: MMLCommand
name: RMV RELAYIPSECTION（删除媒体中继IP段）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RELAYIPSECTION
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继回源IP段配置
status: active
---

# RMV RELAYIPSECTION（删除媒体中继IP段）

## 功能

**适用NF：UPF**

![](删除媒体中继IP段（RMV RELAYIPSECTION）_73589010.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除回源IP段可能会导致用户连接中断，业务受损。

该命令用于删除媒体中继IP段。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | IP池名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定媒体中继IP段对应的IP池名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：IP池名与IP段ID不能与已有媒体中继IP段冲突。 |
| SECTIONID | IP段ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定媒体中继IP段ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0~4294967295。<br>默认值：无<br>配置原则：IP池名与IP段ID不能与已有媒体中继IP段冲突。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYIPSECTION]] · 媒体中继IP段（RELAYIPSECTION）

## 使用实例

假设需要删除媒体中继IP段，则命令如下：

```
RMV RELAYIPSECTION: POOLNAME="pool_relay", SECTIONID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-RELAYIPSECTION.md`
