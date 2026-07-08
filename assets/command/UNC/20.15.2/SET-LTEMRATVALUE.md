---
id: UNC@20.15.2@MMLCommand@SET LTEMRATVALUE
type: MMLCommand
name: SET LTEMRATVALUE（设置LTE-M用户的RAT值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: LTEMRATVALUE
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- LTE-M用户RAT值
status: active
---

# SET LTEMRATVALUE（设置LTE-M用户的RAT值）

## 功能

**适用NF：PGW-C、SGW-C、SMF**

该命令用于设置终端通过LTE-M接入方式时UNC给周边网元发送消息时RAT信元中携带的值。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| OCS | CHF | CG | AAAACCT | AAAAUTH | PCRF | PCF | PGW | UPF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTE_M | LTE_M | LTE_M | LTE_M | LTE_M | LTE_M | LTE_M | LTE_M | LTE_M |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCS | 和OCS交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC和OCS交互时使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- EUTRAN（EUTRAN）<br>- LTE_M（LTE_M）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEMRATVALUE查询当前参数配置值。<br>配置原则：无 |
| CHF | 和CHF交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC和CHF交互时使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- EUTRAN（EUTRAN）<br>- LTE_M（LTE_M）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEMRATVALUE查询当前参数配置值。<br>配置原则：无 |
| CG | 和CG交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC和CG交互时使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- EUTRAN（EUTRAN）<br>- LTE_M（LTE_M）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEMRATVALUE查询当前参数配置值。<br>配置原则：无 |
| AAAACCT | 和AAA计费服务器交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC和AAA计费服务器交互时使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- EUTRAN（EUTRAN）<br>- LTE_M（LTE_M）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEMRATVALUE查询当前参数配置值。<br>配置原则：无 |
| AAAAUTH | 和AAA鉴权服务器交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC作为PGW-C和AAA鉴权服务器交互时使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- EUTRAN（EUTRAN）<br>- LTE_M（LTE_M）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEMRATVALUE查询当前参数配置值。<br>配置原则：无 |
| PCRF | 和PCRF交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC作为PGW-C和PCRF交互时使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- EUTRAN（EUTRAN）<br>- LTE_M（LTE_M）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEMRATVALUE查询当前参数配置值。<br>配置原则：无 |
| PCF | 和PCF交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC和PCF交互时使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- EUTRAN（EUTRAN）<br>- LTE_M（LTE_M）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEMRATVALUE查询当前参数配置值。<br>配置原则：无 |
| PGW | UNC作为SGW-C发送给PGW-C时使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC作为SGW-C和PGW-C交互时使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- EUTRAN（EUTRAN）<br>- LTE_M（LTE_M）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEMRATVALUE查询当前参数配置值。<br>配置原则：无 |
| UPF | 和UPF交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC和UPF交互时使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- EUTRAN（EUTRAN）<br>- LTE_M（LTE_M）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LTEMRATVALUE查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LTEMRATVALUE]] · LTE-M用户的RAT值（LTEMRATVALUE）

## 使用实例

设置终端通过LTE-M接入方式时，UNC给周边网元发送的消息中RAT信元携带的值：

```
SET LTEMRATVALUE: OCS=LTE_M, CHF=LTE_M, CG=LTE_M, AAAACCT=LTE_M, AAAAUTH=LTE_M, PCRF=LTE_M, PCF=LTE_M, PGW=LTE_M, UPF=LTE_M;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-LTEMRATVALUE.md`
