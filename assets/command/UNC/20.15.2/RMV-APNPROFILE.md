---
id: UNC@20.15.2@MMLCommand@RMV APNPROFILE
type: MMLCommand
name: RMV APNPROFILE（删除APN配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNPROFILE
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
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

# RMV APNPROFILE（删除APN配置）

## 功能

**适用网元：SGSN**

该命令用于删除APN的APN的概要信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>数据来源：整网规划<br>取值范围：1~62位字符串<br>默认值： 无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。说明：- APN网络标识不区分大小写。<br>- APNNI在APN中所处的位置，例如：example1.com.mnc123.mcc123.gprs，其中NI= example1.com， OI= mnc123.mcc123.gprs。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNPROFILE]] · APN配置（APNPROFILE）

## 使用实例

删除一条APNNI的概要配置，APNNI为INTERNET，可以用如下命令：

```
RMV APNPROFILE: APNNI="INTERNET";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN配置（RMV-APNPROFILE）_67474993.md`
