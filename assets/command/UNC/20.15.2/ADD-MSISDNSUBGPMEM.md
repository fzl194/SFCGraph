---
id: UNC@20.15.2@MMLCommand@ADD MSISDNSUBGPMEM
type: MMLCommand
name: ADD MSISDNSUBGPMEM（增加MSISDN用户群成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MSISDNSUBGPMEM
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 20000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- MSISDN用户群成员管理
status: active
---

# ADD MSISDNSUBGPMEM（增加MSISDN用户群成员）

## 功能

**适用网元：SGSN、MME**

此命令用于增加MSISDN用户群成员记录。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为20000。
- 此命令配置的 “用户群标识” 参数值不能在 [**ADD SUBGPMEM**](../用户群成员管理/增加用户群成员(ADD SUBGPMEM)_26305374.md) 配置中使用。
- 此命令配置的 “用户群标识” 参数值不能在 [**ADD PEERPLMN**](../../../网络管理/对等PLMN管理/增加对等PLMN配置(ADD PEERPLMN)_26305906.md) 配置中使用。
- 此命令配置的 “用户群标识” 参数值如果在 [**ADD S1ACCAREALST**](../S1模式区域漫游限制参数/增加S1模式接入控制配置（ADD S1ACCAREALST）_72345153.md) 或 [**MOD S1ACCAREALST**](../S1模式区域漫游限制参数/修改S1模式接入控制配置（MOD S1ACCAREALST）_26145556.md) 配置中使用， “SPECSUB（拒绝特征用户接入）” 只能配置为 “NO(否)” ，且 “ENBIND（指示特征RFSP索引）” 只能配置为 “NO(不指示)” 。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBID | 用户群标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户群标识。<br>数据来源：本端规划<br>取值范围：1～100。<br>默认值：无<br>配置原则：<br>- 配置的参数值必须在[**ADD SUBGP**](../用户群管理/增加用户群(ADD SUBGP)_72225241.md)中已经配置。<br>- 配置的参数值不能在[**ADD SUBGPMEM**](../用户群成员管理/增加用户群成员(ADD SUBGPMEM)_26305374.md)或[**ADD PEERPLMN**](../../../网络管理/对等PLMN管理/增加对等PLMN配置(ADD PEERPLMN)_26305906.md)配置中使用。<br>- 如果系统中存在包含了该SUBID，且参数“SPECSUB（拒绝特征用户接入）”不为“NO(否)”，或“ENBIND（指示特征RFSP索引）”不为“NO(不指示)”的[**ADD S1ACCAREALST**](../S1模式区域漫游限制参数/增加S1模式接入控制配置（ADD S1ACCAREALST）_72345153.md)记录，则该SUBID不能在本命令中使用。 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MSISDN前缀。<br>数据来源：本端规划<br>取值范围：1～15位十进制数字。<br>默认值：无 |

## 操作的配置对象

- [MSISDN用户群成员（MSISDNSUBGPMEM）](configobject/UNC/20.15.2/MSISDNSUBGPMEM.md)

## 使用实例

增加一条MSISDN用户群成员记录，用户群标识为30，MSISDN前缀为12345：

ADD MSISDNSUBGPMEM: SUBID=30, MSISDNPRE="12345";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加MSISDN用户群成员(ADD-MSISDNSUBGPMEM)_72345167.md`
