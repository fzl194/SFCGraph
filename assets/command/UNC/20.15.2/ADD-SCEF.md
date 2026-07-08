---
id: UNC@20.15.2@MMLCommand@ADD SCEF
type: MMLCommand
name: ADD SCEF（增加SCEF配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SCEF
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Diameter应用协议
- SCEF管理
status: active
---

# ADD SCEF（增加SCEF配置）

## 功能

**适用网元：MME**

该命令用于配置SCEF信息。

## 注意事项

- 该命令执行后立即生效。
- 该表最大记录数为256。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCEFRLM | SCEF域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCEF域名。<br>数据来源：对端协商<br>取值范围：1~127位字符串<br>默认值：无<br>配置原则：<br>- 不允许配置字符串“NULL”。<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”，大小写不敏感。<br>- 与对端SCEF配置的SCEF域名保持一致。 |
| SCEFHTN | SCEF主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCEF主机名。<br>数据来源：对端协商<br>取值范围：1~127位字符串<br>默认值：无<br>配置原则：<br>- 不允许配置字符串“NULL”。<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”，大小写不敏感。<br>- 与对端SCEF配置的SCEF主机名保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCEF]] · SCEF配置（SCEF）

## 使用实例

增加SCEF域名为example01.com，SCEF主机名为scef0701.example01.com的一条记录：

ADD SCEF: SCEFRLM="example01.com", SCEFHTN="scef0701.example01.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SCEF.md`
