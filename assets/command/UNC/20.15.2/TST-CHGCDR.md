---
id: UNC@20.15.2@MMLCommand@TST CHGCDR
type: MMLCommand
name: TST CHGCDR（模拟SGSN话单）
nf: UNC
version: 20.15.2
verb: TST
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

# TST CHGCDR（模拟SGSN话单）

## 功能

**适用网元：SGSN**

该命令用于模拟生成SGSN话单。话单由SPP或UPP进程生成，生成后发往CDP进程，并存储在SPU硬盘或者发往CG。在新建局时，需要对本局点的计费网络及计费功能进行调测，用以验证SGSN与CG之间对接数据配置的正确性及接口状态是否正常，保证SGSN与CG之间接口可以正常工作。

## 注意事项

- 该命令执行后立即生效。
- 要模拟生成话单必须满足以下几个条件：
    - 至少存在一个状态正常的CDP进程。
    - SPU硬盘没有满。
    - 与CG通讯正常。
    - 当[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)中配置的生成话单类型为“YES(Generate)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDRTYPE | 话单类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要生成的话单类型。<br>数据来源：整网规划<br>取值范围：<br>- “MCDR(MCDR)”<br>- “SCDR(SCDR)”<br>- “SSMOCDR(SSMOCDR)”<br>- “SSMTCDR(SSMTCDR)”<br>- “LCSMOCDR(LCSMOCDR)”<br>- “LCSMTCDR(LCSMTCDR)”<br>- “LCSNICDR(LCSNICDR)”<br>默认值：无<br>说明：“系统类型”<br>为<br>“GPRS”<br>时，不能生成LCSMOCDR模拟话单。 |
| SYSTYPE | 系统类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要生成话单的系统类型。<br>数据来源：整网规划<br>取值范围：<br>- “GPRS(GPRS)”<br>- “UMTS(UMTS)”<br>- “GERAN(GERAN)”<br>默认值：<br>“UMTS” |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定模拟话单中包含的IMSI。<br>数据来源：整网规划<br>取值范围：5～15位十进制数字<br>默认值：无 |
| MSISDN | MSISDN | 可选必选说明：可选参数<br>参数含义：该参数用于指定模拟话单中包含的MSISDN。<br>数据来源：整网规划<br>取值范围：5～15位十进制数字<br>默认值：无 |
| CC | 计费属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定模拟话单的计费属性字段。<br>数据来源：整网规划<br>取值范围：<br>- “NORMAL(普通计费)”<br>- “PREPAID(预付费)”<br>- “FLATRATE(包月制)”<br>- “HOTBILLING(实时计费)”<br>默认值：<br>“NORMAL(普通计费)” |
| LAC | 位置区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定模拟话单的位置区信息。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则： 该参数的值必须大于等于“位置区域码”的值。 新添加的位置区域码范围不能与原有的位置区域码范围出现重叠。 如果该参数不输入，表示配置单个LAC。<br>说明：- 用户在输入值的时候，可以加上“0x”前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| RAC | 寻呼范围路由区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定模拟话单的路由区信息。<br>数据来源：整网规划<br>取值范围：1～2位十六进制数<br>默认值：无 |
| CI | 小区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定模拟话单的小区标识信息。<br>数据来源：整网规划<br>取值范围：1～4位十六进制数<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询的资源单元名称。该参数可以通过<br>[DSP RU](../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划<br>取值范围：1 ~ 63位字符串<br>默认值：无 |
| PID | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要模拟生成话单的SPP/UPP进程号。S-CDR话单只能由UPP进程生成。LCS-NI-CDR、LCS-MT-CDR、LCS-MO-CDR、S-SMT-CDR、S-SMO-CDR、M-CDR话单只能由SPP进程生成。<br>数据来源：整网规划<br>取值范围：0～20<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGCDR]] · 强制生成用户话单（CHGCDR）

## 使用实例

模拟生成一张M-CDR话单：

TST CHGCDR: CDRTYPE=MCDR;

## 证据

- 原始手册：`evidence/UNC/20.15.2/TST-CHGCDR.md`
