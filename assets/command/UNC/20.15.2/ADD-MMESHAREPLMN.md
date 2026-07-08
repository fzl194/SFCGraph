---
id: UNC@20.15.2@MMLCommand@ADD MMESHAREPLMN
type: MMLCommand
name: ADD MMESHAREPLMN（增加MME的共享PLMN）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MMESHAREPLMN
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 31
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME POOL区管理
- MME共享管理
status: active
---

# ADD MMESHAREPLMN（增加MME的共享PLMN）

## 功能

**适用网元：MME**

此命令用于增加一条共享MME的PLMN记录。主要用于 UNC 作为MME被多个拥有独立PLMN ID的运营商共享的场景。

## 注意事项

- 此命令最大记录数为31。
- 此命令执行后立即生效。
- 只有[**ADD MMEID**](../MMEID管理/增加MMEID配置(ADD MMEID)_26146088.md)命令中配置了MCC/MNC时，用户才可以配置MME的共享PLMN，并且MME的共享PLMN的MCC/MNC不能与[**ADD MMEID**](../MMEID管理/增加MMEID配置(ADD MMEID)_26146088.md)命令中配置的MCC/MNC相同。
- ADD MMESHAREPLMN配置的共享PLMN记录不能重复。
- 当未购买“基于LTE的网络共享(GWCN)”License时，执行本命令后，如果现网中存在一个eNodeB支持多个PLMN的场景，该类eNodeB链路中断后重新建立，上层业务可能无法正常使用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定由ITU-T统一分配的移动网络所在国家的标识符。<br>数据来源：整网规划<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个国家内的PLMN标识符。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMESHAREPLMN]] · MME的共享PLMN（MMESHAREPLMN）

## 使用实例

增加一个 “移动国家码” 为 “123” 、 “移动网号” 为 “01” 的MME的共享PLMN：

ADD MMESHAREPLMN: MCC="123", MNC="01";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-MMESHAREPLMN.md`
