---
id: UNC@20.15.2@MMLCommand@ADD SHAREPLMNMEM
type: MMLCommand
name: ADD SHAREPLMNMEM（增加共享PLMN群组成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SHAREPLMNMEM
command_category: 配置类
applicable_nf:
- MME
effect_mode: 延迟生效
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 基于区域MME共享管理
- 共享PLMN群组成员
status: active
---

# ADD SHAREPLMNMEM（增加共享PLMN群组成员）

## 功能

**适用网元：MME**

在 **[MOCN](../../../../../../../../../网络部署/特性部署/UNC特性指南/网络共享功能/WSFD-207003 基于LTE的网络共享（MOCN）_68260814.md)** 组网下的两网融合项目中，基于区域逐步融合，需要配置基于特定区域PLMN的使用策略。该命令用于增加共享PLMN群组成员。

## 注意事项

- 此命令最大记录数为128。
- 此命令执行后60秒内生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMNGPID | PLMN群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PLMN群组标识。<br>数据来源：本端规划<br>取值范围：1～31<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定由ITU-T统一分配的移动网络所在国家的标识符。<br>数据来源：整网规划<br>取值范围：3位十进制数<br>默认值：无<br>说明：ADD SHAREPLMNMEM中的MCC + MNC来源于ADD MMESHAREPLMN中的MCC + MNC。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个国家内的PLMN标识符。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数<br>默认值：无<br>说明：ADD SHAREPLMNMEM中的MCC + MNC来源于ADD MMESHAREPLMN中的MCC + MNC。 |

## 操作的配置对象

- [共享PLMN群组成员（SHAREPLMNMEM）](configobject/UNC/20.15.2/SHAREPLMNMEM.md)

## 使用实例

增加一条： “PLMN群组标识” 为 “1” ， “移动国家码” 为 “460” ， “移动网号” 为 “05” 的记录。

ADD SHAREPLMNMEM: PLMNGPID=1, MCC="460", MNC="05";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加共享PLMN群组成员(ADD-SHAREPLMNMEM)_19405129.md`
