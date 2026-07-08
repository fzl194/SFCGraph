---
id: UNC@20.15.2@MMLCommand@MOD EIR
type: MMLCommand
name: MOD EIR（修改EIR配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: EIR
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Diameter应用协议
- EIR管理
status: active
---

# MOD EIR（修改EIR配置）

## 功能

**适用网元：MME**

此命令用于修改EIR（Equipment Identity Register）表记录。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EIRRLM | EIR域名 | 可选必选说明：可选参数<br>参数含义：待修改的EIR域名。在不配置EIR主机名的情况下，MME根据EIR域名选择EIR。<br>数据来源：与对端EIR设备协商<br>取值范围：1～127位字符串<br>默认值：无<br>配置原则：<br>- 不支持空格。<br>- 与对端EIR配置的EIR域名保持一致。<br>- 参数只能包含“数字”、“字母”、“.”、“-”。 |
| EIRHTN | EIR主机名 | 可选必选说明：可选参数<br>参数含义：待修改的EIR主机名。在配置EIR主机名的情况下，MME根据配置中的EIR主机名选择EIR。<br>数据来源：与对端EIR设备协商<br>取值范围：1～127位字符串<br>默认值：无<br>配置原则：<br>- 不允许配置字符串“NULL”。<br>- 与对端EIR配置的EIR主机名保持一致。<br>- 参数只能包含“数字”、“字母”、“.”、“-”。 |

## 操作的配置对象

- [EIR配置（EIR）](configobject/UNC/20.15.2/EIR.md)

## 使用实例

修改EIR域名改为huawei01.com，EIR主机名改为eir0701.huawei01.com：

MOD EIR: EIRRLM="huawei01.com", EIRHTN="eir0701.huawei01.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改EIR配置(MOD-EIR)_72225133.md`
