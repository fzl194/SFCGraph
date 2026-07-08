---
id: UNC@20.15.2@MMLCommand@RMV UPLIST4RDS
type: MMLCommand
name: RMV UPLIST4RDS（从RADIUS服务器使用的UP列表中删除UP）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UPLIST4RDS
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- UP列表
status: active
---

# RMV UPLIST4RDS（从RADIUS服务器使用的UP列表中删除UP）

## 功能

**适用NF：PGW-C、SMF**

![](从RADIUS服务器使用的UP列表中删除UP（RMV UPLIST4RDS）_52749061.assets/notice_3.0-zh-cn_2.png)

该命令属于高危命令，如果不输入UP主机名，表示删除UP列表下的所有UP，可能导致RADIUS计费功能失败，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

该命令用来从UP列表中删除UP，该UP列表用于根据UP选择RADIUS服务器，并向其发送RADIUS消息。

## 注意事项

- 该命令执行后立即生效。
- 当未输入UP主机名时，则删除UP列表下的所有UP，并导致RADIUS计费功能失败。
- 该命令中的UPLISTNAME被UPFRDSCLIENTIP或UPFRDSSVR绑定时，不允许对绑定在此UPLISTNAME下的UPINSTANCEID做增加和删除操作。如必须修改，请先解除UPLISTNAME与UPFRDSCLIENTIP或UPFRDSSVR的绑定，增加/删除UPLIST4RDS后再与UPFRDSCLIENTIP或UPFRDSSVR绑定。
- 该命令属于高危命令，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPLISTNAME | UP列表名称 | 可选必选说明：必选参数<br>参数含义：指定UP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。长度1到63的非空格字符串。<br>默认值：无<br>配置原则：无 |
| UPINSTANCEID | UP实例标识 | 可选必选说明：可选参数<br>参数含义：指定UP实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～36。字符串类型，输入长度范围是1~36。UpfHostName参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [从RADIUS服务器使用的UP列表中删除UP（UPLIST4RDS）](configobject/UNC/20.15.2/UPLIST4RDS.md)

## 使用实例

将主机名为"up1"的UP从名为"uplist1"的UP列表中删除：

```
RMV UPLIST4RDS: UPLISTNAME="uplist1", UPINSTANCEID="up1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/从RADIUS服务器使用的UP列表中删除UP（RMV-UPLIST4RDS）_52749061.md`
