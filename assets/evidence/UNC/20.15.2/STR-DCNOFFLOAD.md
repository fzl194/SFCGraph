# 启动DCN迁移任务(STR DCNOFFLOAD)

- [命令功能](#ZH-CN_MMLREF_0000001126146124__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126146124__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126146124__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126146124__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126146124__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126146124__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126146124)

**适用网元：MME**

该命令用于启动DCN迁移任务。部署DECOR特性后，执行本命令将本MME中的用户快速归属到各自DCN中。可执行 [**DSP DCNOFFLOAD**](查询DCN迁移状态(DSP DCNOFFLOAD)_26305932.md) 命令查询当前系统中DCN迁移任务进度。

#### [注意事项](#ZH-CN_MMLREF_0000001126146124)

- 此配置涉及DECOR基础功能特性（特性编号：WSFD-208001，license部件编码：LKV2DECOR00）和DECOR特性（特性编号：WSFD-208002，license部件编码：LKV2DECOR01），执行命令请使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“打开”。
- 在迁移过程中，对于不属于本DCN的用户，MME会查找用户所属的DCN，如果查找到，则将用户迁移到所属的DCN中；如果未查找到，则说明此类用户开启DECOR功能但未规划所属DCN，系统会将用户分离。执行此命令前请先核查规划的DCN配置是否正确。
- 本命令仅针对已通过[**ADD DCNPLCY**](../../业务安全管理/DCN管理/DCN配置策略/增加DCN配置策略(ADD DCNPLCY)_26305642.md)命令开启了DECOR功能的用户进行迁移。
- 如果系统当前已启动DCN迁移或POOL迁移任务且未结束，则不能再启动新的迁移任务。请执行[**DSP DCNOFFLOAD**](查询DCN迁移状态(DSP DCNOFFLOAD)_26305932.md)和[**DSP OFFLOAD**](../迁移控制/显示迁移进度(DSP OFFLOAD)_72345691.md)命令查询系统迁移任务状态。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126146124)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126146124)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126146124)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFFLOADTYPE | 迁移用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定迁移用户范围。当启动DCN迁移后，MME基于本参数设定的用户范围，将不在本MME所属DCN并开启DECOR功能的用户迁出。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(全部用户)”<br>- “IMSI_PRE(指定IMSI前缀)”<br>- “IMSI(指定IMSI)”<br>默认值：<br>“ALL_USER(全部用户)”<br>说明：类型为<br>“IMSI(指定IMSI)”<br>的迁移主要用于拨测，执行迁移命令后会立即触发迁移流程。 |
| IMSIPRE | 指定IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用来指定IMSI前缀。<br>前提条件: 该参数在<br>“迁移用户范围”<br>参数配置为<br>“IMSI_PRE(指定IMSI前缀)”<br>后生效。<br>数据来源：全网规划<br>取值范围：5~15位字符串<br>默认值：无 |
| IMSI | 指定IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用来指定IMSI。<br>前提条件: 该参数在<br>“迁移用户范围”<br>参数配置为<br>“IMSI(指定IMSI)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~15位字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126146124)

1. 启动 “迁移用户范围” 为 “ALL_USER(全部用户)” 的迁移任务，将不在本MME所属DCN并开启DECOR功能的用户迁出：
  STR DCNOFFLOAD: OFFLOADTYPE=ALL_USER;
