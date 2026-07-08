---
id: UNC@20.15.2@MMLCommand@SET REDCAPRATVALUE
type: MMLCommand
name: SET REDCAPRATVALUE（设置RedCap终端接入RAT填写值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: REDCAPRATVALUE
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- RedCap用户RAT值
status: active
---

# SET REDCAPRATVALUE（设置RedCap终端接入RAT填写值）

## 功能

**适用NF：SMF**

该命令用于设置RedCap终端接入时UNC给周边网元UPF，PCF，CHF，N16SMF，N16aSMF，AAAACCT，AAAAUTH发送消息时RatType信元中填写的值。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CHF | PCF | UPF | AAAACCT | AAAAUTH | N16SMF | N16ASMF |
| --- | --- | --- | --- | --- | --- | --- |
| NR_REDCAP | NR_REDCAP | NR_REDCAP | NR_REDCAP | NR_REDCAP | NR_REDCAP | NR_REDCAP |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHF | 和CHF交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置和CHF交互使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- NR（NR）<br>- NR_REDCAP（NR_REDCAP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST REDCAPRATVALUE查询当前参数配置值。<br>配置原则：无 |
| PCF | 和PCF交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置和PCF交互使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- NR（NR）<br>- NR_REDCAP（NR_REDCAP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST REDCAPRATVALUE查询当前参数配置值。<br>配置原则：无 |
| UPF | 和UPF交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置和UPF交互使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- NR（NR）<br>- NR_REDCAP（NR_REDCAP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST REDCAPRATVALUE查询当前参数配置值。<br>配置原则：无 |
| AAAACCT | 和AAA计费交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置和ACCT交互使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- NR（NR）<br>- NR_REDCAP（NR_REDCAP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST REDCAPRATVALUE查询当前参数配置值。<br>配置原则：无 |
| AAAAUTH | 和AAA鉴权交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置和AUTH交互使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- NR（NR）<br>- NR_REDCAP（NR_REDCAP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST REDCAPRATVALUE查询当前参数配置值。<br>配置原则：无 |
| N16SMF | 和N16SMF交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置和N16SMF交互使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- NR（NR）<br>- NR_REDCAP（NR_REDCAP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST REDCAPRATVALUE查询当前参数配置值。<br>配置原则：无 |
| N16ASMF | 和N16aSMF交互使用的RAT值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置和N16aSMF交互使用的RAT值。<br>数据来源：对端协商<br>取值范围：<br>- NR（NR）<br>- NR_REDCAP（NR_REDCAP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST REDCAPRATVALUE查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/REDCAPRATVALUE]] · RedCap接入用户的RAT填写值（REDCAPRATVALUE）

## 使用实例

指定RedCap终端接入与UPF交互时Rat值为NR，与CHF交互时Rat值为NR，与PCF交互时Rat值为NR，与AAAACCT交互时Rat值为NR，与AAAAUTH交互时Rat值为NR，与N16SMF交互时Rat值为NR，与N16aSMF交互时Rat值为NR：

```
SET REDCAPRATVALUE: CHF=NR, PCF=NR, UPF=NR, AAAACCT=NR, AAAAUTH=NR, N16SMF=NR, N16ASMF=NR;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-REDCAPRATVALUE.md`
