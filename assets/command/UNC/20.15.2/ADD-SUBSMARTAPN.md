---
id: UNC@20.15.2@MMLCommand@ADD SUBSMARTAPN
type: MMLCommand
name: ADD SUBSMARTAPN（增加智能分流APN）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SUBSMARTAPN
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 智能分流管理
status: active
---

# ADD SUBSMARTAPN（增加智能分流APN）

## 功能

**适用网元：MME**

该命令用于增加智能分流APN，当用户签约APN与该APN完全匹配时，系统标记用户为智能分流用户。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数为1024。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | 智能分流APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定智能分流的APNNI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~62<br>默认值：无<br>配置原则：<br>- 智能分流APNNI由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。例如“HUAWEI.COM”<br>- 智能分流APNNI不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |

## 操作的配置对象

- [智能分流APN（SUBSMARTAPN）](configobject/UNC/20.15.2/SUBSMARTAPN.md)

## 使用实例

1. 添加一条智能分流APNNI，可以用如下命令：
  ```
  ADD SUBSMARTAPN: APNNI="APN1";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加智能分流APN-(ADD-SUBSMARTAPN)_81502368.md`
