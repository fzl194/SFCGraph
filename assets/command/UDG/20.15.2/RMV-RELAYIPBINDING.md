---
id: UDG@20.15.2@MMLCommand@RMV RELAYIPBINDING
type: MMLCommand
name: RMV RELAYIPBINDING（删除媒体中继服务IP绑定配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RELAYIPBINDING
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继服务IP绑定配置
status: active
---

# RMV RELAYIPBINDING（删除媒体中继服务IP绑定配置）

## 功能

**适用NF：UPF、PGW-U**

![](删除媒体中继服务IP绑定配置（RMV RELAYIPBINDING）_14541481.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除该配置后，会导致媒体中继业务中断。

该命令用于删除媒体中继服务IP配置和媒体中继模板名称的绑定关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYTPLNAME | 媒体中继模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示媒体中继模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD RELAYTEMPLATE命令配置生成。<br>- 配置时需要确保RELAYTPLNAME已经配置（ADD RELAYTEMPLATE）。 |
| RELAYIPNAME | 媒体中继IP地址名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示媒体中继服务IP配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD RELAYIPINFO命令配置生成。<br>- 配置时需要确保RELAYIPNAME已经配置（ADD RELAYIPINFO）。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYIPBINDING]] · 媒体中继服务IP绑定配置（RELAYIPBINDING）

## 使用实例

删除服务IP配置为testIP，模板名为test的绑定关系：

```
RMV RELAYIPBINDING: RELAYIPNAME="testIP", RELAYTPLNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-RELAYIPBINDING.md`
