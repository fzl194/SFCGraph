# 发送MME配置信息 (SND MMECFG)

- [命令功能](#ZH-CN_MMLREF_0000001172225769__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225769__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225769__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225769__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225769__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225769__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225769)

![](发送MME配置信息 (SND MMECFG)_72225769.assets/notice_3.0-zh-cn_2.png)

该命令执行后会改变eNodeB上该MME权重。

**适用网元：MME**

MME组Pool时，单个eNodeB会连接多个MME。该命令用于存储BYPASS状态时应急配置或针对特定MME调测。

#### [注意事项](#ZH-CN_MMLREF_0000001172225769)

- 该命令执行后立即生效。
- 当需要调测特定的MME时，可以接入特定的MME，并把对应的eNodeB连接的其他MME的“CAP（设备能力）”设置为0。
- 当本MME处在存储BYPASS状态时，可以应急执行此命令，并把“SENDSCE（发送场景）”设置为“ALL（所有eNodeB）”、“CAP（设备能力）”设置为0。
- 当本MME从存储BYPASS状态恢复后，需要通过此命令重新下发负荷权重到原始值，应把“SENDSCE（发送场景）”设置为“ALL（所有eNodeB）”、“CAP（设备能力）”设置为255。
- 非存储BYPASS场景，通过[**SET SYS**](../../../系统管理/系统参数管理/设置系统参数(SET SYS)_72345947.md)或者[**ADD MMECAPBYTA**](../../../S1接口管理/基于跟踪区的MME相对权重/增加基于跟踪区的MME相对权重配置(ADD MMECAPBYTA)_72345865.md)修改所有eNodeB上本MME的“CAP（设备能力）”值。
- 执行此命令前须确保本MME不在执行由[**STR OFFLOADBYMME**](../../迁移控制/启动MME迁移任务（STR OFFLOADBYMME）_72345693.md)或者**[STR OFFLOADBYTA](../../迁移控制/启动TA迁移任务（STR OFFLOADBYTA）_02884717.md)**启动的迁移任务，否则命令不能执行，若需立即执行此命令，可先执行[**STP OFFLOAD**](../../迁移控制/停止迁移任务(STP OFFLOAD)_26146092.md)命令停止迁移任务。
- 执行此命令前须确保eNodeB不在[**STR OFFLOADBYENODEB**](../../迁移控制/启动eNodeB迁移任务(STR OFFLOADBYENODEB)_26305902.md)命令启动的迁移任务列表中，否则命令不能执行，若需立即执行此命令，可先执行[**STP OFFLOAD**](../../迁移控制/停止迁移任务(STP OFFLOAD)_26146092.md)命令停止迁移任务。
- 存储BYPASS状态时出现进程复位，则此命令对该进程不生效。
- 如果命令执行期间有eNodeB与MME间链路故障、或者在执行命令后有新eNodeB接入，该命令修改的“CAP（设备能力）”不生效。
- 当使用该命令向指定eNodeB发送配置更新消息时，即使MME未收到eNodeB的响应，或者收到eNodeB配置更新失败的响应，MME都不会触发"ALM-80590 MME配置更新请求失败"的告警，而且在未收到eNodeB的响应的情况下，MME也不会重新发送配置更新消息。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225769)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225769)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225769)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SENDSCE | 发送场景 | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送本设备能力的范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL（所有eNodeB）”<br>- “SPECIFY（指定eNodeB）”<br>默认值：<br>“SPECIFY（指定eNodeB）” |
| MCCMNC | 移动国家码_移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定移动国家码及移动网号。<br>前提条件：只有<br>“发送场景”<br>为<br>“SPECIFY（指定eNodeB）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：5～6位数字<br>默认值：无 |
| ENODEBTYPE | eNodeB类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定eNodeB的类型。<br>前提条件：只有<br>“发送场景”<br>为<br>“SPECIFY（指定eNodeB）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “HOME_ENB(HOME_ENB)”：表示28位长的eNodeB。<br>- “MACRO_ENB(MACRO_ENB)”：表示20位长的eNodeB。<br>默认值：无 |
| ENODEBID | eNodeB标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定eNodeB ID，用来唯一标识一个eNodeB。<br>前提条件：只有<br>“发送场景”<br>为<br>“SPECIFY（指定eNodeB）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：0～268435455<br>默认值：无 |
| CAP | 设备能力 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB连接的MME负荷权重。负荷权重越大，相对的分配到的用户也越多。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>说明：- 当“发送场景”为“ALL（所有eNodeB）”时，CAP=255为特殊的值，系统将读取[**SET SYS**](../../../系统管理/系统参数管理/设置系统参数(SET SYS)_72345947.md)或者[**ADD MMECAPBYTA**](../../../S1接口管理/基于跟踪区的MME相对权重/增加基于跟踪区的MME相对权重配置(ADD MMECAPBYTA)_72345865.md)中的设备能力值下发。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225769)

发送MME配置信息，移动国家码_移动网号为123456，eNodeB类型为“HOME_ENB(HOME_ENB)”,eNodeB号为10，CAP为254：

SND MMECFG: SENDSCE=SPECIFY, MCCMNC="123456", ENODEBTYPE=HOME_ENB, ENODEBID=10, CAP=254;
