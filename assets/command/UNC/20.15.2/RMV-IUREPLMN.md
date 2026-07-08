---
id: UNC@20.15.2@MMLCommand@RMV IUREPLMN
type: MMLCommand
name: RMV IUREPLMN（删除3G重定向PLMN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IUREPLMN
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 基于区域SGSN共享管理
- 3G重定向PLMN
status: active
---

# RMV IUREPLMN（删除3G重定向PLMN）

## 功能

**适用网元：SGSN**

该命令用于删除3G重定向PLMN。

## 注意事项

- 此命令在下一次业务流程时生效。
- 此命令不对移动虚拟网络运营商生效

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HPLMN的移动国家号码。<br>数据来源：整网规划<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HPLMN的移动网号码。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IUREPLMN]] · 3G重定向PLMN（IUREPLMN）

## 使用实例

删除一条： “移动国家码” 为 “460” ， “移动网号” 为 “05” ，的记录。

RMV IUREPLMN: MCC="460", MNC="05";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除3G重定向PLMN(RMV-IUREPLMN)_19455573.md`
