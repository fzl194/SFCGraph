---
id: UNC@20.15.2@MMLCommand@RMV VLRCTX
type: MMLCommand
name: RMV VLRCTX（删除VLR用户的上下文）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: VLRCTX
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- 用户上下文管理
status: active
---

# RMV VLRCTX（删除VLR用户的上下文）

## 功能

![](删除VLR用户的上下文（RMV VLRCTX）_53321878.assets/notice_3.0-zh-cn_2.png)

删除VLR用户上下文将影响用户正在进行的短消息业务。

**适用NF：SMSF**

该命令用于删除用户的VLR上下文。当功能调测或拨测过程中需要手动删除用户的VLR上下文时，使用该命令。

## 注意事项

- 该命令执行后立即生效。

- 删除VLR上下文将影响用户正在进行的短消息业务，请慎重使用此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVOPTION | VLR用户的识别码类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VLR用户的识别码类型。<br>数据来源：本端规划<br>取值范围：<br>- “IMSI（国际移动用户识别码）”：国际移动用户识别码<br>- “MSISDN（移动台国际ISDN号码）”：移动台国际ISDN号码<br>- “IMEI（国际移动设备标识）”：国际移动设备标识<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"RMVOPTION"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于表示VLR用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~15。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"RMVOPTION"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于表示VLR用户的MSISDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~15。<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：该参数在"RMVOPTION"配置为"IMEI"时为条件必选参数。<br>参数含义：该参数用于表示VLR用户的IMEI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~16。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLRCTX]] · VLR用户的上下文（VLRCTX）

## 使用实例

操作员在功能调测过程中手动删除值为“460023500100001”的IMSI对应的用户的VLR上下文，执行如下命令：

```
RMV VLRCTX: RMVOPTION=IMSI, IMSI="460023500100001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-VLRCTX.md`
