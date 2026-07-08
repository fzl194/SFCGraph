---
id: UNC@20.15.2@MMLCommand@DEA UPCCTX
type: MMLCommand
name: DEA UPCCTX（去激活用户面控制上下文）
nf: UNC
version: 20.15.2
verb: DEA
object_keyword: UPCCTX
command_category: 动作类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 去活UPC上下文
status: active
---

# DEA UPCCTX（去激活用户面控制上下文）

## 功能

![](去激活用户面控制上下文（DEA UPCCTX）_72615136.assets/notice_3.0-zh-cn_2.png)

该命令会去激活指定的签约用户。因为去活用户需要通知周边网元清除相关资源，所以当去活速率过高时，网络上会产生大量消息需要CPU进行处理，导致CPU使用率升高。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于去激活用户面控制上下文。

## 注意事项

- 该命令执行后立即生效。

- 该命令只去激活当前系统已有用户，即不会去激活该命令下发之后激活的用户。
- 当批量去激活用户时，系统负荷增大，CPU使用率会有一定程度的升高。待去激活完成后，系统会恢复正常。
- 若需设置去激活用户承载的速率，可以使用SET UPCSCANRATE命令。该命令设置的是整系统的去活承载速率，当系统内存在上下文核查或其他去活任务时，DEA UPCCTX命令实际的去活速率将降低。默认去激活用户承载的速率为1个每秒。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEATYPE | 去活方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定去活的类型。<br>数据来源：本端规划<br>取值范围：<br>- “IMSI（IMSI）”：按IMSI去激活用户<br>- “MSISDN（MSISDN）”：按MSISDN去激活用户<br>- “IMEI（IMEI）”：按IMEI去激活用户<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"DEATYPE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定国际移动用户标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"DEATYPE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定用户的MSISDN号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| IMEI | 国际移动用户识别码 | 可选必选说明：该参数在"DEATYPE"配置为"IMEI"时为条件必选参数。<br>参数含义：该参数用于指定国际移动设备标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是15~16。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPCCTX]] · 用户面控制上下文（UPCCTX）

## 使用实例

删除指定IMSI的用户面控制上下文:

```
DEA UPCCTX: DEATYPE = IMSI, IMSI="351521004992889";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DEA-UPCCTX.md`
