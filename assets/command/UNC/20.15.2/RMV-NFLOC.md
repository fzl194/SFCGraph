---
id: UNC@20.15.2@MMLCommand@RMV NFLOC
type: MMLCommand
name: RMV NFLOC（删除目标NF发现和选择的位置匹配信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NFLOC
command_category: 配置类
applicable_nf:
- AMF
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF优选区域管理
status: active
---

# RMV NFLOC（删除目标NF发现和选择的位置匹配信息）

## 功能

![](删除目标NF发现和选择的位置匹配信息（RMV NFLOC）_09653223.assets/notice_3.0-zh-cn_2.png)

执行该命令，如果参数设置不合理，可能影响AMF优选本DC SMF。

**适用NF：AMF、SMF**

该命令用于删除为目标NF的发现和选择配置的位置匹配相关的信息。

位置类型为LOCALITY时，执行该命令基于目标网元位置的精确选择功能将失效。

位置类型为Preferred-Locality时，执行该命令基于目标网元位置的优先选择功能将失效。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示服务发现的目标NF的请求者的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- “NfAMF（NfAMF）”：AMF<br>- “NfSMF（NfSMF）”：SMF<br>默认值：无<br>配置原则：无 |
| TGTNFTYPE | 目标NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示目标NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “NF_ALL（所有NF）”：所有NF<br>- “UDM（UDM）”：UDM<br>- “AMF（AMF）”：AMF<br>- “SMF（SMF）”：SMF<br>- “AUSF（AUSF）”：AUSF<br>- “PCF（PCF）”：PCF<br>- “SMSF（SMSF）”：SMSF<br>- “NSSF（NSSF）”：NSSF<br>- “LMF（LMF）”：LMF<br>- “GMLC（GMLC）”：GMLC<br>- “FIFTHG_EIR（5G_EIR）”：5G_EIR<br>默认值：无<br>配置原则：无 |
| LOCTYPE | 位置类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示目标NF发现和选择流程中用作匹配条件的位置类型。<br>数据来源：全网规划<br>取值范围：<br>- “LOCALITY（位置）”：将位置信息作为仅次于目标NF优先级的策略选择目标NF。<br>- “PREFERRED_LOCALITY（优选位置）”：将位置信息作为最高优先级选择目标NF。<br>默认值：无<br>配置原则：<br>在基于位置的NF发现和选择过程中，如果运营商期望以目标NF的位置信息作为第一优选条件，则使用PREFERRED_LOCALITY类型；如果期望以目标NF的优先级作为第一优选条件，位置信息次之，则使用LOCALITY类型。如果运营商期望用点分格式，应使用LOCALITY类型。LOCALITY的点分格式为“大区标识.数据中心标识.资源池标识”。<br>LOCALITY和PREFERRED_LOCALITY两种目标NF的位置匹配条件都依赖于目标NF配置了位置信息，并注册给了NRF。两者的区别在于：<br>- 执行位置匹配的地点不同。LOCALITY是在请求者NF从NRF获取目标NF列表后执行的，而PREFERRED_LOCALITY是在NRF上执行的。说明：基于PREFERRED_LOCALITY选择时，NRF可能仅返回与优选位置匹配的目标NF列表，也可能返回非优选位置匹配的目标NF。华为的NRF支持开关控制（在NRF上通过SET NRFFUNCSW命令中“DISCLOCPREFERSW”和“DISCLOCMATEHSW”控制）。为了防止NRF返回非PREFERRED_LOCALITY匹配的目标NF列表，UNC支持从NRF获取目标NF列表后，本地再按照优选区域匹配目标NF列表。<br>- 执行位置匹配的优先级不同。LOCALITY是首先使用优先级筛选后再根据位置进行匹配；而PREFERRED_LOCALITY是首先根据优选位置匹配，随后再针对匹配优选位置的目标NF根据优先级、权重进行选择。<br>- 执行位置匹配的算法不同。LOCALITY支持点分格式的字符串，支持指定长度的匹配；而PREFERRED_LOCALITY目标仅支持全字段匹配。<br>- 执行位置匹配的依赖条件不同。LOCALITY需要在UNC上打开匹配开关（详见SET NFDISCPLCY的LOCSELECT参数）；而PREFERRED_LOCALITY与NRF上的优选位置功能有关。 |

## 操作的配置对象

- [目标NF发现和选择的位置匹配信息（NFLOC）](configobject/UNC/20.15.2/NFLOC.md)

## 使用实例

当UE新建PDU Session时，不需要优选指定区域内的SMF，执行如下命令：

```
RMV NFLOC: NFTYPE=NfAMF, TGTNFTYPE=SMF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除目标NF发现和选择的位置匹配信息（RMV-NFLOC）_09653223.md`
