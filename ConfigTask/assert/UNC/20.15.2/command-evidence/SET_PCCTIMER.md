# 命令证据包：SET PCCTIMER
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

![](设置PCC定时器（SET PCCTIMER）_09897082.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，执行命令配置超时时长不合理可能导致在超时场景下，激活响应的总时长过长，这可能会导致用户激活失败。在前期规划时，建议1：产品配置的等待右侧网元的最大时长小于产品ADD GTPCT3N3命令配置的T3N3时长
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。
- 在前期规划时，建议1：产品配置的等待右侧网元的最大时长小于产品ADD GTPCT3N3命令配置的T3N3时长及左侧（MME\SGSN等）的T3N3时长，避免右侧网元无响应造成激活响应的总时长过长。建议2：产品配置的等待右侧网元的最大时长小于产品SET SMCOMMTIMER命令配置的TPOLICY（等待策略响应定时器）的时长，避免右侧网元

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APPRETRYTIMES | 应用层重传次数 | local_planned | optional | 无 | 整数类型，取值范围为0～3。 |
| APPRETRYTIMEOUT | 应用层重传时间间隔（秒） | local_planned | optional | 无 | 整数类型，取值范围为0～10，单位是秒。 |
| HOLDINGTIME | 用户回滚后在线保持时长（分钟） | global_planned | optional | 无 | 整数类型，取值范围为0～1440，单位是分钟。 |
| ADJUSTRANGE | 随机延迟范围（分钟） | global_planned | optional | 无 | 整数类型，取值范围为0～60，单位是分钟。 |
| REVALIDHYSTMR | Revalidation重授权迟滞时间（秒） | local_planned | optional | 无 | 整数类型，取值范围为600～3600，单位是秒。 |
| REDIRECTHYSTMR | 重定向迟滞时间（秒） | local_planned | optional | 无 | 整数类型，取值范围为1～3600，单位是秒。 |
| SUPFEANEGOTMR | Supported-features协商定时器（分钟） | local_planned | optional | 无 | 整数类型，取值范围为1～43200，单位是分钟。 |
| DYNPCRFAGETMR | 动态PCRF老化时长（分钟） | local_planned | optional | 无 | 整数类型，取值范围为0～43200，单位是分钟。 |
| PENDRETRYTIMES | 事务等待重传次数 | 对端协商 | optional | 无 | 整数类型，取值范围为1～3，单位是次数。 |
| PENDRETRYTIMER | 事务等待重传间隔 (秒) | 对端协商 | optional | 无 | 整数类型，取值范围为1～3，单位是秒。 |
| FAILOVERALLTMR | Failover All-sessions定时器超时时长(分钟) | local_planned | optional | 无 | 整数类型，取值范围为1～60，单位是分钟。 |
| N7TXTIMERPARA | N7接口TxTimer定时器时长系数 | local_planned | optional | 无 | 整数类型，取值范围为1～32。 |
| REQDATATIMER | N7接口请求信息定时器 | 对端协商 | optional | 无 | 整数类型，取值范围为5～60，单位是秒。 |
| FASTHOLDINGTIME | 用户快速回滚后在线保持时长（分钟） | global_planned | optional | 无 | 整数类型，取值范围为0～1440，单位是分钟。 |
| FASTADJUSTRANGE | 快速回滚随机延迟范围（分钟） | global_planned | optional | 无 | 整数类型，取值范围为0～60，单位是分钟。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - [**ADD DIAMCONNGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路组/增加Diameter链路组（ADD DIAMCONNGRP）_09897261.md)
    > - [**ADD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)
    > - [**SET PCCTIMER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
    > - [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**ADD PCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)

**md：`WSFD-109101/实现原理_29056158.md`**
- 操作步骤上下文（±2 行原文）：
  L159:
    > 由于二次协商流程会导致Gx接口的信令交互增加，故 UNC 会在第一个会话建立过程中学习并存储对端PCRF的实际能力，即实际的协商结果，后续会话建立时，直接根据对端的实际能力发起协商，从而可以一次协商成功，提高协商成功率。在网络中实际部署时建议将本地配置的PCRF feature能力与PCRF实际支持的feature能力一致，减少二次协商过程。
    > 
    > 考虑到PCRF的升级场景， UNC 需定时清除本地缓存的对端PCRF能力，以保证新接入的用户可以发起全新的协商流程，从而学习到对端PCRF新的真实的支持能力。在 UNC 上可以使用 [**SET PCCTIMER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md) 命令配置本地缓存的定时器时长，或使用 [**RST PCCTIMER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/复位PCC定时器/复位PCC定时器（RST PCCTIMER）_09897075.md) 命令手动重启定时器清除本地缓存的对端能力信息。
    > 
    > 如果 UNC 动态协商功能使能，而PCRF不支持Supported-Features AVP，则PCRF会返回值为DIAMETER_AVP_UNSUPPORTED的Result-Code AVP，并且携带Failed-AVP AVP指示无法识别Supported-Features AVP，最终IP-CAN会话创建失败。

**md：`WSFD-109101/Gx Failover功能_31422950.md`**
- 数据规划表（该命令的参数行）：
  | [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md) | 应用层重传时间间隔（秒）（APPRETRYTIMEOUT） | 10 | 本端规划 | Tx定时器。 |
- 任务示例脚本（该命令行）：
  `SET PCCTIMER:APPRETRYTIMEOUT=10;`
- 操作步骤上下文（±2 行原文）：
  L61:
    >       [**SET MASTERPCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md)
    > 3. **可选：**配置PCC定时器的消息重传时间间隔。缺省使用默认值。
    >   [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
    > 4. 将指定的PCRF分组绑定到指定APN。
    >   [**ADD PCRFGRPBNDAPN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md)
  L106:
    > 3. 配置Tx定时器的时长。
    >   ```
    >   SET PCCTIMER:APPRETRYTIMEOUT=10;
    >   ```
    > 4. 将PCRF分组绑定到指定APN。

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 操作步骤上下文（±2 行原文）：
  L141:
    >       > - 根据PCRF的接收能力，通过设置“WAL”参数以限制向PCRF发送的消息数。
    >     b. 如果supported-features-negotiation功能使能，且需要定时或手工删除本地缓存的对端PCRF能力，需要配置动态协商定时器的时长，缺省使用默认值。
    >       [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
    >     c. 配置PCRF地址信息。
    >       [**ADD DIAMPEERADDR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)

**md：`WSFD-109101/配置异常场景数据_31422947.md`**
- 操作步骤上下文（±2 行原文）：
  L76:
    >       [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)
    >     3. **可选：**配置PCC用户回滚后的在线保持时长，缺省使用默认值。
    >       [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
    >     4. 配置PCC Template中GGSN/PGW-C无法与PCRF进行正常交互时对PCC用户的处理方式以及PCC用户回滚后的在线保持时长。若不配置，GGSN/PGW-C默认继承全局配置。
    >       [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)
  L88:
    >       [**ADD RESULTCODECTRL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)
    >     4. **可选：**如果设置GGSN/PGW-C收到直连对端返回码后执行FAILOVERALL动作，可配置FAILOVERALL的持续时长，缺省使用默认值。
    >       [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
    >       > **说明**
    >       > GGSN/PGW-C根据指定返回码对所有用户执行failover动作后，已在线和新激活的用户使用备PCRF进行交互。当Failover All-sessions定时器到达后，如果主PCRF可用，新激活用户将使用主PCRF进行交互，已在线用户仍使用备PCRF进行交互，否则均使用备PCRF进行交互。

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L66:
    > **[LST PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/查询PCC故障处理（LST PCCFAILACTION）_33684768.md)**
    > 
    > **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**
    > 
    > **[LST PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/查询PCC定时器（LST PCCTIMER）_96782686.md)**

**md：`WSFD-201207/实现原理（N7接口）_85304236.md`**
- 操作步骤上下文（±2 行原文）：
  L76:
    >   | 备SCP回复如下结果码和Protocol or application Error组合：<br>- 500 NF_SERVICE_FAILOVER<br>- 504 TARGET_NF_NOT_REACHABLE<br>- 502 NF_DISCOVERY_ERROR<br>- 502 MAX_SCP_HOPS_REACHED | - **[ADD RESULTCODECTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)**命令对应N7返回码的“Initial流程处理动作（INITACTION）”参数值为“FAILOVER”<br>- 用户使用的PCC模板（**[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)**）中的“N7 Failover功能开关（N7FAILOVERSW）”参数值为“ENABLE” | 会话回滚为本地PCC会话，使用本地配置的规则，进入PCF Bypass状态。<br>如果<br>**[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)**<br>或者<br>**[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**<br>配置了Holding Time参数，SMF根据软参<br>[DWORD519 Bit9](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/DWORD519 Bit9控制激活流程查询PCF失败发生回滚时，HoldingTime功能是否生效_97903713.md)<br>配置决定是否启动Holding Time定时器。 |
    >   | 备SCP回复其它异常结果码 | - **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)**命令对应的N7返回码和故障码对应的Protocol or application Error信息组合的“Initial流程处理动作（INITACTION）”参数值为“FAILOVER”<br>- **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**命令的“SCP故障重选开关（SCPFAILOVERSW）”参数值为“SCP_FAILOVER”<br>- **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)**命令的“无语音专载时的故障非预期Bypass场景的异常处理动作（ACTNODEDBEARER）”参数值为“TERMINATE” | 会话激活失败。 |
    >   **步骤** **7** ：如果SMF将用户回滚为本地PCC用户，标识用户进入PCF Bypass状态。如果 **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** 或者 **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** 配置了Holding Time参数，SMF根据软参 [DWORD519 Bit9](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/DWORD519 Bit9控制激活流程查询PCF失败发生回滚时，HoldingTime功能是否生效_97903713.md) 配置决定是否启动Holding Time定时器。
    >   **步骤** **8** ：SMF选择UPF。
    >   **步骤** **9-10** ：SMF给UPF发送PFCP Session Establishment Request消息请求建立新的PFCP会话上下文，提供用于该PDU会话的数据监测，CN隧道信息，用于语音专有QoS Flow\专有承载创建的静态PCC策略等。
  L124:
    >   | 备SCP回复如下结果码和Protocol or application Error组合：<br>- 500 NF_SERVICE_FAILOVER<br>- 504 TARGET_NF_NOT_REACHABLE<br>- 502 NF_DISCOVERY_ERROR<br>- 502 MAX_SCP_HOPS_REACHED | **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)**<br>命令对应的N7返回码和故障码对应的Protocol or application Error信息组合的<br>“Update流程处理动作（UPDATEACTION）”<br>参数值为<br>“INHERIT_PCC”<br>，并且<br>“Update流程回滚后使能Holding-Time（UPDHOLDTMSW）”<br>参数值为<br>“ENABLE” | 会话回滚为本地PCC会话，继续使用PCF下发的规则，会话进入PCF Bypass状态。<br>如果<br>**[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)**<br>或者<br>**[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**<br>配置了Holding Time参数，SMF启动Holding Time定时器。 |
    >   | 备SCP回复其它异常结果码 | - **[ADD RESULTCODESCP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加配置MODELC_D组网的SCP原因码控制（ADD RESULTCODESCP）_81322858.md)**命令对应的N7返回码和故障码对应的Protocol or application Error信息组合的“Update流程处理动作（UPDATEACTION）”参数值为“FAILOVER”<br>- **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**命令的“SCP故障重选开关（SCPFAILOVERSW）”参数值为“SCP_FAILOVER”<br>- **[SET IMSBYPASSFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/设置语音PCF_PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）_49496669.md)**命令的“无语音专载时的故障非预期Bypass场景的异常处理动作（ACTNODEDBEARER）”参数值为“TERMINATE”，“存在语音专载时的更新流程故障非预期Bypass场景的异常处理动作（ACTWITDEDBEARER）”参数值为“FASTROLLBACK”，并且“存在语音专载时更新流程故障回滚为Local PCC用户类型（FAILLOCPCC）”参数值为“INHERIT_PCC” | 当用户存在语音会话时，当前会话回滚为本地PCC会话，继续使用PCF下发的规则，会话进入PCF Bypass状态。<br>如果<br>**[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**<br>配置了用户快速回滚后在线保持时长参数，SMF启动Holding Time定时器。<br>当用户不存在语音会话时，去激活当前会话。 |
    >   **步骤** **4** ：如果SMF将用户回滚为本地PCC用户，标识用户进入PCF Bypass状态。如果 **[ADD PCCTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md)** 或者 **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** 配置了Holding Time参数，启动Holding Time定时器。
    >   **步骤** **5** ：SMF发送Nsmf_PDUSession_UpdateSmContext Response给AMF。
    >   **步骤** **6** ：（可选）QoS改变需要通知(R)AN侧时，进行该流程，(R)AN侧接受策略修改。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（Gx接口）_60552093.md`**
- 数据规划表（该命令的参数行）：
  | **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** | 用户回滚后在线保持时长（分钟）（HOLDINGTIME） | 30 | 本端规划 | 配置全局Holding Time和Fast Holding Time。 |
  | **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** | 随机延迟范围（分钟）（ADJUSTRANGE） | 10 | 本端规划 | 配置全局Holding Time和Fast Holding Time。 |
  | **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** | 用户快速回滚后在线保持时长（分钟）（FASTHOLDINGTIME） | 10 | 全网规划 | 配置全局Holding Time和Fast Holding Time。 |
  | **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** | 快速随机延迟范围（分钟）（FASTADJUSTRANGE） | 5 | 全网规划 | 配置全局Holding Time和Fast Holding Time。 |
- 任务示例脚本（该命令行）：
  `SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10, FASTHOLDINGTIME=10, FASTADJUSTRANGE=5;`
  `SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10, FASTHOLDINGTIME=10, FASTADJUSTRANGE=5;`
- 操作步骤上下文（±2 行原文）：
  L256:
    >       **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**
    >     b. 配置全局Holding Time。
    >       **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**
    >     c. 基于PCC模板配置故障处理动作、failover开关和Holding Time。
    >       > **说明**
  L390:
    > 
    >       ```
    >       SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10, FASTHOLDINGTIME=10, FASTADJUSTRANGE=5;
    >       ```
    >       //基于存在的PCC模板配置故障处理动作、failover开关和Holding Time。
  L504:
    > 
    >       ```
    >       SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10, FASTHOLDINGTIME=10, FASTADJUSTRANGE=5;
    >       ```
    >       //基于存在的PCC模板配置故障处理动作、failover开关和Holding Time。

**md：`WSFD-201207/激活语音PCF_PCRF故障Bypass（N7接口）_32852169.md`**
- 数据规划表（该命令的参数行）：
  | **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** | 用户回滚后在线保持时长（分钟）（HOLDINGTIME） | 30 | 本端规划 | 配置全局Holding Time。 |
  | **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)** | 随机延迟范围（分钟）（ADJUSTRANGE） | 10 | 本端规划 | 配置全局Holding Time。 |
- 任务示例脚本（该命令行）：
  `SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;`
  `SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;`
  `SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;`
  `SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;`
  `SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;`
  `SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;`
- 操作步骤上下文（±2 行原文）：
  L277:
    >       **[SET PCCFAILACTION](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)**
    >     c. 配置全局Holding Time。
    >       **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**
    >     d. 基于PCC模板配置故障处理动作、failover开关和Holding Time。
    >       > **说明**
  L424:
    > 
    >             ```
    >             SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;
    >             ```
    >             //基于存在的PCC模板配置故障处理动作、failover开关和Holding Time。
  L476:
    > 
    >             ```
    >             SET PCCTIMER:HOLDINGTIME=30, ADJUSTRANGE=10;
    >             ```
    >             //基于存在的PCC模板配置故障处理动作、failover开关和Holding Time。

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L31:
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - **[ADD PCRF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)**
    > - **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**
    > 
    > #### [告警](#ZH-CN_CONCEPT_0229315046)

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 操作步骤上下文（±2 行原文）：
  L141:
    >       > 如果PCRF未配置域信息，则需要在本步骤中进行配置。
    >     b. **可选：**配置动态PCRF主机列表表项老化时长。
    >       **[SET PCCTIMER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)**
    > 8. 配置SCTP端点信息。
    >   **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**

## ④ 自动比对
- 命令真相参数（15）：['ADJUSTRANGE', 'APPRETRYTIMEOUT', 'APPRETRYTIMES', 'DYNPCRFAGETMR', 'FAILOVERALLTMR', 'FASTADJUSTRANGE', 'FASTHOLDINGTIME', 'HOLDINGTIME', 'N7TXTIMERPARA', 'PENDRETRYTIMER', 'PENDRETRYTIMES', 'REDIRECTHYSTMR', 'REQDATATIMER', 'REVALIDHYSTMR', 'SUPFEANEGOTMR']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 5, '全网规划': 2}（多值→atom 应考虑 decision_driven）
