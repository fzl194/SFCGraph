# WSFD-102702 EPS Fallback 参考信息

- [命令](#ZH-CN_TOPIC_0182764866__1.3.1.1)
- [告警](#ZH-CN_TOPIC_0182764866__1.3.2.1)
- [软参](#ZH-CN_TOPIC_0182764866__1.3.3.1)
- [测量指标](#ZH-CN_TOPIC_0182764866__1.3.4.1)

#### [命令](#ZH-CN_TOPIC_0182764866)

本特性相关的MML命令如下：

- **[**SET NGIMSVOPS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/VoPS管理/设置VoPS配置（SET NGIMSVOPS）_09653214.md)**
- **[**LST NGIMSVOPS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/5G 语音业务管理/VoPS管理/查询VoPS配置（LST NGIMSVOPS）_09653054.md)**
- **[**DSP PDUSESSION**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**
- **[**SET APNIMSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/设置APN的IMS属性（SET APNIMSATTR）_33845576.md)**
- **[**LST APNIMSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/查询APN的IMS属性（LST APNIMSATTR）_09653158.md)**
- **[**ADD PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/增加P-CSCF组配置（ADD PCSCFGROUP）_09653619.md)**
- **[**RMV PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/删除P-CSCF组配置（RMV PCSCFGROUP）_09651437.md)**
- **[**LST PCSCFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组/查询P-CSCF组配置（LST PCSCFGROUP）_09654405.md)**
- **[**ADD PCSCFIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/增加P-CSCF地址配置（ADD PCSCFIP）_09651572.md)**
- **[**RMV PCSCFIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/删除P-CSCF地址配置（RMV PCSCFIP）_09653290.md)**
- **[**LST PCSCFIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/查询P-CSCF地址配置（LST PCSCFIP）_09653781.md)**
- **[ADD IMSIMSISDNSEG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)**
- **[**MOD IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/修改IMSI和MSISDN号段（MOD IMSIMSISDNSEG）_09897129.md)**
- **[**LST IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/查询IMSI和MSISDN号段（LST IMSIMSISDNSEG）_09897131.md)**
- **[**LCK IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/锁定IMSI和MSISDN号段（LCK IMSIMSISDNSEG）_09897132.md)**
- **[**RMV IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/删除IMSI和MSISDN号段（RMV IMSIMSISDNSEG）_09897130.md)**
- **[**ADD PCSCFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组与APN关联关系/增加APN和P-CSCF组关联关系（ADD PCSCFGRPBNDAPN）_09653091.md)**
- **[**RMV PCSCFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组与APN关联关系/删除APN和P-CSCF组关联关系（RMV PCSCFGRPBNDAPN）_09651444.md)**
- **[**MOD PCSCFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组与APN关联关系/修改APN和P-CSCF组关联关系（MOD PCSCFGRPBNDAPN）_09652533.md)**
- **[**LST PCSCFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF组与APN关联关系/查询APN和P-CSCF组关联关系（LST PCSCFGRPBNDAPN）_09652537.md)**
- **[**SET NGAPCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/N2接口管理/NGAP兼容性参数管理/设置NGAP兼容性参数（SET NGAPCMPT）_09652644.md)**

#### [告警](#ZH-CN_TOPIC_0182764866)

本特性无相关告警。

#### [软参](#ZH-CN_TOPIC_0182764866)

**[DWORD1016 BIT12 5G DDN流程中，SMF收到AMF发送的UpdateSMContextRequest消息携带AN_NOT_RESPONDING原因值时，是否重新发送N1N2TransferRequest尝试激活用户面](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/会话管理/DWORD1016 BIT12 5G DDN流程中，SMF收到AMF发送的UpdateSMContex_f7e9e60f_42462280.md)**

**[DWORD1016 BIT13 控制在特定场景下SMF对主锚点UPF上PFCP会话缺省承载下行FAR的处理方式](../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/会话管理/DWORD1016 BIT13 控制在特定场景下SMF对主锚点UPF上PFCP会话缺省承载下行FAR的处理方式_84623079.md)**

#### [测量指标](#ZH-CN_TOPIC_0182764866)

本特性相关的测量指标如下（指标组中和IMS相关的指标）：

- **[1929458390 SMF/PGW-C统计EPS Fallback流程请求次数](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/SMF 4G_5G互操作流程/1929458390 SMF_PGW-C统计EPS Fallback流程请求次数_10377816.md)**
- **[1929458391 SMF/PGW-C统计EPS Fallback流程成功次数](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/SMF 4G_5G互操作流程/1929458391 SMF_PGW-C统计EPS Fallback流程成功次数_10377817.md)**
- **[KPI](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/KPI_23880629.md)**
- **[PGW-C业务层S5/S8接口IMS流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SGW_PGW_GGSN GTP会话管理/PGW-C业务层S5_S8接口IMS流程_10378044.md)**
- **[SMF 4G/5G互操作流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/SMF 4G_5G互操作流程_10377802.md)**
- **[SMF 5G会话管理流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/SMF 5G会话管理流程_25945953.md)**
- **[SMF 5G会话管理失败流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/SMF 5G会话管理失败流程_10377828.md)**
- **[SMF 5G会话资源](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/SMF 5G会话资源_10377768.md)**
- **[SPGW-C合一形态业务层S11/S4接口IMS流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SGW_PGW_GGSN GTP会话管理/SPGW-C合一形态业务层S11_S4接口IMS流程_15047483.md)**
- **[指定DNN的SMF 5G会话资源](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/指定DNN的SMF 5G会话资源_10377782.md)**
- **[指定DNN的SMF 5G会话管理流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/指定DNN的SMF 5G会话管理流程_10377754.md)**
- **[指定S-NSSAI的SMF 5G会话资源](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/指定S-NSSAI的SMF 5G会话资源_10377775.md)**
- **[指定S-NSSAI的SMF 5G会话管理失败流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/指定S-NSSAI的SMF 5G会话管理失败流程_10377841.md)**
- **[指定S-NSSAI的SMF 5G会话管理流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/指定S-NSSAI的SMF 5G会话管理流程_10377740.md)**
- **[N16SMF 5G会话资源](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16SMF 5G会话资源_44044872.md)**
- **[N16SMF 5G会话管理流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16SMF 5G会话管理流程_44044788.md)**
- **[N16SMF 5G会话管理失败流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16SMF 5G会话管理失败流程_44044919.md)**
- **[指定DNN的N16SMF 5G会话资源](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/指定DNN的N16SMF 5G会话资源_44044898.md)**
- **[指定DNN的N16SMF 5G会话管理流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/指定DNN的N16SMF 5G会话管理流程_44044845.md)**
- **[指定S-NSSAI的N16SMF 5G会话资源](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/指定S-NSSAI的N16SMF 5G会话资源_44044891.md)**
- **[指定S-NSSAI的N16SMF 5G会话管理流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/指定S-NSSAI的N16SMF 5G会话管理流程_44044818.md)**
- **[指定S-NSSAI的N16SMF 5G会话管理失败流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/指定S-NSSAI的N16SMF 5G会话管理失败流程_44044930.md)**
- **[指定DNN的SMF 5G会话管理失败流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/指定DNN的SMF 5G会话管理失败流程_10377854.md)**
- **[指定DNN的N16SMF 5G会话管理失败流程](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/指定DNN的N16SMF 5G会话管理失败流程_44044941.md)**
- **[N7接口返回码测量](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/服务化接口测量/N7接口返回码测量_36502246.md)**
- **[1929512201 PGW-C统计N16aSMF EPS Fallback流程请求次数](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512201 PGW-C统计N16aSMF EPS Fallback流程请求次数_34297614.md)**
- **[1929512197 N16aSMF/PGW-C统计EPS Fallback流程成功次数](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/KPI_18600245.md)**
- **[1929512198 N16aSMF/PGW-C统计EPS Fallback流程失败次数](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512198 N16aSMF_PGW-C统计EPS Fallback流程失败次数_34776188.md)**
- **[1929512199 N16aSMF/PGW-C统计EPS Fallback流程超时次数](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512199 N16aSMF_PGW-C统计EPS Fallback流程超时次数_38057197.md)**
- **[1929512200 N16aSMF/PGW-C统计EPS Fallback流程失败次数-取消](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512200 N16aSMF_PGW-C统计EPS Fallback流程失败次数-取消_37935309.md)**
- **[1929512201 PGW-C统计N16aSMF EPS Fallback流程请求次数](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512201 PGW-C统计N16aSMF EPS Fallback流程请求次数_34297614.md)**
- **[1929512197 N16aSMF/PGW-C统计EPS Fallback流程成功次数](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512197 N16aSMF_PGW-C统计EPS Fallback流程成功次数_38215249.md)**
- **[1929512203 SPGW-C统计N16aSMF EPS Fallback流程请求次数](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512197 N16aSMF_PGW-C统计EPS Fallback流程成功次数_38215249.md)**
- **[1929512204 SPGW-C统计N16aSMF EPS Fallback流程成功次数](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512204 SPGW-C统计N16aSMF EPS Fallback流程成功次数_35016014.md)**
- **[1929512205 SPGW-C统计N16aSMF EPS Fallback流程失败次数-超时](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512205 SPGW-C统计N16aSMF EPS Fallback流程失败次数-超时_38215251.md)**
- **[1929512206 SPGW-C统计N16aSMF EPS Fallback流程失败次数-取消](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512206 SPGW-C统计N16aSMF EPS Fallback流程失败次数-取消_34776190.md)**
- **[1929512207 SPGW-C/PGW-C统计N16aSMF EPS Fallback流程（等待EPS首消息阶段）总时长](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512207 SPGW-C_PGW-C统计N16aSMF EPS Fallback流程（等待E_1ce3dc5d_38057199.md)**
- **[1929512208 SPGW-C/PGW-C统计N16aSMF EPS Fallback流程（等待EPS首消息阶段）平均时长](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512208 SPGW-C_PGW-C统计N16aSMF EPS Fallback流程（等待E_bc6924d9_37935311.md)**
- **[1929512209 N16aSMF EPS Fallback流程总时长](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512208 SPGW-C_PGW-C统计N16aSMF EPS Fallback流程（等待E_bc6924d9_37935311.md)**
- **[1929512210 N16aSMF EPS Fallback流程平均时长](../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/SMF 会话管理/N16aSMF 4G_5G互操作流程/1929512210 N16aSMF EPS Fallback流程平均时长_34537314.md)**
