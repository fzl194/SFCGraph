---
id: UNC@20.15.2@MMLCommand@SET NRFMATCHRULE
type: MMLCommand
name: SET NRFMATCHRULE（设置服务发现最长匹配处理规则）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFMATCHRULE
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF服务发现最长匹配规则
status: active
---

# SET NRFMATCHRULE（设置服务发现最长匹配处理规则）

## 功能

**适用NF：NRF**

该命令用于设置服务发现时是否开启最长匹配规则。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NFTYPE | MATCHSW |
| --- | --- |
| AMF | FUNC_OFF |
| SMF | FUNC_OFF |
| BSF | FUNC_OFF |
| UDR | FUNC_OFF |
| UDM | FUNC_OFF |
| AUSF | FUNC_OFF |
| PCF | FUNC_OFF |
| CHF | FUNC_OFF |
| CUSTOM_OCS | FUNC_OFF |
| SMSF | FUNC_OFF |
| NWDAF | FUNC_OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NRF服务发现的目标网元类型。<br>数据来源：本端规划<br>取值范围：<br>- AMF（AMF）<br>- SMF（SMF ）<br>- BSF（BSF）<br>- UDR（UDR）<br>- UDM（UDM）<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SMSF（SMSF）<br>- NWDAF（NWDAF）<br>默认值：无。<br>配置原则：无 |
| MATCHSW | 匹配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF服务发现时是否开启最长匹配功能。<br>开关设置为“FUNC_ON”时， 对于AMF/SMF/NWDAF而言，表示使用TAI匹配目标NF TAIRANGE，如果匹配出多个NF，选择最长匹配（匹配到的区间最小）的NF返回；<br>对于BSF而言，表示使用UeIpv4Address/UeIpv6Prefix匹配目标BSF Ipv4AddressRanges/Ipv6PrefixRanges，如果匹配出多个BSF，选择最长匹配（匹配到的区间最小）的BSF返回；<br>对于UDR/UDM/AUSF/PCF/CHF/CUSTOM_OCS/SMSF而言，表示NRF在号段匹配时会选择与请求方NF携带的号段匹配度最高的NF返回（即选择号段匹配最长的NF返回，号段可以匹配但非最长号段匹配的NF被认为不满足号段发现条件）；<br>开关设置为“FUNC_OFF”时，会返回所有匹配上的NF。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFMATCHRULE查询当前参数配置值。<br>配置原则：<br>当AMF的最长匹配功能开关打开时，不允许将AMF的“TAI上报策略”配置为TAIRANGELIST和TAIRANGELISTFIRST。否则同一AMF Pool内TAI Range最小的AMF总是会被优先选择，可能导致用户分布不均。<br>AMF的“TAI上报策略”开关通过LST AMFPROFILEPLCY命令查询TAIPPTPLCY参数来获取。需要结合实际业务情况，决策AMF的“TAI精细化选择开关”和“TAI上报策略”的配置选择。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFMATCHRULE]] · 服务发现最长匹配处理规则（NRFMATCHRULE）

## 使用实例

NRF服务发现时,设置SMF网元开启最长匹配功能开关为开。

```
SET NRFMATCHRULE: NFTYPE=SMF, MATCHSW=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置服务发现最长匹配处理规则（SET-NRFMATCHRULE）_88248960.md`
