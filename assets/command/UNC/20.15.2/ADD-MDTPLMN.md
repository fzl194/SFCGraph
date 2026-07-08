---
id: UNC@20.15.2@MMLCommand@ADD MDTPLMN
type: MMLCommand
name: ADD MDTPLMN（增加基于管理的最小化路测的PLMN）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MDTPLMN
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
- MDT管理
status: active
---

# ADD MDTPLMN（增加基于管理的最小化路测的PLMN）

## 功能

**适用网元：MME**

该命令用于增加基于管理的最小化路测（MDT）的PLMN。MME通过本地配置和是否签约MDT授权，决策在HANDOVER REQUEST和INITIAL CONTEXT SETUP REQUEST消息中是否携带Management Based MDT PLMN List信元给eNodeB。

该命令的使用场景：该命令主要应用于小区无线质量的测量，旨在针对特定范围内（如Cell ID、TA等）的UE进行MDT的数据采集和分析。

## 注意事项

- 该命令执行后立即生效。

- 配置记录添加后，如果当前用户正在进行业务流程，配置限制不会实时生效，在下一个流程中生效。

- 最多可输入16条记录。
- 若MCC相同，MNC有效长度为2位和MNC有效长度为3位的记录，前两位不允许相同。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数表示组成Serving PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>- 此参数需要先在[**ADD MMEID**](../../网络管理/MME POOL区管理/MMEID管理/增加MMEID配置(ADD MMEID)_26146088.md)或[**ADD MMESHAREPLMN**](../../网络管理/MME POOL区管理/MME共享管理/增加MME的共享PLMN(ADD MMESHAREPLMN)_26146086.md)中先配置好。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数表示组成Serving PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>- 此参数需要先在[**ADD MMEID**](../../网络管理/MME POOL区管理/MMEID管理/增加MMEID配置(ADD MMEID)_26146088.md)或[**ADD MMESHAREPLMN**](../../网络管理/MME POOL区管理/MME共享管理/增加MME的共享PLMN(ADD MMESHAREPLMN)_26146086.md)中先配置好。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数是对MDT PLMN的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MDTPLMN]] · 基于管理的最小化路测的PLMN（MDTPLMN）

## 使用实例

增加一条移动国家码为123、移动网号为030、描述为“visit”的MDT PLMN配置：

ADD MDTPLMN: MCC="123", MNC="030", DESC="visit";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加基于管理的最小化路测的PLMN(ADD-MDTPLMN)_63155530.md`
