# 显示信令失败统计的结果（DSP SESSIONMSGSTAT）

- [命令功能](#ZH-CN_CONCEPT_0000206934254378__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206934254378__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206934254378__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206934254378__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206934254378__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000206934254378__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206934254378)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于显示信令失败统计的结果。

#### [注意事项](#ZH-CN_CONCEPT_0000206934254378)

激活信令的部分场景的失败获取不到角色。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206934254378)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206934254378)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：查询方式。<br>数据来源：本端规划<br>取值范围：<br>- WHOLESTAT：查询信令成功率等整体的统计信息。<br>- DETAILSTAT：查询具体协议的失败信息。<br>默认值：WHOLESTAT<br>配置原则：无 |
| PODNAME | 名称 | 可选必选说明：可选参数<br>参数含义：Pod名称。<br>数据来源：本端规划<br>取值范围：字符串，输入长度范围为1～64。<br>默认值：无<br>配置原则：无 |
| FAILMSGTYPE | 失败的消息类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QUERYTYPE”配置为“DETAILSTAT”时为可选参数。<br>参数含义：查询的消息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SESS_CRT_FAIL：激活失败消息。<br>- SESS_DEL_FAIL：去活失败消息。<br>- SESS_MOD_FAIL：更新失败消息。<br>- SESS_RPT_DEA：主动去活消息。<br>默认值：SESS_CRT_FAIL<br>配置原则：无 |
| PROTOCALCAUSE | 协议失败原因值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“FAILMSGTYPE”配置为“SESS_CRT_FAIL”、“SESS_DEL_FAIL”、“SESS_MOD_FAIL” 或 “SESS_RPT_DEA”时为可选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“QUERYTYPE”配置为“DETAILSTAT”时为可选参数。<br>参数含义：协议失败的原因值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- more-usage-report-to-send：需要发送更多的使用报告。<br>- request-partially-accepted：请求部分被接受。<br>- request-rejected：请求被拒绝。<br>- session-context-not-found：会话上下文未找到。<br>- mandatory-ie-missing：缺少必选的信元。<br>- conditional-ie-missing：缺少条件可选信元。<br>- invalid-length：长度无效。<br>- mandatory-ie-incorrect：必选信元不正确。<br>- invalid-forwarding-policy：转发策略无效。<br>- invalid-fteid-allocation-option：F-TEID分配选项无效。<br>- no-established-pfcp-association：没有建立的PFCP偶联。<br>- rule-creation-or-modification-failure：规则创建或修改失败。<br>- pfcp-entity-in-congestion：PFCP实体处于拥塞状态。<br>- no-resources-available：没有可用资源。<br>- service-not-supported：不支持的服务。<br>- system-failure：系统故障。<br>- l2tp-tunnel-establishment-failure：L2TP隧道建立失败。<br>- l2tp-session-establishment-failure：L2TP会话建立失败。<br>- l2tp-tunnel-release：L2TP隧道释放。<br>- l2tp-session-release：L2TP会话释放。<br>- ether-group-not-found：以太网组未找到。<br>- ether-ngbindvxlan-not-config：以太网NGBINDVXLAN未配置。<br>- inner-drop：内部丢弃。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206934254378)

