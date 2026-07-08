---
id: UDG@20.15.2@MMLCommand@RMV RELAYIPINFO
type: MMLCommand
name: RMV RELAYIPINFO（删除媒体中继IP信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RELAYIPINFO
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
- 媒体中继IP地址信息
status: active
---

# RMV RELAYIPINFO（删除媒体中继IP信息）

## 功能

**适用NF：PGW-U、UPF**

![](删除媒体中继IP信息（RMV RELAYIPINFO）_64063390.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除该配置后，会导致媒体中继业务中断。

该命令用于删除媒体中继IP信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYIPNAME | 媒体中继IP地址名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示媒体中继服务IP配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPSERVICETYPE | IP业务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示IP业务类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GROUPIP：表示填写的IP地址是组级IP。<br>- REDIRECTIP：表示填写的IP地址是重定向IP。<br>默认值：无<br>配置原则：无 |
| INSTID | 实例ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPSERVICETYPE”配置为“REDIRECTIP”时为可选参数。<br>参数含义：该参数用于表示实例ID。<br>数据来源：本端规划<br>取值范围：对应RelayPodID(0~15)。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYIPINFO]] · 媒体中继IP信息（RELAYIPINFO）

## 使用实例

删除服务IP配置为test的IP信息：

```
RMV RELAYIPINFO:  RELAYIPNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-RELAYIPINFO.md`
