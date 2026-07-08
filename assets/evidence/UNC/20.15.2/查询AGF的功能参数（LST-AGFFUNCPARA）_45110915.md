# 查询AGF的功能参数（LST AGFFUNCPARA）

- [命令功能](#ZH-CN_MMLREF_0245110915__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0245110915__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0245110915__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0245110915__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0245110915__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0245110915)

**适用NF：NCG**

该命令用于查询AGF的功能参数。

## [注意事项](#ZH-CN_MMLREF_0245110915)

无

#### [操作用户权限](#ZH-CN_MMLREF_0245110915)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0245110915)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSRETRYCNT | 计费消息重发次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NCG等待OCS计费响应超时重发次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1。<br>默认值：无<br>配置原则：无 |
| OCSDISCPLCY | OCS选择策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定选择OCS时使用的参数。<br>数据来源：本端规划<br>取值范围：<br>- “SUPI（SUPI）”：根据SUPI选择OCS<br>- “GPSI（GPSI）”：根据GPSI选择OCS<br>- “DNN（DNN）”：根据DNN选择OCS<br>默认值：无<br>配置原则：<br>OCS选择策略选项中至少选择一个。 |
| CDFIPKGPLCY | CDF I包抄送策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CDF I包抄送策略。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：<br>FALSE表示不抄送。<br>TRUE表示抄送。 |
| QBCCHGSWITCH | H-CHF QBC计费开关 | 可选必选说明：可选参数<br>参数含义：是否开启H-CHF QBC计费模式。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| VSMFJUDGEMODE | V-SMF判断模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定V-SMF的判断模式。<br>数据来源：本端规划<br>取值范围：<br>- HUAWEIQBCINDICATION_MODE（根据huaweiQBCIndication判断）<br>- NETWORKFUNCTIONALITY_MODE（根据networkFunctionality判断）<br>- PLMN_MODE（根据plmn判断）<br>默认值：无<br>配置原则：无 |
| OCSRSPFOFHPLCY | 是否忽略OCS的Failover策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否忽略OCS的Failover策略。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：<br>FALSE表示向前端网元透传OCS响应中sessionFailover与failureHandling值。<br>TRUE表示忽略OCS响应中sessionFailover为FAILOVER_NOT_SUPPORTED的值，固定填为FAILOVER_SUPPORTED；忽略OCS响应中failureHandling为TERMINATE或RETRY_AND_TERMINATE的值，固定填为CONTINUE。 |
| SMSFCHGSWITCH | SMSF计费开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启SMSF计费模式。<br>数据来源：全网规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0245110915)

查询计费重发次数为1的记录：

```
LST AGFFUNCPARA: OCSRETRYCNT=1;
RETCODE = 0  操作成功

结果如下
--------
   计费消息重发次数  =  1
        OCS选择策略  =  SUPI
    CDF I包抄送策略  =  是
  H-CHF QBC计费开关  =  否
      V-SMF判断模式  =  根据huaweiQBCIndication判断
是否忽略OCS的Failover策略 = 否
SMSF计费开关 = 否
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0245110915)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 计费消息重发次数 | 该参数用于指定NCG等待OCS计费响应超时重发次数。 |
| OCS选择策略 | 该参数用于指定选择OCS时使用的参数。 |
| CDF I包抄送策略 | 该参数用于指定CDF I包抄送策略。 |
| H-CHF QBC计费开关 | 是否开启H-CHF QBC计费模式。 |
| V-SMF判断模式 | 该参数用于指定V-SMF的判断模式。 |
| 是否忽略OCS的Failover策略 | 该参数用于指定是否忽略OCS的Failover策略。 |
| SMSF计费开关 | 该参数用于指定是否开启SMSF计费模式。 |