- 基于所有协议消息的查询：
  ```
  DSP SESSIONMSGSTAT: QUERYTYPE=WHOLESTAT, PODNAME="ssg-pod-1";
  ```
  ```

  RETCODE = 0  操作成功.  

  结果如下
  -------------------------- 
  结果  =   
  名称              角色    消息类型                     成功率(%)  请求次数（10分钟）  失败次数（10分钟）  失败次数（累计）
  ssg-pod-1         ALL     N4_Send_Establishment_Req    99         1                  1                  100
  ssg-pod-1         ALL     N4_Send_Modification_Req     99         1                  1                  100
  ssg-pod-1         ALL     N4_Recieve_Delete_Req        100        1                  1                  100
  ssg-pod-1         ALL     N4_Send_Delete_Report        98         0                  0                  0
  ssg-pod-1         UPF     N4_Send_Establishment_Req    99         1                  1                  100
  ssg-pod-1         UPF     N4_Send_Modification_Req     99         1                  1                  100
  ssg-pod-1         UPF     N4_Recieve_Delete_Req        100        1                  1                  100
  ssg-pod-1         UPF     N4_Send_Delete_Report        98         0                  0                  0
  ssg-pod-1         SPGW    N4_Send_Establishment_Req    99         1                  1                  100
  ssg-pod-1         SPGW    N4_Send_Modification_Req     99         1                  1                  100
  ssg-pod-1         SPGW    N4_Recieve_Delete_Req        100        1                  1                  100
  ssg-pod-1         SPGW    N4_Send_Delete_Report        98         0                  0                  0
  ssg-pod-1         PGW     N4_Send_Establishment_Req    99         1                  1                  100
  ssg-pod-1         PGW     N4_Send_Modification_Req     99         1                  1                  100
  ssg-pod-1         PGW     N4_Recieve_Delete_Req        100        1                  1                  100
  ssg-pod-1         PGW     N4_Send_Delete_Report        98         0                  0                  0
  ssg-pod-1         SGW     N4_Send_Establishment_Req    99         1                  1                  100
  ssg-pod-1         SGW     N4_Send_Modification_Req     99         1                  1                  100
  ssg-pod-1         SGW     N4_Recieve_Delete_Req        100        1                  1                  100
  ssg-pod-1         SGW     N4_Send_Delete_Report        98         0                  0                  0
  ssg-pod-1         GGSN    N4_Send_Establishment_Req    99         1                  1                  100
  ssg-pod-1         GGSN    N4_Send_Modification_Req     99         1                  1                  100
  ssg-pod-1         GGSN    N4_Recieve_Delete_Req        100        1                  1                  100
  ssg-pod-1         GGSN    N4_Send_Delete_Report        98         0                  0                  0

  (结果个数 = 1)

  ---    END
  ```
- 不指定具体消息类型：
  ```
  DSP SESSIONMSGSTAT: QUERYTYPE=DETAILSTAT, PODNAME="ssg-pod-1";
  ```
  ```

  RETCODE = 0  操作成功.  

  结果如下
  -------------------------- 
  结果  =   
  名称             消息类型                               失败次数（5分钟）    协议失败原因值
  ssg-pod-1        N4_Send_Establishment_Req              80                  mandatory-ie-missing(66)
  ssg-pod-1        N4_Send_Establishment_Req              80                  system-failure(77)
  ssg-pod-1        N4_Send_Delete_Report                  80                  user-plane-N4_Recieve_Delete_Req-request
  ssg-pod-1        N4_Send_Modification_Req               80                  mandatory-ie-missing(66)
  ssg-pod-1        N4_Recieve_Delete_Req                  1                   system-failure(77)

  (结果个数 = 1)

  ---    END
  ```
- 指定消息类型：
  ```
  DSP SESSIONMSGSTAT: QUERYTYPE=DETAILSTAT, FAILMSGTYPE=SESS_CRT_FAIL, PODNAME="ssg-pod-1";
  ```
  ```

  RETCODE = 0  操作成功.  

  结果如下
  -------------------------- 
  结果  =   
  名称            消息类型                    失败次数（5分钟）	 协议失败原因值           	    内部失败原因值
  ssg-pod-1	    N4_Send_Establishment_Req  	80	                mandatory-ie-missing(66)	  Manadary ie node-id is error.
  ssg-pod-1	    N4_Send_Establishment_Req  	80	                system-failure(77)	          lck nf!

  (结果个数 = 1)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0000206934254378)

| 输出项名称 | 输出项解释 |
| --- | --- |
| PODNAME | POD名称。 |
| ROLES | 角色。 |
| MSGTYPE | 消息类型。 |
| INTERNALCAUSE | 内部原因值。 |
| SUCCESSRATE | 成功率。 |
| MIN_NUMREQUESTS | 五分钟内请求次数。 |
| MIN_FAILURES | 五分钟内失败次数。 |
| NUMFAILURES | 失败次数累计值。 |
| PROTOCALCAUSE | 协议原因值。 |
