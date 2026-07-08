---
id: UNC@20.15.2@MMLCommand@RMV APNNI
type: MMLCommand
name: RMV APNNI（删除APNNI）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNNI
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- APNNI信息管理
- APNNI管理
status: active
---

# RMV APNNI（删除APNNI）

## 功能

**适用网元：SGSN、MME**

该命令用来删除特定组中的APNNI成员。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPID | APNNI组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI组号。<br>数据来源：本端规划<br>取值范围：0～15<br>默认值：无<br>配置原则：该ID必须是<br>[**ADD APNNIGROUP**](../APNNI组管理/增加APNNI组(ADD APNNIGROUP)_26305508.md)<br>命令中已配置的ID记录。 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用来设置APNNI信息。<br>数据来源：本端规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNNI]] · APNNI（APNNI）

## 使用实例

删除组号为2的“APNNI组号”，“APNNI”为“HUAWEI.COM”。运行如下命令：

RMV APNNI: GRPID=2, APNNI="HUAWEI.COM";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APNNI(RMV-APNNI)_72345293.md`
