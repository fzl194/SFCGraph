---
id: UNC@20.15.2@MMLCommand@SET SMARTCL
type: MMLCommand
name: SET SMARTCL（设置智能分流功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMARTCL
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 智能分流管理
status: active
---

# SET SMARTCL（设置智能分流功能）

## 功能

**适用网元：MME**

该命令用于设置智能分流功能参数。

## 注意事项

- 该命令执行后立即生效。

- 此命令的最大记录数为1。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMARTCLSW | 智能分流开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置系统智能分流开关。<br>数据来源：全网规划<br>取值范围：<br>- OFF（关闭）<br>- ON（打开）<br>系统初始设置值：OFF（关闭）<br>配置原则：<br>- 当该参数设置为"ON（打开）"时，系统会根据用户签约和本地配置，判断用户是否是智能分流用户。如果用户是智能分流用户并且会话建立时的请求APN开启了智能分流功能，该会话将选择专用PGW-C。<br>- 当该参数设置为“OFF（关闭）”时，系统不区分智能分流用户和普通用户，执行通用PGW-C选择策略。<br>说明：此参数选择“ON(打开)”时，需要设置参数APNKEY（APN智能分流关键字）。 |
| APNKEY | APN智能分流关键字 | 可选必选说明：分支必选参数<br>参数含义：该参数用于设置智能分流APN关键字，当用户签约APN包含该关键字时，用户被标识为智能分流用户。智能分流用户对应APN开启专用PGW-C选择功能时，关键字作为定制LABEL拼接在FQDN中查询专用PGW-C。<br>前提条件：该参数在“SMARTCLSW”配置为“ON（打开）”时生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~62<br>系统初始设置值：无<br>配置原则：<br>- APN智能分流关键字由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。例如“HUAWEI.COM”。<br>- APN智能分流关键字不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |
| LABELPOS | APN智能分流关键字定制标识位置 | 可选必选说明：分支必选参数<br>参数含义：该参数用于配置定制LABEL在FQDN拼接时的位置信息。<br>前提条件：该参数在“SMARTCLSW”配置为“ON（打开）”时生效。<br>数据来源：全网规划<br>取值范围：<br>- BEFORE（BEFORE）：表示使用定制LABLE添加在APN前组装FQDN去查询DNS。<br>- AFTER（AFTER）：表示使用定制LABLE添加在APN后组装FQDN去查询DNS。<br>系统初始设置值：无<br>配置原则：无 |

## 操作的配置对象

- [智能分流功能（SMARTCL）](configobject/UNC/20.15.2/SMARTCL.md)

## 使用实例

设置启用智能分流功能，APN智能分流关键字设置为"multidomain"：

```
SET SMARTCL: SMARTCLSW=ON, APNKEY="multidomain", LABELPOS=BEFORE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置智能分流功能(SET-SMARTCL)_76951144.md`
