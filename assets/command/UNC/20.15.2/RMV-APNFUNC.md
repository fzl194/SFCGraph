---
id: UNC@20.15.2@MMLCommand@RMV APNFUNC
type: MMLCommand
name: RMV APNFUNC（删除APNNI功能配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNFUNC
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- APN功能配置
status: active
---

# RMV APNFUNC（删除APNNI功能配置）

## 功能

**适用网元：SGSN**

该命令用于删除APNNI功能。

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>数据来源：整网规划<br>取值范围：长度不超过62的字符串<br>默认值： 无<br>配置原则：<br>- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。<br>说明：- APN网络标识不区分大小写。<br>- APNNI在APN中所处的位置，例如：huawei1.com.mnc.mcc.gprs，其中NI= huawei1.com， OI= mnc.mcc.gprs。 |
| APNPURPOSE | APN用途 | 可选必选说明：必选参数<br>参数含义：该参数决定了该APNNI所属用户是VIP用户。<br>数据来源：整网规划<br>取值范围：<br>- “VIP(VIP用户)”:标识该APNNI所属用户为VIP用户。<br>默认值： 无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNFUNC]] · APNNI功能配置（APNFUNC）

## 使用实例

删除APNNI为"huawei1.com"的VIP用户：

RMV APNFUNC: APNNI="huawei1.com", APNPURPOSE=VIP;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APNNI功能配置(RMV-APNFUNC)_72225335.md`
