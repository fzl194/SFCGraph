---
id: UDG@20.15.2@MMLCommand@RMV RELAYTEMPLATE
type: MMLCommand
name: RMV RELAYTEMPLATE（删除媒体中继模板）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RELAYTEMPLATE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继模板
status: active
---

# RMV RELAYTEMPLATE（删除媒体中继模板）

## 功能

**适用NF：PGW-U、UPF**

![](删除媒体中继模板（RMV RELAYTEMPLATE）_64063388.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除该配置后，会导致媒体中继业务中断

该命令用于删除一组媒体中继模板。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYTPLNAME | 媒体中继模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定媒体中继模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [媒体中继模板（RELAYTEMPLATE）](configobject/UDG/20.15.2/RELAYTEMPLATE.md)

## 使用实例

如果要删除一组媒体中继模板，则配置命令如下：

```
RMV RELAYTEMPLATE:RELAYTPLNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除媒体中继模板（RMV-RELAYTEMPLATE）_64063388.md`
