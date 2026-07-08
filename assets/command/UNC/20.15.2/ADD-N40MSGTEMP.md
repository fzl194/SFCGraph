---
id: UNC@20.15.2@MMLCommand@ADD N40MSGTEMP
type: MMLCommand
name: ADD N40MSGTEMP（增加N40消息属性模板）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: N40MSGTEMP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- N40消息属性模板
status: active
---

# ADD N40MSGTEMP（增加N40消息属性模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用于增加N40消息属性模板，用于控制N40消息中是否携带对应字段。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入101条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TEMPLATENAME | SECRATUSAGE | NBEXTENDATTR | QFIDOWNLINK | HOMECHGID | HWQBCIDCT | APPSVCPROVID | RCP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| global | ENABLE | ENABLE | ENABLE | ENABLE | DISABLE | DISABLE | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TEMPLATENAME | N40消息属性模板名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定N40消息字段模板名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| SECRATUSAGE | RANSecondaryRATUsageReport | 可选必选说明：可选参数<br>参数含义：N40消息中是否携带RANSecondaryRATUsageReport。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE（携带该字段）<br>- DISABLE（不携带该字段）<br>默认值：ENABLE<br>配置原则：<br>该参数配置为DISABLE时，ADD CCT中SECRUTHRESHOLD功能不生效。 |
| NBEXTENDATTR | NB扩展属性 | 可选必选说明：可选参数<br>参数含义：控制NB-IOT、LTEM接入时N40消息是否携带扩展属性信息，包括APN Rate Control、Serving PLMN Rate Control、CP only indication和PtP隧道。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE（携带该字段）<br>- DISABLE（不携带该字段）<br>默认值：ENABLE<br>配置原则：<br>仅在SET N40APIVER的FEATURE使能NBIOTCHG或LTEMCHG时生效。 |
| QFIDOWNLINK | QFI容器中的DownLinkVolume | 可选必选说明：可选参数<br>参数含义：N40消息中MultipleQFIcontainer信元是否携带DownLinkVolume。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE（携带该字段）<br>- DISABLE（不携带该字段）<br>默认值：ENABLE<br>配置原则：无 |
| HOMECHGID | HomeProvidedChargingID | 可选必选说明：可选参数<br>参数含义：N40消息中是否携带HomeProvidedChargingID。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE（携带该字段）<br>- DISABLE（不携带该字段）<br>默认值：ENABLE<br>配置原则：无 |
| HWQBCIDCT | huaweiQBCIndication | 可选必选说明：可选参数<br>参数含义：QBC计费时N40消息中是否携带huaweiQBCIndication信元。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不携带该字段）<br>- ENABLE（携带该字段）<br>默认值：DISABLE<br>配置原则：<br>如果CHF需要SMF显示指示N40消息为QBC计费的消息，开启该功能，开启前请确认对端CHF是否支持该信元。 |
| APPSVCPROVID | applicationserviceProviderIdentity | 可选必选说明：可选参数<br>参数含义：该参数用于控制N40消息中是否携带applicationserviceProviderIdentity（应用提供商标识）。<br>数据来源：全网规划<br>取值范围：<br>- ENABLE（携带该字段）<br>- DISABLE（不携带该字段）<br>默认值：DISABLE<br>配置原则：无 |
| RCP | 是否支持携带roamingChargingProfile | 可选必选说明：可选参数<br>参数含义：该参数用于控制RCP不协商场景，N40消息中RoamingQBCInformation信元是否携带RoamingChargingProfile。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE（携带该字段）<br>- DISABLE（不携带该字段）<br>默认值：ENABLE<br>配置原则：<br>该参数仅在SET HVNEGRCPSW命令的参数VSMFSW或HSMFSW设为DISABLE的场景生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N40MSGTEMP]] · N40消息属性模板（N40MSGTEMP）

## 使用实例

新增名为“n40attr”的模板，配置N40消息中不携带RANSecondaryRATUsageReport字段：

```
ADD N40MSGTEMP: TEMPLATENAME="n40attr", SECRATUSAGE=DISABLE, NBEXTENDATTR=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加N40消息属性模板（ADD-N40MSGTEMP）_48957459.md`
