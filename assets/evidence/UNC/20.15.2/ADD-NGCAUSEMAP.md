# 增加5G原因值映射配置（ADD NGCAUSEMAP）

- [命令功能](#ZH-CN_MMLREF_0319478931__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0319478931__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0319478931__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0319478931__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0319478931)

![](增加5G原因值映射配置（ADD NGCAUSEMAP）_19478931.assets/notice_3.0-zh-cn_2.png)

配置下发的原因值可能会对终端行为产生影响，该命令必须通过华为研发工程师评审后使用。

**适用NF：AMF**

该命令用于增加5G NAS原因值映射配置。原因值映射即为AMF给UE下发的NAS原因值映射成特定原因值。

## [注意事项](#ZH-CN_MMLREF_0319478931)

- 该命令执行后立即生效。

- 该命令必须通过华为研发工程师评审后使用。
- 相同流程中，对于同一种原因值映射配置，ADD NGCAUSEMAP命令优先级高于SET NGMMPROCTRL、ADD NGACCAREALST、SET NGIPAREACTRL等命令。
- 如果同时存在协议原因值和内部原因值的配置记录，内部原因值的配置记录优先级高于协议原因值的配置记录。
- 最多可输入127条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0319478931)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0319478931)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROT | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程类型，根据场景来确认是否需要配置相应的流程。<br>数据来源：全网规划<br>取值范围：<br>- INIT_REG（初始注册）<br>- MOBL_INTRA_REG（移动性INTRA注册）<br>- MOBL_INTER_REG（移动性INTER注册）<br>- PROD_REG（周期性注册）<br>- REG_AFT_INTRAHO（INTRA切换流程后的注册）<br>- REG_AFT_INTERHO（INTER切换流程后的注册）<br>- IDLE_SYSCHG_REG（空闲态EPS到5GS注册）<br>- CONN_SYSCHG_REG（连接态EPS到5GS切换后的注册）<br>- PDU_SESSION_EST_PROC（PDU Session创建流程）<br>- SERVICE_REQUEST（服务请求）<br>- ALL（所有注册、PDU Session创建、服务请求的失败流程）<br>- RESERV_PROC1（预留字段1）<br>- RESERV_PROC2（预留字段2）<br>- RESERV_PROC3（预留字段3）<br>- RESERV_PROC4（预留字段4）<br>- RESERV_PROC5（预留字段5）<br>- RESERV_PROC6（预留字段6）<br>默认值：无<br>配置原则：<br>指定流程和“ALL”类型同时配置时，指定流程配置的原因值映射优先级高于“ALL”类型配置的原因值映射。对于SMF拒绝的PDU Session创建流程，该命令所配置的原因值映射不生效。 |
| SCAUSETYPE | 原始原因值类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要映射的原始原因值的类型。<br>数据来源：全网规划<br>取值范围：<br>- “PROTOCOL_CAUSE（协议原因值）”：表示协议定义的原因值。<br>- “INNER_CAUSE（内部原因值）”：表示产品内部使用的原因值。<br>默认值：PROTOCOL_CAUSE<br>配置原则：<br>如需使用内部原因值转换功能，请联系华为技术支持处理。 |
| SCAUSE | 原始原因值 | 可选必选说明：该参数在"SCAUSETYPE"配置为"PROTOCOL_CAUSE"时为条件必选参数。<br>参数含义：该参数用于指定下发到目标网元的原始原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| PROCSTAGE | 流程阶段 | 可选必选说明：该参数在"SCAUSETYPE"配置为"INNER_CAUSE"时为条件必选参数。<br>参数含义：该参数用于指定需要进行原因值映射的流程阶段。<br>数据来源：全网规划<br>取值范围：<br>- ALL（全部）<br>- UeCtxTransfer（用户按上下文传递）<br>- GetSubNssaiData（获取签约切片）<br>- GetSubSmsData（获取签约短消息数据）<br>- Security（安全）<br>- UdmReg（UDM注册）<br>- UdmGetSub（获取UDM签约数据）<br>- UdmSub（UDM订阅）<br>- MobilityRestrict（移动接入限制）<br>- GetCtxFromMme（获取MME上下文）<br>- Accept（流程接受）<br>- NssaiSelect（切片选择）<br>- Other（其他）<br>- RESERV_STATUS1（预留状态1）<br>- RESERV_STATUS2（预留状态2）<br>- RESERV_STATUS3（预留状态3）<br>默认值：无<br>配置原则：<br>根据流程失败时所处的流程阶段来配置。当“流程类型”为非注册类型流程时，需要配置为“ALL”。 |
| SRCINNERCAUSE | 原始内部原因值 | 可选必选说明：该参数在"SCAUSETYPE"配置为"INNER_CAUSE"时为条件必选参数。<br>参数含义：该参数用于指定用户流程失败的原始内部原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| TCAUSE | 目标原因值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定下发到目标网元的映射后原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0319478931)

增加一个5G原因值映射配置，流程类型为初始注册，原始原因值为27，目标原因值为111，执行如下命令：

```
ADD NGCAUSEMAP: PROT=INIT_REG, SCAUSE=27, TCAUSE=111;
```
