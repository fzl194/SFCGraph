---
id: UNC@20.15.2@MMLCommand@SET SMFCACHEFUNC
type: MMLCommand
name: SET SMFCACHEFUNC（设置SMF映射关系的本地缓存策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMFCACHEFUNC
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- SMF缓存策略管理
status: active
---

# SET SMFCACHEFUNC（设置SMF映射关系的本地缓存策略）

## 功能

![](设置SMF映射关系的本地缓存策略（SET SMFCACHEFUNC）_88377456.assets/notice_3.0-zh-cn_2.png)

开关变更可能对进程CPU和内存产生影响。

**适用NF：AMF**

该命令用于设置SMF映射关系的本地缓存策略，通过设置缓存策略，后续查询时先判断当前缓存信息是否可用，以减少SMF服务发现。

## 注意事项

- 该命令执行后立即生效。

- SMFCACHESW参数的取值对NSA漫游用户或SA漫游用户的H-SMF不生效，无论参数的取值是“YES（是）”还是“NO（否）”，都不将NSA漫游用户或SA漫游用户的H-SMF信息存入本地缓存。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SMFCACHESW | AGEINGTIMER | INTERWORKSW | NONROAMINTRASW | ROAMINTRASW |
| --- | --- | --- | --- | --- |
| NO | 60 | YES | YES | YES |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMFCACHESW | 是否打开SMF映射关系本地缓存 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否打开SMF与TAI映射关系本地缓存以及PGW FQDN与锚点SMF映射关系本地缓存。<br>该参数为SMF本地缓存功能的总开关，INTERWORKSW、NONROAMINTRASW、ROAMINTRASW参数按子场景控制SMF本地缓存功能。当SMFCACHESW和子场景开关都打开时，对应场景下的SMF本地缓存功能才能生效。<br>当开关设置为"YES"时，AMF会缓存SMF与TAI映射关系以及PGW FQDN与锚点SMF映射关系。在4G到5G的重选流程以及4G到5G的切换流程中，当PGW FQDN发生变更时可以优先判断是否存在当前PGW FQDN到锚点SMF的缓存，。<br>如果存在，则直接使用本地缓存中的锚点SMF; 其它流程当UE发生TAI变更时可以优先从SMF-TAI映射缓存中判断当前选择的SMF是否支持用户所在的TAI，以减少服务发现。<br>当开关设置为"NO"时，则直接进行服务发现选择。<br>数据来源：本端规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无。<br>配置原则：无 |
| AGEINGTIMER | 老化时长(分钟) | 可选必选说明：该参数在"SMFCACHESW"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于指定SMF与TAI列表映射关系以及PGW FQDN与锚点SMF映射关系的老化时间，当超过老化时间，本地缓存的映射关系将在最新查询时触发更新，覆盖本地的缓存关系。更新的数据来源于新的服务发现结果。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFCACHEFUNC查询当前参数配置值。<br>配置原则：无 |
| INTERWORKSW | 45G互操作场景是否打开SMF缓存 | 可选必选说明：可选参数<br>参数含义：该参数用于指定4G到5G的重选以及4G到5G的切换场景下是否优先使用本地缓存查询SMF。<br>漫游用户和非漫游用户都受此开关控制。<br>数据来源：本端规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFCACHEFUNC查询当前参数配置值。<br>配置原则：<br>开启WSFD-104510 LTE与5G SA网络间重选特性和WSFD-104511 LTE与5G SA网络间切换特性后，可能会增加AMF性能开销，此时可将开关设置为"YES"。 |
| NONROAMINTRASW | 非漫游AMF内移动性流程是否打开SMF缓存 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跨区域场景下Service Request/Xn Handover等Intra AMF移动性管理流程是否优先使用本地缓存查询SMF。<br>非漫游用户和漫游用户的LBO模式会话都受此参数控制。<br>数据来源：本端规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFCACHEFUNC查询当前参数配置值。<br>配置原则：<br>跨区域场景下Service Request/Xn Handover等Intra AMF移动性管理流程AMF查询用户所在区域SMF次数过多，影响AMF性能，本开关设置为"YES"，AMF比较会话上下文存储的位置信息与用户当前位置信息，如果相同，则不需要服务发现SMF，减少AMF发现SMF的次数，提高AMF性能。 |
| ROAMINTRASW | 漫游场景AMF内移动性流程是否打开SMF缓存 | 可选必选说明：可选参数<br>参数含义：该参数用于漫游用户PDU会话模式为HomeRouted时，Service Request/Xn Handover等Intra AMF移动性管理流程是否优先使用本地缓存查询SMF。<br>数据来源：本端规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFCACHEFUNC查询当前参数配置值。<br>配置原则：<br>漫游用户有HomeRouted模式的PDU会话时，Service Request/Xn Handover等Intra AMF移动性管理流程AMF查询用户所在区域SMF次数过多，影响AMF性能，本开关设置为"YES"，AMF比较会话上下文存储的位置信息与用户当前位置信息，如果相同，则不需要服务发现SMF，减少AMF发现SMF的次数，提高AMF性能。本参数对HSMF不生效。 |

## 操作的配置对象

- [SMF映射关系的本地缓存策略（SMFCACHEFUNC）](configobject/UNC/20.15.2/SMFCACHEFUNC.md)

## 使用实例

设置AMF上支持SMF映射关系缓存策略，其中老化时长为60分钟，执行如下命令：

```
SET SMFCACHEFUNC:SMFCACHESW=YES,AGEINGTIMER=60;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMF映射关系的本地缓存策略（SET-SMFCACHEFUNC）_88377456.md`
