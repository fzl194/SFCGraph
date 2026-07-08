# 查询GGSN-C原因值控制参数（LST GGSNCAUSECTRL）

- [命令功能](#ZH-CN_MMLREF_0225120885__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0225120885__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0225120885__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0225120885__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0225120885__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0225120885)

**适用NF：GGSN**

该命令用于查询GGSN-C的原因值控制参数。

## [注意事项](#ZH-CN_MMLREF_0225120885)

无

#### [操作用户权限](#ZH-CN_MMLREF_0225120885)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0225120885)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCEDURETYPE | 流程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流程类型，要根据场景来配置相应的流程。<br>数据来源：本端规划<br>取值范围：<br>- CRT_PDP_PROC（创建PDP流程）<br>- UPD_PDP_PROC（更新PDP流程）<br>默认值：无<br>配置原则：无 |
| CAUSESOURCE | 异常来源 | 可选必选说明：可选参数<br>参数含义：该参数用于描述发生异常的来源。<br>数据来源：本端规划<br>取值范围：<br>- UPF（UPF）<br>- POLICY_PCRF（PCRF策略）<br>- CHG_3GPP（3GPP计费）<br>- RADIUS_AUTH（Radius鉴权）<br>- INNER（内部异常）<br>- RADIUS_CHG（Radius计费）<br>- POLICY_PCF（PCF策略）<br>- CHF_3GPP（3GPP CHF）<br>默认值：无<br>配置原则：<br>POLICY_PCF以及CHF_3GPP网元类型仅在2G用户下生效。 |

## [使用实例](#ZH-CN_MMLREF_0225120885)

- 查询全部GGSN-C的原因值控制参数：
  ```
  %%LST GGSNCAUSECTRL:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  流程类型     异常来源  NE拒绝导致流程拒绝原因值组号  响应超时导致流程拒绝的GTPv1原因值  APN锁定或整机锁定导致流程拒绝的GTPv1原因值  IP地址耗尽导致流程拒绝的GTPv1原因值  发送消息流控导致流程拒绝的GTPv1原因值  承载受限原因值   CPU过载原因值

  创建PDP流程  PCRF策略  123                           10                                 NULL                              NULL                                 #199 无资源可用                        #199 无资源可用  #199 无资源可用
  更新PDP流程  内部异常  0                             0                                  #199 无资源可用                   #211 无动态PDP地址                   NULL                                   #199 无资源可用  #199 无资源可用
  (结果个数 = 2)

  ---    END
  ```
- 查询创建PDP流程的原因值控制参数：
  ```
  %%LST GGSNCAUSECTRL: PROCEDURETYPE=CRT_PDP_PROC;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                                    流程类型  =  创建PDP流程
                                    异常来源  =  UPF
                NE拒绝导致流程拒绝原因值组号  =  0
           响应超时导致流程拒绝的GTPv1原因值  =  204
  APN锁定或整机锁定导致流程拒绝的GTPv1原因值  =  NULL
         IP地址耗尽导致流程拒绝的GTPv1原因值  =  NULL
       发送消息流控导致流程拒绝的GTPv1原因值  =  NULL
                              承载受限原因值  =  #199 无资源可用
                               CPU过载原因值  =  #199 无资源可用
  (结果个数 = 1)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0225120885)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 流程类型 | 该参数用于指定流程类型，要根据场景来配置相应的流程。 |
| 异常来源 | 该参数用于描述发生异常的来源。 |
| NE拒绝导致流程拒绝原因值组号 | 该参数用于设置因周边网元返回拒绝而导致流程拒绝时，下发给左侧网元（SGSN）的GTPv1消息中拒绝原因值采用的映射规则。 |
| 响应超时导致流程拒绝的GTPv1原因值 | 该参数用于设置因周边网元响应超时而导致流程拒绝时，下发给左侧网元（SGSN）的GTPv1消息中的拒绝原因值。 |
| APN锁定或整机锁定导致流程拒绝的GTPv1原因值 | 该参数用于指示因为APN锁定或整机锁定导致创建PDP流程失败，发送的Create PDP Context Response消息中携带的GTPv1原因值。 |
| IP地址耗尽导致流程拒绝的GTPv1原因值 | 该参数用于指示因为IP地址耗尽导致创建PDP流程失败，发送的Create PDP Context Response消息中携带的GTPv1原因值。 |
| 发送消息流控导致流程拒绝的GTPv1原因值 | 该参数用于指示因为发送消息流控导致创建PDP流程失败，发送的Create PDP Context Response消息中携带的GTPv1原因值。 |
| 承载受限原因值 | 该参数用来控制承载受限导致流程拒绝的原因值。 |
| CPU过载原因值 | 该参数用来控制CPU过载或APN流控导致流程拒绝的原因值。 |
