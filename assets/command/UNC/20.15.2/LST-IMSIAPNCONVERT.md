---
id: UNC@20.15.2@MMLCommand@LST IMSIAPNCONVERT
type: MMLCommand
name: LST IMSIAPNCONVERT（查询APNNI转换配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSIAPNCONVERT
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- APNNI转换管理
status: active
---

# LST IMSIAPNCONVERT（查询APNNI转换配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询APN（Access Point Name）转换配置。如果用户激活请求消息中携带的APN和本配置命令“OLDAPN（请求APNNI）”匹配，则用户激活请求消息中携带的APN将被替换为“NEWAPN（转换APNNI）”后再进行签约数据匹配。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定签约用户的范围。<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>取值范围：1~15位数字<br>默认值：无<br>说明：根据IMSI、<br>“请求APNNI”<br>映射唯一的<br>“转换APNNI”<br>。 |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定所查询的IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>取值范围：1~15位数字<br>默认值：无<br>说明：根据IMSI、<br>“请求APNNI”<br>映射唯一的<br>“转换APNNI”<br>。 |
| OLDAPN | 请求APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定激活请求消息中携带的APNNI。<br>取值范围：1~62<br>默认值：无<br>说明：- “请求APNNI”由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A~Z或a~z、数字0~9和中划线“-”。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |

## 操作的配置对象

- [APNNI转换配置（IMSIAPNCONVERT）](configobject/UNC/20.15.2/IMSIAPNCONVERT.md)

## 使用实例

查询所有APN NI转换配置记录：

LST IMSIAPNCONVERT:;

```
%%LST IMSIAPNCONVERT:;%%
RETCODE = 0  操作成功。

APN转换表
---------
用户范围        IMSI前缀    请求APNNI    APN转换                      转换APNNI    描述

所有用户        NULL        CDMA         对签约了野卡APN的用户启用    ABCD         NULL
指定IMSI前缀    12345       WCDMA        对号段内的用户都启用         EFG          NULL
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APNNI转换配置(LST-IMSIAPNCONVERT)_26145662.md`
