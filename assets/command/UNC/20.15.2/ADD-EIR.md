---
id: UNC@20.15.2@MMLCommand@ADD EIR
type: MMLCommand
name: ADD EIR（增加EIR配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: EIR
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
- Diameter应用协议
- EIR管理
status: active
---

# ADD EIR（增加EIR配置）

## 功能

**适用网元：MME**

此命令用于增加EIR（Equipment Identity Register）表记录。MME（Mobility Management Entity）根据EIR表记录选择EIR。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为1。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EIRRLM | EIR域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定EIR域名。在不配置EIR主机名的情况下，MME根据EIR域名选择EIR。<br>数据来源：与对端EIR设备协商<br>取值范围：1～127位字符串<br>默认值：无<br>配置原则：<br>- 不支持空格。<br>- 与对端EIR配置的EIR域名保持一致。<br>- 参数只能包含“数字”、“字母”、“.”、“-”。 |
| EIRHTN | EIR主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定EIR主机名。在配置EIR主机名的情况下，MME根据EIR主机名选择EIR。<br>数据来源：与对端EIR设备协商<br>取值范围：1～127位字符串<br>默认值：无<br>配置原则：<br>- 不允许配置字符串“NULL”。<br>- 与对端EIR配置的EIR主机名保持一致。<br>- 参数只能包含“数字”、“字母”、“.”、“-”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EIR]] · EIR配置（EIR）

## 使用实例

增加EIR域名为example01.com，EIR主机名为eir0701.example01.com的一条映射记录：

ADD EIR: EIRRLM="example01.com", EIRHTN="eir0701.example01.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加EIR配置(ADD-EIR)_72345049.md`
