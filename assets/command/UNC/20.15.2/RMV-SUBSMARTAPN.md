---
id: UNC@20.15.2@MMLCommand@RMV SUBSMARTAPN
type: MMLCommand
name: RMV SUBSMARTAPN（删除智能分流APN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SUBSMARTAPN
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 智能分流管理
status: active
---

# RMV SUBSMARTAPN（删除智能分流APN）

## 功能

**适用网元：MME**

该命令用户删除匹配用户签约APN智能分流配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | 智能分流APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定智能分流的APNNI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~62<br>默认值：无<br>配置原则：<br>- 智能分流APNNI由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。例如“HUAWEI.COM”<br>- 智能分流APNNI不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SUBSMARTAPN]] · 智能分流APN（SUBSMARTAPN）

## 使用实例

1. 删除APN1智能分流配置，可以用如下命令：
  ```
  RMV SUBSMARTAPN: APNNI="APN1";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除智能分流APN-(RMV-SUBSMARTAPN)_33902845.md`
