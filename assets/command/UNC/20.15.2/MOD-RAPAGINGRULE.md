---
id: UNC@20.15.2@MMLCommand@MOD RAPAGINGRULE
type: MMLCommand
name: MOD RAPAGINGRULE（修改基于路由区的寻呼参数设置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: RAPAGINGRULE
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 基于路由区的寻呼参数设置
status: active
---

# MOD RAPAGINGRULE（修改基于路由区的寻呼参数设置）

## 功能

**适用网元：SGSN**

本命令用于修改基于路由区的2/3G寻呼参数。

## 注意事项

- 对某些路由区存在大量终端用户的情况下，针对这些路由区执行本命令设置较小的“N3313”和“T3313”，可以降低大量的寻呼对无线侧设备造成的压力。
- 该命令执行后立即生效。
- 如果启用特殊寻呼参数的区域与系统不在同一时区，则需要先将该区域时间转换成系统本地时间后再修改。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家代码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：整网规划<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区域码。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| RAC | 路由区域码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由区域码。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无 |
| WKDAY | 星期序号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定寻呼策略生效的一星期中的某一天。<br>数据来源：整网规划<br>取值范围：<br>- “MON(星期一)”<br>- “TUES(星期二)”<br>- “WED(星期三)”<br>- “THURS(星期四)”<br>- “FRI(星期五)”<br>- “SAT(星期六)”<br>- “SUN(星期日)”<br>默认值：无 |
| STARTTIME | 起始时间 | 可选必选说明：必选参数<br>参数含义：该参数用于指定寻呼策略生效的起始时间。<br>数据来源：整网规划<br>取值范围：00&00～23&59<br>默认值：无 |
| ENDTIME | 终止时间 | 可选必选说明：必选参数<br>参数含义：该参数用于指定寻呼策略生效的终止时间。<br>数据来源：整网规划<br>取值范围：00&00～23&59<br>默认值：无 |
| T3313 | T3313（s） | 可选必选说明：可选参数<br>参数含义：此定时器用于控制SGSN发起寻呼与MS响应的时间间隔。<br>数据来源：整网规划<br>取值范围：4～20<br>默认值：无<br>说明：- 对于3G，在SGSN发送PAGING REQUEST消息后启动，在收到SERVICE REQUEST(PAGING RESPONSE)消息后停止，超时后，SGSN重发PAGING REQUEST消息；对于2G，在SGSN发送PAGING REQUEST消息后启动，在收到MS的任意的LLC消息(非NULL FRAME)后停止，超时后，SGSN重发PAGING REQUEST消息。 |
| N3313 | N3313（times） | 可选必选说明：可选参数<br>参数含义：该参数用于指定在寻呼流程中，没有收到MS的响应消息，SGSN重复发送PAGING REQUEST消息的次数。<br>数据来源：整网规划<br>取值范围：0～5<br>默认值：无<br>说明：- 若将N3313调整为低于[**SET GMM**](../MM协议参数管理/Gb模式MM协议参数/设置Gb模式MM协议参数(SET GMM)_72345121.md)和[**SET PMM**](../MM协议参数管理/Iu模式MM协议参数/设置Iu模式MM协议参数(SET PMM)_26305336.md)原配置值，可能会导致这些路由区内的寻呼成功率降低。 |
| PAGINGDELTA | 重寻呼间隔递增值（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定在寻呼流程中，没有收到MS的响应消息，SGSN重复发送PAGING REQUEST消息的间隔递增时间值。<br>数据来源：整网规划<br>取值范围：0～20<br>默认值：无 |
| RADESC | 描述 | 可选必选说明：可选参数<br>参数含义：本参数指定本路由区的简要描述，用于帮助解释本记录指定的物理位置。<br>数据来源：整网规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [基于路由区的寻呼参数设置（RAPAGINGRULE）](configobject/UNC/20.15.2/RAPAGINGRULE.md)

## 使用实例

“移动国家代码” 为 “123” ， “移动网号” 为 “03” ， “位置区域码” 为 “0x113” ， “路由区域码” 为 “0x3E” 的路由区， “星期序号” 为 “SAT(星期六)” ， “起始时间” 为 “18&00” ， “终止时间” 为 “20&00” ，寻呼策略参数修改为 “T3313(s)” 为 “6” 、 “N3313(times)” 为 “2” 、 “重寻呼间隔递增值(s)” 为 “0” ， “描述” 为 “stadium” ：

MOD RAPAGINGRULE: MCC="123", MNC="03", LAC="0x113", RAC="0x3E", WKDAY=SAT, STARTTIME=18&00, ENDTIME=20&00, T3313=6, N3313=2, PAGINGDELTA=0, RADESC="stadium";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于路由区的寻呼参数设置(MOD-RAPAGINGRULE)_26305340.md`
