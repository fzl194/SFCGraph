---
id: UNC@20.15.2@MMLCommand@RMV IMSIDT
type: MMLCommand
name: RMV IMSIDT（删除IMSI Direct Tunnel配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMSIDT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- Direct Tunnel管理
status: active
---

# RMV IMSIDT（删除IMSI Direct Tunnel配置）

## 功能

![](删除IMSI Direct Tunnel配置(RMV IMSIDT)_26146048.assets/notice_3.0-zh-cn_2.png)

删除了“IMSI”，可能会对系统产生重大影响。如果删除SUBRANGE=ALL_USER, DT=NO;配置，将会使默认情况下所有用户都支持DT，可能导致业务异常。

**适用网元：SGSN**

此命令用于删除IMSI DT属性信息表中的某个IMSI的DT属性记录。

## 注意事项

- 此命令执行后立即生效。
- 用户要使用DT功能还需满足RNC和GGSN支持DT功能。
- 本次命令删除了“IMSI”，可能会对系统产生重大影响。如果删除SUBRANGE=ALL_USER, DT=NO;配置，将会使默认情况下所有用户都支持DT，可能导致业务异常。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>- “IMSI_RANGE（指定IMSI范围）”<br>默认值：无<br>说明：使用时首先按照用户的IMSI在<br>“IMSI_PREFIX（指定IMSI前缀）”<br>或<br>“IMSI_RANGE（指定IMSI范围）”<br>进行查询，如果查询成功则使用该记录对应的配置；如果查询失败，则查询<br>“所有用户”<br>对应的配置记录，如果查询成功则使用<br>“所有用户”<br>的配置，如果查询还失败，则默认支持DT。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：当<br>“用户范围”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>取值范围：1~15位十进制字符串<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI，对该IMSI所在号段进行删除。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>取值范围：1~15位十进制字符串<br>默认值： 无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMSIDT]] · IMSI Direct Tunnel配置（IMSIDT）

## 使用实例

删除一条 “用户范围” 为 “指定IMSI前缀” ， “IMSI前缀” 为 “123456” 的IMSI DT权限属性记录：

RMV IMSIDT: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IMSIDT.md`
