---
id: UNC@20.15.2@MMLCommand@SET NFNRFMGMTPARA
type: MMLCommand
name: SET NFNRFMGMTPARA（设置NF与NRF间的全局管理参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NFNRFMGMTPARA
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
- SMSF
- CBCF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF参数管理
- NF与NRF间全局管理参数管理
status: active
---

# SET NFNRFMGMTPARA（设置NF与NRF间的全局管理参数）

## 功能

![](设置NF与NRF间的全局管理参数（SET NFNRFMGMTPARA）_32041712.assets/notice_3.0-zh-cn_2.png)

执行本命令将NTFUPDCACHESW开关打开时，当NRF订阅通知消息量较大时，可能会对通信造成压力。

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF、CBCF**

该命令用于配置NF与NRF间的管理参数。NF向NRF注册、订阅/通知、发现时，需要配置一些参数控制不同功能。例如NRF主备组网情况下，当主用NRF故障恢复后，NF可以配置自动从备用NRF切换到主用NRF；针对缓存的NF，可以控制本端网元是否使用NRF发送的订阅通知中的NfProfile信息更新其缓存信息。

## 注意事项

- 该命令执行后立即生效。

- 当MGMTNRFFAILCODE未设置时，将在连续收到NRF响应码502、504、602时，切换到新NRF上进行后续业务。
- 当DISCNRFFAILCODE未设置时，将在连续收到NRF响应码504时，后续服务发现流程切换到新NRF上进行。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCHMASTERNRF | SUBNTFSYNCDELAY | NFREGSRVMAPSW | NFDISCSRVMAPSW | NFPROFILECHKSW | TAIPOLICY | BSFREGMAPSW | TPROFILECHK | NFDIRREGSW | REGSMSFINFOSW | NTFUPDCACHESW | NTFPARMTHR | REGPERPLMNNSSW | ISNRFSYNC | DATACHKALMSW | NRFFCALMSW | NRFFCALMTIME |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OFF | 120 | OFF | OFF | AMF_TAI-1&SMF_SNSSAI-1&SMSF_GROUPID-1&SMSF_SUPI_OR_GPSI-1 | TAI_UNION | OFF | 0 | OFF | OFF | OFF | 2 | OFF | SUPPORT | OFF | OFF | 5 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCHMASTERNRF | 切换主用NRF开关 | 可选必选说明：可选参数<br>参数含义：NRF主备组网情况下，如果当前NF已经注册在备用NRF上，设置该参数为ON可以让NF实时感知主用NRF的状态。主用NRF恢复后，NF将会向主用NRF发起注册，从备用NRF切换到主用NRF。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：<br>主备NRF组网，主用NRF管理自身区域内的NF，当主NRF故障，备NRF可以接替原主NRF管理区域内的NF，当原主NRF故障恢复后需要原主NRF继续接管本区域管理的NF时，可以打开此开关。 |
| SUBNTFSYNCDELAY | 订阅通知后触发缓存同步时延 (秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定订阅推送后触发缓存同步更新的最大延时时间。实际系统中会在零到最大延时时间中选取随机数作为实际延时时间，以实现对缓存同步更新的离散化。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~300，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：<br>若配置为零，则最大延时时间取为120秒。 |
| NFREGSRVMAPSW | NFService注册MAP格式开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制NF注册的NF Service是否为MAP格式。<br>- 开关值为OFF时，NF注册携带Array格式的NF Service；<br>- 开关值为ON时，NF注册携带MAP格式的NF Service。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：<br>打开此开关需保证NRF支持相应功能。 |
| NFDISCSRVMAPSW | NFService服务发现MAP格式开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制NF服务发现请求NRF返回以及创建订阅请求NRF通知的NF Service是否为MAP格式。<br>- 开关值为OFF时，NF请求NRF返回的目标NF的NF Service为Array格式；<br>- 开关值为ON时，NF请求NRF返回的目标NF的NF Service为MAP格式。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：无 |
| NFPROFILECHKSW | NF参数检查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在NF注册/更新流程时，是否开启NF参数检查的开关。<br>- 当参数中NF的检查开关勾选时，NF注册/更新流程时会进行NF参数检查：如果参数检查失败，NF侧会上报“ALM-100225 NF注册失败”告警，且NF注册到对端的状态设置为Undiscoverable；<br>- 当参数中NF的检查开关未勾选时，NF注册/更新流程时不进行NF参数检查。<br>数据来源：本端规划<br>取值范围：<br>- “AMF_TAI（AMF_TAI）”：检查AMF注册/更新时，必须携带TAI List或TAI Range参数。<br>- “AMF_GUAMI（AMF_GUAMI）”：检查AMF注册/更新时，必须携带Guami参数。<br>- “AMF_SETID（AMF_SETID）”：检查AMF注册/更新时，必须携带AmfSetId参数。<br>- “AMF_N2INTERINFO（AMF_N2INTERINFO）”：检查AMF注册/更新时，必须携带N2InterfaceAmfInfo参数。<br>- “AMF_RESERVE1（AMF_RESERVE1）”：AMF预留，不使用。<br>- “AMF_RESERVE2（AMF_RESERVE2）”：AMF预留，不使用。<br>- “SMF_TAI（SMF_TAI）”：检查SMF注册/更新时，必须携带TAI List或TAI Range参数。<br>- “SMF_SNSSAI（SMF_SNSSAI）”：检查SMF注册/更新时，必须携带SNSSAI和对应的DNN参数。<br>- “SMF_ACCESSTYPE（SMF_ACCESSTYPE）”：检查SMF注册/更新时，必须携带ACCESSTYPE参数。<br>- “SMF_RESERVE1（SMF_RESERVE1）”：SMF预留，不使用。<br>- “SMF_RESERVE2（SMF_RESERVE2）”：SMF预留，不使用。<br>- “BSF_IP（BSF_IP）”：检查BSF注册/更新时，必须携带IP参数。<br>- “BSF_RESERVE1（BSF_RESERVE1）”：BSF预留，不使用。<br>- “SMSF_GROUPID（SMSF_GROUPID）”：检查SMSF注册/更新时，必须携带GROUPID参数。<br>- “SMSF_SUPI_OR_GPSI（SMSF_SUPI_OR_GPSI）”：检查SMSF注册/更新时，必须携带SUPI参数或GPSI参数。<br>- “SMSF_RESERVE1（SMSF_RESERVE1）”：SMSF预留，不使用。<br>- “AMF_SNSSAI（AMF_SNSSAI）”：检查AMF注册/更新时，必须携带SNSSAI参数。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：无 |
| TAIPOLICY | AMF向NRF注册的TAI策略 | 可选必选说明：可选参数<br>参数含义：该参数用于控制AMF向NRF注册的TAI范围的组合方式，即本地配置和无线上报的TAI进行组合的方式，本地配置可以通过ADD TACRANGE、ADD TAIRANGELIST进行配置。<br>数据来源：全网规划<br>取值范围：<br>- TAI_UNION（取本地配置和无线上报的TAI并集）<br>- TAI_INTER（取本地配置和无线上报的TAI交集）<br>- TAI_LOCAL_ONLY（仅取本地配置的TAI）<br>- TAI_REPORT_ONLY（仅取无线上报的TAI）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：<br>当TAIPOLICY设置为TAI_UNION时，是否合并静态配置和无线上报的TA信息由软参DWORD201 BIT22 控制。 |
| BSFREGMAPSW | 注册时BsfInfo的MAP格式开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制BSF注册的BsfInfo是否为MAP格式。<br>- 开关值为OFF时，BSF注册携带Array格式的BsfInfo；<br>- 开关值为ON时，BSF注册携带MAP格式的BsfInfo。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：无 |
| TPROFILECHK | 数据校验周期(分钟) | 可选必选说明：可选参数<br>参数含义：用于控制NF周期性发起向NRF进行数据校验的时间间隔（分钟），当值为0时表示不开启周期性数据校验。NF向NRF进行数据校验的内容为NF本地配置的NFProfile信息和NRF上存储的该NF的NFProfile信息，如果两者不一致NF会自动触发一次注册，保证NRF上存储的NFProfile信息和本地配置的保持一致。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是60~1440，0，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：无 |
| NFDIRREGSW | 参数检查NF直接注册开关 | 可选必选说明：可选参数<br>参数含义：用于控制NF周期性发起向NRF进行数据校验时是否直接发起重注册。<br>- 开关值为OFF时，将NF和NRF上的NFProfile数据进行比对，不一致发起重注册，一致则不发起重注册；<br>- 开关值为ON时直接发起重注册。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：无 |
| MGMTNRFFAILCODE | NF管理类流程NRF故障返回码 | 可选必选说明：可选参数<br>参数含义：该参数用于配置本端网元管理类流程NRF故障返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是0~1024。只允许输入数字和“-”，“-”用于分隔不同的错误码。例如：401-403。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：<br>- 当NRF故障且本端网元管理类流程中长期未切换NRF时，可以根据NRF的返回码设置本参数。<br>- 本参数目前只支持NRF主备组网。<br>- 配置该参数时需要考虑内部错误码，如504等。<br>- 本参数不支持错误码为400或413时切换NRF。 |
| DISCNRFFAILCODE | NF服务发现流程NRF故障返回码 | 可选必选说明：可选参数<br>参数含义：该参数用于配置本端网元服务发现流程NRF故障返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是0~1024。只允许输入数字和“-”，“-”用于分隔不同的错误码。例如：400-403。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：<br>- 当NRF故障且本端网元服务发现流程中长期未切换NRF时，可以根据NRF的返回码设置本参数。<br>- 本参数目前只支持NRF主备组网。<br>- 当需要该参数生效，需要本端网元类型为CHF、NRF或设置软参SET COMMONSOFTPARAOFBIT: DT=DwCom, DWORDCOMNUM=4, VALUE=VALUE_1, POSITION=18。<br>- 配置该参数时需要考虑内部错误码，如504等。 |
| REGSMSFINFOSW | SMSF注册携带SmsfInfo开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制SMSF向NRF注册时是否携带SmsfInfo。开关值为OFF时，SMSF注册不携带SmsfInfo；开关值为ON时，SMSF注册携带SmsfInfo。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：无 |
| NTFUPDCACHESW | 订阅通知更新缓存开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制针对缓存的NF，本端网元是否使用NRF发送的订阅通知中的NfProfile信息更新其缓存信息。<br>数据来源：对端协商<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：<br>执行本命令将NTFUPDCACHESW开关打开时，当NRF订阅通知消息量较大时，可能会对通信造成压力。 |
| NTFPARMTHR | 订阅通知中信元长度阈值 | 可选必选说明：该参数在"NTFUPDCACHESW"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于指定接收到订阅通知中的信元长度的阈值。当本端网元收到NRF发送的订阅通知时，如NfProfile中的supi、gpsi、tai、dnn的信元长度都小于该参数值时，不使用订阅通知中的NfProfile信息更新其缓存信息，而是后续向NRF服务发现更新缓存。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：无 |
| REGPERPLMNNSSW | 注册携带PerPlmnSnssaiList开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制本端网元向NRF注册时是否携带PerPlmnSnssaiList。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：无 |
| ISNRFSYNC | NRF是否支持数据同步 | 可选必选说明：可选参数<br>参数含义：该参数用于在NRF主备或NRF双活组网情况下，设置NRF是否有数据同步的功能 。<br>数据来源：全网规划<br>取值范围：<br>- SUPPORT（支持）<br>- NOTSUPPORT（不支持）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：<br>如果NRF未实现数据备份，需要将ISNRFSYNC设置为NOTSUPPORT，用于支持高优先级NRF故障恢复后本端NF向高优先级NRF的自动回迁。 |
| DATACHKALMSW | 数据校验不一致上报告警开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制NF向NRF周期性发起数据校验的数据校验结果不一致时是否上报ALM-100225 NF注册失败告警。<br>- 开关值为OFF时，数据校验结果不一致时不上报告警；<br>- 开关值为ON时，数据校验结果不一致时上报告警。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：无 |
| NRFFCALMSW | NRF服务发现流控告警上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否上报ALM-100720 NRF服务发现流控告警。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：无 |
| NRFFCALMTIME | NRF服务发现流控告警检测周期(分钟) | 可选必选说明：该参数在"NRFFCALMSW"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于指定ALM-100720 NRF服务发现流控告警的检测周期。在配置的时间周期内每分钟检测一次是否存在流控，检测周期内每分钟都出现流控则上报告警，检测周期内每分钟都没有出现流控则告警恢复。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1440，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFNRFMGMTPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFNRFMGMTPARA]] · NF与NRF间的全局管理参数（NFNRFMGMTPARA）

## 使用实例

设置切换主用NRF开关为开。

```
SET NFNRFMGMTPARA:SWITCHMASTERNRF=ON,SUBNTFSYNCDELAY=120;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置NF与NRF间的全局管理参数（SET-NFNRFMGMTPARA）_32041712.md`
