---
id: UNC@20.15.2@MMLCommand@CRE CHGCDR
type: MMLCommand
name: CRE CHGCDR（强制生成用户话单）
nf: UNC
version: 20.15.2
verb: CRE
object_keyword: CHGCDR
command_category: 调测类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 计费控制
status: active
---

# CRE CHGCDR（强制生成用户话单）

## 功能

**适用网元：SGSN**

该命令用于强制生成用户话单M-CDR或S-CDR。如果强制生成某一个用户的话单，强制生成话单结果可以实时得到。如果强制生成所有用户的话单，强制生成话单结果需要用命令 [**DSP CHGCDR**](显示强制生成用户话单的结果信息(DSP CHGCDR)_26305188.md) 查询得到。

## 注意事项

- 该命令执行后立即生效。
- 在强制生成所有用户话单时，耗时较长，占用系统资源较大，请谨慎使用。
- 如果对指定MSISDN生成话单，则对应的所有IMSI用户均生成话单。
- 若“MSISDN”与“IMSI”都不输入，表示强制生成所有用户的话单。
- 在multi IMSI功能开启的情况下，不支持根据MSISDN来强制生成话单。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDR | 话单类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识需要生成的话单类型。<br>数据来源：整网规划<br>取值范围：<br>- “S_CDR（S_CDR）”<br>- “M_CDR（M_CDR）”<br>默认值：无 |
| MSISDN | MSISDN | 可选必选说明：可选参数<br>参数含义：该参数用于标识模拟话单中包含的MSISDN。<br>数据来源：整网规划<br>取值范围：1～15位十进制字数字<br>默认值：无<br>说明：“MSISDN”<br>和<br>“IMSI”<br>不能同时输入。 |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于模拟话单中包含的IMSI。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGCDR]] · 强制生成用户话单（CHGCDR）

## 使用实例

1. 强制生成IMSI为“123432708000017”用户的M-CDR话单：
  CRE CHGCDR: CDR=M_CDR, IMSI="123432708000017";
2. 强制生成MSISDN为“8613902100004”用户的S-CDR话单：
  CRE CHGCDR: CDR=S_CDR, MSISDN="8613902100004";

## 证据

- 原始手册：`evidence/UNC/20.15.2/强制生成用户话单（CRE-CHGCDR）_26145374.md`
