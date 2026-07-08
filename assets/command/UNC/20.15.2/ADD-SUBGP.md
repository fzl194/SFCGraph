---
id: UNC@20.15.2@MMLCommand@ADD SUBGP
type: MMLCommand
name: ADD SUBGP（增加用户群）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SUBGP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- 用户群管理
status: active
---

# ADD SUBGP（增加用户群）

## 功能

**适用网元：SGSN、MME**

此命令用于增加用户群记录，同一个用户群中的用户具有相同的接入控制策略。

当将需要采用相同接入控制策略的不同的IMSI号段或MSISDN号段用户进行划分，作为一个用户群统一进行控制时，需要执行此命令。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为100。
- 如果已经存在[**ADD SUBGP**](增加用户群(ADD SUBGP)_72225241.md)的接入限制策略，如果新配置的[**ADD SUBGP**](增加用户群(ADD SUBGP)_72225241.md)和原有的[**ADD SUBGP**](增加用户群(ADD SUBGP)_72225241.md)关联的[**ADD SUBGPMEM**](../用户群成员管理/增加用户群成员(ADD SUBGPMEM)_26305374.md)中IMSI号段前缀相同但长度不同，则可能导致关联的[**ADD S1ACCAREALST**](../S1模式区域漫游限制参数/增加S1模式接入控制配置（ADD S1ACCAREALST）_72345153.md)接入限制策略变更，导致用户无法接入。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBID | 用户群标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户群标识。<br>数据来源：整网规划<br>取值范围：1～100<br>默认值：无 |
| SUBN | 用户群名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户群名称。<br>数据来源：整网规划<br>取值范围：1～32位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SUBGP]] · 用户群（SUBGP）

## 使用实例

增加一条用户群管理记录，用户群标识为30：

ADD SUBGP: SUBID=30;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SUBGP.md`
