---
id: UNC@20.15.2@MMLCommand@ADD SPCTLLI
type: MMLCommand
name: ADD SPCTLLI（增加特殊随机TLLI配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SPCTLLI
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 特殊TLLI配置
status: active
---

# ADD SPCTLLI（增加特殊随机TLLI配置）

## 功能

**适用网元：SGSN**

如果现网很多手机使用固定的RANDOM TLLI附着会导致附着因TLLI冲突而失败。该命令用于对增加一项特殊RANDOM TLLI的记录，对该RANDOM TLLI的IMSI附着串行接入。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数128。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TLLI | TLLI | 可选必选说明：必选参数<br>参数含义：该参数用于指定RANDOM TLLI，系统将串行接入该参数指定的RANDOM TLLI附着。<br>数据来源：网上问题<br>取值范围： 0x00000000～0xffffffff(十六进制)<br>默认值：无 |
| MSINFO | 手机信息 | 可选必选说明：可选参数<br>参数含义：描述使用该RANDOM TLLI的用户信息。<br>数据来源：整网规划<br>取值范围： 0～63个字符<br>默认值 ： none |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SPCTLLI]] · 特殊随机TLLI配置（SPCTLLI）

## 使用实例

增加一条RANDOM TLLI为71234abc的记录：

**ADD SPCTLLI: TLLI="0x71234abc";或者 ADD SPCTLLI: TLLI="71234abc";**

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SPCTLLI.md`
