---
id: UNC@20.15.2@MMLCommand@SET NGLCSPARA
type: MMLCommand
name: SET NGLCSPARA（设置5G定位服务参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NGLCSPARA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G定位服务管理
- 定位服务管理
status: active
---

# SET NGLCSPARA（设置5G定位服务参数）

## 功能

![](设置5G定位服务参数（SET NGLCSPARA）_44007975.assets/notice_3.0-zh-cn_2.png)

开启定位服务功能后，为保护用户位置信息，应添加位置定位安全加固配置。

**适用NF：AMF**

该命令用于设置AMF的定位服务功能的相关参数。

Non-UE辅助定位流程中，AMF是否支持Namf_Communication_NonUeN2InfoSubscribe Request消息不携带globalRanNodeList信元受软参DWORD71 BIT7控制。

## 注意事项

- 该命令执行后立即生效。

- 当前版本不支持此命令的POSEXPR参数。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| LCSSW | POSEXPR | LCSPLCY | LRC | GUAMINOTIFY | LCSIDCHK | LMFRETRY | SUPISW | GPSISW | CAMPLCSEN | NSSW | LCSQOSCLASS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OFF | 60 | PROTOCOL_POSITION | NO | NO | NO | NO | NO | NO | OFF | NO | NO |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LCSSW | 定位服务功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于开启和关闭5G定位服务功能。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：<br>当运营商希望开启定位服务功能时，设置为“ON”；当运营商希望关闭定位服务功能时，设置为“OFF”。 |
| POSEXPR | 5G位置信息表老化定时器(min) | 可选必选说明：可选参数<br>参数含义：该参数用于设置AMF的位置信息表的老化定时器。当前该功能尚未实现。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~60，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：<br>如果定位业务需要查询用户初始位置的次数较多，建议配置较长的定时器；如果定位业务查询用户初始位置的次数较少，建议配置较短的定时器。 |
| LCSPLCY | 5G定位服务策略 | 可选必选说明：可选参数<br>参数含义：该参数用于设置AMF的定位服务策略。<br>数据来源：全网规划<br>取值范围：<br>- “PROTOCOL_POSITION（协议模式定位）”：协议模式定位<br>- “NO_LMF_POSITION（无LMF定位）”：无LMF的定位<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：<br>当取值为“PROTOCOL_POSITION（协议模式定位）”时，系统按照3GPP协议定义的标准规范进行LCS定位。<br>当取值为“NO_LMF_POSITION（无LMF定位）”时，适用于没有部署LMF网元场景的LCS定位。此种策略下定位上报结果是NCGI信息而不是经纬度信息，精度较低。 |
| LRC | 启用连接态LRC流程 | 可选必选说明：可选参数<br>参数含义：该参数用于控制AMF收到GMLC的Namf_Location_ProvidePositioningInfo Request消息时，如果UE处于连接态，是否需要发起Location Reporting Control(LRC)流程获取最新的NCGI。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：<br>该功能在协议标准流程上增加了Location Reporting Control(LRC)流程，用于获取UE最新的NCGI信息。一般情况下请保持系统初始设置值，只有在有特殊需求的局点才需要开启。如需调整，请联系华为技术支持。 |
| GUAMINOTIFY | 是否携带GUAMI信息 | 可选必选说明：可选参数<br>参数含义：该参数用于控制AMF在Namf_Communication_N2InfoNotify Request和Namf_Communication_N1MessageNotify Request消息中是否携带为UE服务的GUAMI信息。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：否<br>- “YES（是）”：是<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：无 |
| LCSIDCHK | 是否校验LCS Correlation ID | 可选必选说明：可选参数<br>参数含义：该参数用于使能LCS Correlation ID校验功能。<br>LCS Correlation ID由AMF分配，用于标识一次定位流程，由AMF在发起LMF精准定位流程中传递给LMF，开启此功能可以避免LMF伪造场景带来的安全可靠问题。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：无 |
| LMFRETRY | 是否重选LMF | 可选必选说明：可选参数<br>参数含义：该参数用于指定当AMF选择某个LMF进行定位流程，如果对端返回5xx原因值时，是否重新选择新的LMF再次重试业务请求。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：<br>当本参数取值为“YES”时，一次定位流程中，最多进行一次LMF重选。此功能适用于现网部署多个LMF的场景。 |
| SUPISW | 是否使用SUPI | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用用户的SUPI作为目标LMF的选择条件。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：否<br>- “YES（是）”：是<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：<br>本参数只有在运营商使用SUPI号段规划LMF的时候才需要打开。 |
| GPSISW | 是否使用GPSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用用户的GPSI作为目标LMF的选择条件。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：否<br>- “YES（是）”：是<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：<br>本参数只有在运营商使用GPSI号段规划LMF的时候才需要打开。 |
| CAMPLCSEN | 园区定位增强开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制AMF在MT-LR或周期性定位流程中，是否优先使用GMLC在Namf_Location_ProvidePositioningInfo Request消息中携带的lmfId去发现指定LMF。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：<br>园区定位场景下，GMLC可以携带园区lmfId，指示AMF选择园区LMF。<br>该功能和使用SUPI、GPSI、切片发现LMF功能互斥。当本参数设置为“ON（打开）”且GMLC携带lmfId时，SUPISW、GPSISW和NSSW参数控制不生效。<br>AMF使用lmfId发现LMF目前仅支持LocalNRF模式。 |
| DFTLMFGRPID | 缺省的LMF群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定缺省的LMF群组标识。当该参数非空时，定位流程AMF会使用本参数发现LMF。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。大小写不敏感。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：<br>lmfGroupId不是AMF选择LMF的标准选择条件，需要依赖AMF的local NRF功能。 |
| NSSW | 是否使用切片 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用用户的切片作为目标LMF的选择条件。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：否<br>- “YES（是）”：是<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：<br>本参数只有在运营商使用切片规划LMF的时候才需要打开。 |
| LCSQOSCLASS | 是否携带lcsQosClass信息 | 可选必选说明：可选参数<br>参数含义：该参数用于控制AMF在Nlmf_Location_DetermineLocation Request消息中是否携带lcsQosClass信息。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：否<br>- “YES（是）”：是<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGLCSPARA查询当前参数配置值。<br>配置原则：<br>针对MT-LR流程，当GMLC发送的Namf_Location_Provide_PositioningInfo Request消息中携带lcsQosClass且携带的HAccuracy或VAccuracy有效，建议将本开关设置为"YES"。<br>针对NI-LR流程，当本地配置的lcsQosClass和HAccuracy有效，建议将本开关设置为"YES"。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGLCSPARA]] · 5G定位服务参数（NGLCSPARA）

## 使用实例

将AMF的5G位置信息表老化定时器设置为30分钟，执行如下命令：

```
SET NGLCSPARA:POSEXPR=30;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NGLCSPARA.md`
