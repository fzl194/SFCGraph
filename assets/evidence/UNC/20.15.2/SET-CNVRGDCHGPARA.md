# 设置融合计费全局参数（SET CNVRGDCHGPARA）

- [命令功能](#ZH-CN_MMLREF_0209653056__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653056__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653056__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653056__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209653056)

**适用NF：PGW-C、SMF**

该命令用于配置融合计费全局参数。

## [注意事项](#ZH-CN_MMLREF_0209653056)

- 该命令执行后立即生效。

- 参数OFLRGTIMECALC和CHGDATAREFFMT功能仅针对新用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MULTIUPFQUOTAM | ROAMHSMFQBC | MLOCMISSPRC | CHGDATAREFGEN | STARTTRIGGER | IPV6ITFID | RGTRIGGERFILL | OFLRGTIMECALC | RPTBASEDONGU | DEFERPDUTRIG | PDULIMITTRIG | RGLIMITTRIG | MERGERGVTSW | BADRSPACT | SPTABNTRIGGER | TIMEROUNDMODE | DELDYNRULENTYUP | NOSRVRPTSW | CHGDATAREFFMT | WAITUPDRSPSW | CHGDATAREFUSE | IGNOREERRTRIGS | CONTINUEALARM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QUOTAINDEP | DISABLE | ABSENCE | CHF | DISABLE | INITITFID | DISABLE | PACKETTRIGGERED | DISABLE | PDULVLNOTCARRY | ONLINE-1&OFFLINE-1&CONVERGED-1 | OFFLINE-1&CONVERGED-1 | DISABLE | TERMINATE | ENABLE | ROUNDOFF | ENABLE | ENABLE | CHGDATAREF_FMT_DEFAULT | DISABLE | SMF | ENABLE | DISABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0209653056)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653056)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MULTIUPFQUOTAM | 多UPF场景配额管理 | 可选必选说明：可选参数<br>参数含义：该参数用于设置多UPF场景配额管理方式。<br>数据来源：全网规划<br>取值范围：<br>- “QUOTAINDEP（独立配额）”：各UPF独立使用CHF下发的配额<br>- “QUOTASHARED（共享配额）”：多UPF共享使用CHF下发的配额<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| ROAMHSMFQBC | 漫游用户归属地QBC计费 | 可选必选说明：可选参数<br>参数含义：该参数用于设置漫游用户在归属地是否进行QBC计费。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（不使能）”：漫游用户在归属地关闭QBC功能。<br>- “ENABLE（使能）”：漫游用户在归属地使用QBC功能。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| MLOCMISSPRC | 位置信息必选信元缺失处理 | 可选必选说明：可选参数<br>参数含义：设置4、5G切换过程中，位置信息必选信元缺失时的处理方式。<br>数据来源：本端规划<br>取值范围：<br>- “ABSENCE（不携带）”：缺失的必选位置信息不携带。<br>- “ZEROVALUE（携带零值）”：缺失的必选位置信息携带0值字符串。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| CHGDATAREFGEN | ChargingDataRef生成方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定融合计费ChargingDataRef的生成方式。需要打开SMF本地缓存融合计费消息的功能时，请指定使用SMF生成。<br>数据来源：全网规划<br>取值范围：<br>- CHF（CHF生成ChargingDataRef）<br>- SMF（SMF生成ChargingDataRef）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：<br>ChargingDataRef的生成方式需要预先规划。 |
| STARTTRIGGER | 携带Start Trigger开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示新业务上报场景是否支持在业务容器中携带Start Trigger。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：<br>当该参数配置为ENABLE，且N40APIVER命令的N40APIVER参数配置为F40时，建议打开DWORD513 BIT5，携带F40协议格式的“usedUnitContainer”信元。 |
| IPV6ITFID | IPv6地址Interface Identifier | 可选必选说明：可选参数<br>参数含义：该参数用于设置N40接口用户IPv6地址interface identifier的填写方式。<br>数据来源：全网规划<br>取值范围：对于N40接口，在UPF/PGW-U不产生流量时，仍然可能会与CHF有交互，此时携带的interface identifier为初始分配的；后续再UPF/PGW-U有流量产生时，才能获取到数据中的interface identifier。对外呈现N40接口同一计费会话，用户IPv6地址中的interface identifier在参数IPV6ITFID设置为“UPDATAITFID”时，中间可能会改变。<br>- “INITITFID（INITITFID）”：使用用户签约IPv6地址或核心网分配的IPv6地址的interface identifier<br>- “UPDATAITFID（UPDATAITFID）”：使用UP上用户上行数据包中源IPv6地址的interface identifier<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| RGTRIGGERFILL | RG级Trigger填写方式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当仅对PDU会话有效的Trigger发生时，生成的业务容器是否携带同PDU会话一样的Trigger。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：当仅对PDU会话有效的Trigger发生时，生成的业务容器中不携带同PDU会话一样的Trigger<br>- “ENABLE（使能）”：当仅对PDU会话有效的Trigger发生时，生成的业务容器中携带同PDU会话一样的Trigger<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：<br>缺省时，SMF按Trigger的实际生效粒度携带在PDU会话级或RG级。<br>当CHF期望在仅对PDU会话有效的Trigger发生时，生成的业务容器中也携带同PDU会话一样的Trigger，可以使能该功能。<br>当该参数配置为ENABLE且N40APIVER命令的N40APIVER参数配置为F40时，建议打开DWORD513 BIT5，携带F40协议格式的“usedUnitContainer”信元。 |
| OFLRGTIMECALC | 离线RG时长计算方式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置CP指示UP离线RG的时长计费方式。<br>数据来源：本端规划<br>取值范围：<br>- “PACKETTRIGGERED（PACKETTRIGGERED）”：统计周期内收到第一个数据包到最后一个数据包的时长<br>- “CONTINUOUS（CONTINUOUS）”：从收到URR开始计算连续时长<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| RPTBASEDONGU | 基于GrantedUnit上报用量 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否基于GrantedUnit上报用量。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能，则不基于GrantedUnit上报用量，即按实际用量上报。<br>- “ENABLE（使能）”：使能，则基于GrantedUnit上报用量，即上报用量不会大于GrantedUnit下发的配额。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：<br>根据计费系统的处理能力进行设置。 |
| DEFERPDUTRIG | 延时上报PDU级Trigger携带方式 | 可选必选说明：可选参数<br>参数含义：该参数用于控制延时上报的PDU级Trigger在融合计费请求消息PDU级的携带方式。<br>数据来源：本端规划<br>取值范围：<br>- “PDULVLNOTCARRY（PDU级不携带）”：PDU级延时上报的Trigger不在下一次Session级上报消息的PDU Trigger中携带。<br>- “PDULVLCARRY（PDU级携带）”：PDU级延时上报的Trigger在下一次Session级上报消息的PDU Trigger中携带。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| PDULIMITTRIG | PDU级门限Trigger适用范围 | 可选必选说明：可选参数<br>参数含义：该参数用于设置PDU级门限Trigger的适用范围。<br>数据来源：本端规划<br>取值范围：<br>- “ONLINE（在线计费用户）”：PDU级门限Trigger适用于在线计费用户。<br>- “OFFLINE（离线计费用户）”：PDU级门限Trigger适用于离线计费用户。<br>- “CONVERGED（融合计费用户）”：PDU级门限Trigger适用于融合计费用户。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| RGLIMITTRIG | RG级门限Trigger适用范围 | 可选必选说明：可选参数<br>参数含义：该参数用于设置RG级门限Trigger的适用范围。<br>数据来源：本端规划<br>取值范围：<br>- “OFFLINE（离线计费用户）”：RG级门限Trigger适用于离线计费用户。<br>- “CONVERGED（融合计费用户）”：RG级门限Trigger适用于融合计费用户。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| MERGERGVTSW | RG VT事件合并上报开关 | 可选必选说明：可选参数<br>参数含义：该参数控制同时发生的RG VT事件合并上报。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：每个RG VT事件单独上报CHF，不做消息合并。<br>- “ENABLE（使能）”：对同时发生的RG VT进行合并，一起上报给CHF。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| IGNORERSPAVP | 忽略CHF响应消息的信元列表 | 可选必选说明：可选参数<br>参数含义：该参数用于SMF处理CHF响应消息时，忽略CHF下发的指定信元。<br>数据来源：全网规划<br>取值范围：<br>- “INVOCATIONNUM（忽略Invocation Sequence Number）”：忽略CHF响应消息中的Invocation Sequence Number，不检查是否跟请求消息一致。<br>- “FUI（忽略FinalUnitIndication）”：当RG级ResultCode不是Success时，忽略CHF响应消息中的FinalUnitIndication，按照对应RGRCACT配置的动作执行。<br>- “SESSIONFAILOVER（忽略SessionFailover）”：忽略CHF响应消息中的SessionFailover，使用CCT中的FAILOVERSUP。<br>- “FAILUREHANDLING（忽略FailureHandling）”：忽略CHF响应消息中的FailureHandling，使用CCT中的FHACTION。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| BADRSPACT | CHF响应消息信元错误的处理动作 | 可选必选说明：可选参数<br>参数含义：该参数用于控制CHF的响应消息携带信元错误时SMF的处理动作。<br>数据来源：全网规划<br>取值范围：<br>- “TERMINATE（去活会话）”：去活PDU会话。<br>- “CONTINUE（允许业务继续进行）”：允许业务继续进行，不再进行配额管理。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：<br>该参数配置动作为CONTINUE时，控制在CHF的响应消息中携带信元错误的场景下允许业务继续进行。 |
| SPTABNTRIGGER | Trigger中是否支持填写AbnormalRelease | 可选必选说明：可选参数<br>参数含义：该参数用于控制Trigger中是否支持填写AbnormalRelease。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：支持Trigger填写AbnormalRelease。<br>- “DISABLE（不使能）”：不支持Trigger填写AbnormalRelease，将AbnormalRelease改为Final。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：<br>对于N40DIAGTRIGGER中设置为ABNORMALRELEASE的情况，本命令不生效。 |
| TIMEROUNDMODE | 控制Nchf消息中时间戳的计算方式 | 可选必选说明：可选参数<br>参数含义：该参数用于控制Nchf消息中时间戳的计算方式。控制的字段包含StartTime、StopTime、invocationTimeStamp。<br>数据来源：本端规划<br>取值范围：<br>- “ROUNDOFF（四舍五入）”：Nchf消息中时间戳相关的信元，将毫秒转换为秒时按四舍五入计算。<br>- “ROUNDDOWN（向下取整）”：Nchf消息中时间戳相关的信元，将毫秒转换为秒时按向下取整计算。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| DELDYNRULENTYUP | 删除动态规则是否通知用户面 | 可选必选说明：可选参数<br>参数含义：该参数用于控制动态规则删除时，SMF是否显式地向UPF指示删除URR。本参数仅控制融合计费使用的，通过动态规则关联的动态URR删除场景。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：通知UPF删除URR。<br>- “DISABLE（不使能）”：不通知UPF删除URR。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：<br>如果此参数设置为DISABLE，则不推荐ADD CCT或MOD CCT中将QHTEXPIREDRSU设置为WITH_RSU，否则会导致动态规则创建的动态URR无法通过QHT功能老化。 |
| IGNORETRIGGER | 忽略CHF下发的Trigger列表 | 可选必选说明：可选参数<br>参数含义：该参数用于SMF处理CHF响应消息时，忽略CHF下发指定的Trigger控制，使用命令PDUTRIGGER、RGTRIGGER配置的Trigger控制，包含会话级Trigger和RG级Trigger。<br>数据来源：本端规划<br>取值范围：<br>- “MAXNUMCCC（计费条件改变阈值）”：忽略CHF响应消息中的MAX_NUMBER_OF_CHANGES_IN_CHARGING_CONDITIONS的Trigger，使用命令PDUTRIGGER配置的Trigger控制。<br>- “PDUTIMELIMIT（会话级时间阈值）”：忽略CHF响应消息中的会话级TIMELIMIT Trigger，使用命令PDUTRIGGER配置的Trigger控制。<br>- “PDUVOLUMELIMIT（会话级流量阈值）”：忽略CHF响应消息中的会话级VOLUMELIMIT Trigger，使用命令PDUTRIGGER配置的Trigger控制。<br>- “RGTIMELIMIT（RG级时间阈值）”：忽略CHF响应消息中的RG级TIMELIMIT Trigger，使用命令RGTRIGGER配置的Trigger控制。<br>- “RGVOLUMELIMIT（RG级流量阈值）”：忽略CHF响应消息中的RG级VOLUMELIMIT Trigger，使用命令RGTRIGGER配置的Trigger控制。<br>- “QHT（配额保持时长）”：忽略CHF响应消息中的QHT Trigger，使用命令RGTRIGGER配置的Trigger控制。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：<br>配置本参数时，CHF在响应消息中携带了Trigger的前提下，未携带某个通过本参数忽略的Trigger，仍然会采用该被忽略的Trigger的配置值。配置前需要确认上述Trigger生效方式是否符合预期。 |
| NOSRVRPTSW | 无业务上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制会话级事件发生时，用户当前无业务需要上报的情况下SMF是否需要上报CHF。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：上报CHF。<br>- “DISABLE（不使能）”：不上报CHF。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| CHGDATAREFFMT | ChargingDataRef格式 | 可选必选说明：该参数在"CHGDATAREFGEN"配置为"SMF"时为条件可选参数。<br>参数含义：该参数用于配置ChargingDataRef的格式。<br>数据来源：全网规划<br>取值范围：<br>- “CHGDATAREF_FMT_DEFAULT（ChargingDataRef默认格式）”：使用ChargingDataRef的默认格式。{SMF网元NfInstanceId}{SMF为PDU会话分配的ChargingId }{时间戳}。<br>- “CHGDATAREF_FMT_CUSTOM1（ChargingDataRef运营商定制格式）”：使用ChargingDataRef的运营商定制格式。{SMF网元NfInstanceId}-{SMF为PDU会话分配的ChargingId }-{时间戳}。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| WAITUPDRSPSW | 去活等待更新消息响应开关 | 可选必选说明：可选参数<br>参数含义：该参数用于用户去活时是否需要等待CHF更新请求消息的响应。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：<br>使能该功能时会导致会话去活等待时间变长，为避免重复激活场景丢失N40接口Release消息，建议同时开启SMF软参DWORD504 BIT18。 |
| CHGDATAREFUSE | ChargingDataRef使用方式 | 可选必选说明：该参数在"CHGDATAREFGEN"配置为"SMF"时为条件可选参数。<br>参数含义：该参数用于指定融合计费ChargingDataRef的使用方式。<br>数据来源：全网规划<br>取值范围：<br>- SMF（使用SMF生成的ChargingDataRef）<br>- “CHF（使用CHF生成的ChargingDataRef）”：优先使用CHF生成的ChargingDataRef，如果CHF未携带ChargingDataRef给SMF，使用SMF生成的ChargingDataRef。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：<br>ChargingDataRef的使用方式需要预先规划。 |
| IGNOREERRTRIGS | 忽略CHF下发非法Triggers | 可选必选说明：可选参数<br>参数含义：该参数用于控制CHF下发的Triggers包含的所有Trigger均为非法信元时是否要忽略。该参仅控制Triggers信元包含的Trigger数量不为零，且所有的Trigger都存在非法子信元的场景。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |
| CONTINUEALARM | 缓存未开启放通告警开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否开启“融合计费用户放通不计费”告警功能。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能，则不开启“融合计费用户放通不计费”告警功能。<br>- “ENABLE（使能）”：使能，则开启“融合计费用户放通不计费”告警功能。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CNVRGDCHGPARA查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653056)

配置融合计费全局参数多UPF场景为独立配额管理；漫游场景归属地QBC会话管理使能：

```
SET CNVRGDCHGPARA: MULTIUPFQUOTAM=QUOTAINDEP, ROAMHSMFQBC=ENABLE;
```
