# 设置PDP过滤功能参数(SET PDPFILTERCTL)

- [命令功能](#ZH-CN_MMLREF_0000001126145688__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145688__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145688__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145688__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145688__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145688__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145688)

**适用网元：SGSN**

该命令用于设置PDP过滤功能相关参数，PDP过滤功能是指当用户通过RAU或者RELOCATION流程从LTE网络迁移到GU网络后，SGSN主动识别出低优先级的PDP，通过PDP去激活流程删除旧侧LTE网络专有承载对应的PDP以及低优先级的PDP。当运营商GU网络无线侧PDP能力不足时使用。

#### [注意事项](#ZH-CN_MMLREF_0000001126145688)

- 该命令执行后立即生效。
- PDP过滤功能开启后，PDP的优先级取决于对应APN的优先级。APN优先级配置参见[**ADD PDPFILTERAPN**](增加APN优先级配置(ADD PDPFILTERAPN)_26305498.md)命令。
- 此命令功能只适用于Gn/Gp组网形式。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145688)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145688)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145688)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 过滤开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否开启PDP过滤功能。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>系统初始设置值：OFF(关闭) |
| PDPNUM | 最大保留的PDP个数 | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置最大保留的PDP个数。<br>前提条件: 该参数在<br>“过滤开关”<br>配置为<br>“ON(开启)”<br>时生效。<br>数据来源：整网规划<br>取值范围：1～10<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145688)

**任务描述：**

假设某运营商GU网络能力有限，不能同时支持2个及以上的PDP上下文，即当用户从LTE网络切换到GU网络后，运营商期望SGSN按优先级保留1个PDP。为确保重要业务不被中断，运营商需要对全网用户进行如下APN优先级配置：

- “IMSI前缀”为“12302”的用户有两个“APNNI”：“huawei4.com”和“huawei5.com”，运营商期望优先保留“APNNI”为“huawei4.com”所对应的PDP。
- “IMSI前缀”为“1230”的用户，运营商期望优先保留“APNNI”为“huawei3.com”的PDP。
- 对于本网用户，运营商期望优先保留“APNNI”为“huawei2.com”的PDP。
- 对于其他所有用户，运营商期望优先保留“APNNI”为“huawei1.com”的PDP。

**配置脚本：**

1. 开启PDP过滤功能，设置为最大支持1个PDP：
  SET PDPFILTERCTL: SWITCH=ON, PDPNUM=1;
2. 增加两条“用户范围”为“IMSI_PREFIX(指定IMSI前缀)”、“IMSI前缀”为“12302”、“APNNI”分别为“huawei4.com”和“huawei5.com”的APN优先级记录，使得在该范围内“APNNI”为“huawei4.com”的优先级高于“huawei5.com”：
  ADD PDPFILTERAPN: SUBRANGE=IMSI_PREFIX, IMSIPRE="12302", APNNI="huawei4.com", PRI=1;
  ADD PDPFILTERAPN: SUBRANGE=IMSI_PREFIX, IMSIPRE="12302", APNNI="huawei5.com", PRI=2;
3. 增加一条“用户范围”为“IMSI_PREFIX(指定IMSI前缀)”、“IMSI前缀”为“1230”、“APNNI”为“huawei3.com”、“优先级”为“1”的APN优先级记录：
  ADD PDPFILTERAPN: SUBRANGE=IMSI_PREFIX, IMSIPRE="1230", APNNI="huawei3.com", PRI=1;
4. 增加一条“用户范围”为“LOCAL_USER(本网用户)”、“APNNI”为“huawei2.com”、“优先级”为“1”的APN优先级记录：
  ADD PDPFILTERAPN: SUBRANGE=LOCAL_USER, APNNI="huawei2.com", PRI=1;
5. 增加一条“用户范围”为“ALL_USER(所有用户)”、“APNNI”为“huawei1.com”、“优先级”为“1”的APN优先级记录：
  ADD PDPFILTERAPN: SUBRANGE=ALL_USER, APNNI="huawei1.com", PRI=1;

**任务描述：**

假设某运营商期望只对“IMSI前缀”为“12300”的用户按优先级保留1个PDP，对其他所有用户不限制最大保留的PDP个数，运营商需要进行如下APN优先级配置：

- “IMSI前缀”为“12300”的用户，运营商期望优先保留“APNNI”为“huawei7.com”的PDP。

**配置脚本：**

1. 开启PDP过滤功能，设置为最大支持1个PDP：
  SET PDPFILTERCTL: SWITCH=ON, PDPNUM=1;
2. 增加一条“用户范围”为“IMSI_PREFIX(指定IMSI前缀)”、“IMSI前缀”为“12300”、“APNNI”为“huawei7.com”、“优先级”为“1”的APN优先级记录：
  ADD PDPFILTERAPN: SUBRANGE=IMSI_PREFIX, IMSIPRE="12300", APNNI="huawei7.com", PRI=1;
