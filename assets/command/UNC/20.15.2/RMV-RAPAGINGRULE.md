---
id: UNC@20.15.2@MMLCommand@RMV RAPAGINGRULE
type: MMLCommand
name: RMV RAPAGINGRULE（删除基于路由区的寻呼参数设置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV RAPAGINGRULE（删除基于路由区的寻呼参数设置）

## 功能

**适用网元：SGSN**

该命令用于删除特定路由区对应的寻呼策略配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，该路由区的寻呼策略使用系统默认的GMM配置（[**SET GMM**](../MM协议参数管理/Gb模式MM协议参数/设置Gb模式MM协议参数(SET GMM)_72345121.md)）和PMM配置（[**SET PMM**](../MM协议参数管理/Iu模式MM协议参数/设置Iu模式MM协议参数(SET PMM)_26305336.md)）设定。
- 该命令中的WKDAY、STARTTIME、ENDTIME为可选参数，允许的组合：
    - 只输入WKDAY，将该RAI(MCC+MNC+LAC+RAC)下的指定WKDAY的记录都删除；
    - 同时输入WKDAY、STARTTIME、ENDTIME，将该RAI(MCC+MNC+LAC+RAC)下的指定WKDAY、STARTTIME、ENDTIME的记录删除（会精确匹配到单条记录）；
    - 不输入WKDAY、STARTTIME、ENDTIME，将删除该RAI(MCC+MNC+LAC+RAC)的所有记录。其他参数组合不支持。
- 如果启用特殊寻呼参数的区域与系统不在同一时区，则需要先将该区域时间转换成系统本地时间后再执行删除。

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
| WKDAY | 星期序号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定寻呼策略生效的一星期中的某一天。<br>数据来源：整网规划<br>取值范围：<br>- “MON(星期一)”<br>- “TUES(星期二)”<br>- “WED(星期三)”<br>- “THURS(星期四)”<br>- “FRI(星期五)”<br>- “SAT(星期六)”<br>- “SUN(星期日)”<br>默认值：无 |
| STARTTIME | 起始时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定寻呼策略生效的起始时间。<br>数据来源：整网规划<br>取值范围：00&00～23&59<br>默认值：无 |
| ENDTIME | 终止时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定寻呼策略生效的终止时间。<br>数据来源：整网规划<br>取值范围：00&00～23&59<br>默认值：无 |

## 操作的配置对象

- [基于路由区的寻呼参数设置（RAPAGINGRULE）](configobject/UNC/20.15.2/RAPAGINGRULE.md)

## 使用实例

删除 “移动国家代码” 为 “123” ， “移动网号” 为 “03” ， “位置区域码” 为 “0x113” ， “路由区域码” 为 “0x3E” 的路由区配置：

RMV RAPAGINGRULE: MCC="123", MNC="03", LAC="0x113", RAC="0x3E";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除基于路由区的寻呼参数设置(RMV-RAPAGINGRULE)_72225209.md`
