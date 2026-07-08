---
id: UNC@20.15.2@MMLCommand@RMV SMCTX
type: MMLCommand
name: RMV SMCTX（删除SM上下文）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMCTX
command_category: 配置类
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
- 删除SM上下文
status: active
---

# RMV SMCTX（删除SM上下文）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除SM上下文。

## 注意事项

- 该命令执行后立即生效。

- 该命令仅用于内部调测，不对外使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 国际移动用户识别码 | 可选必选说明：该参数在"RMVTYPE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指示国际移动用户标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| KEYTYPE | 键值类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定会话删除类型。<br>数据来源：本端规划<br>取值范围：<br>- NSAPI（网络层服务接入点标识）<br>- LBI（4G缺省承载ID）<br>- PDUSESSIONID（PDU会话ID）<br>默认值：无<br>配置原则：无 |
| NSAPI | 网络层服务接入点标识 | 可选必选说明：该参数在"KEYTYPE"配置为"NSAPI"时为条件必选参数。<br>参数含义：该参数用于指示网络层服务接入点标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| LBI | LBI | 可选必选说明：该参数在"KEYTYPE"配置为"LBI"时为条件必选参数。<br>参数含义：该参数用于指示链接的EPS承载标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| PDUSESSIONID | PDU会话ID | 可选必选说明：该参数在"KEYTYPE"配置为"PDUSESSIONID"时为条件必选参数。<br>参数含义：该参数用于指示PDU会话标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| NOTIFYUE | 是否通知终端 | 可选必选说明：可选参数<br>参数含义：该参数用于指示是否通知终端。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| FORCEDEL | 指定用户删除方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定删除用户的方式。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：该参数在"RMVTYPE"配置为"IMEI"时为条件必选参数。<br>参数含义：该参数用于指定国际移动设备标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是15~16。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| RMVTYPE | 删除方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定删除的类型。<br>数据来源：本端规划<br>取值范围：<br>- “IMSI（IMSI）”：按IMSI删除用户<br>- “IMEI（IMEI）”：按IMEI删除用户<br>默认值：IMSI<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMCTX]] · 承载上下文（SMCTX）

## 使用实例

删除指定IMSI的PDUSESSION

```
RMV SMCTX:RMVTYPE = IMSI,  IMSI="351521004992889";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SM上下文（RMV-SMCTX）_09653768.md`
