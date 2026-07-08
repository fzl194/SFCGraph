# 设置NB流控参数(SET NBFC)

- [命令功能](#ZH-CN_MMLREF_0000001126305974__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305974__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305974__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305974__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305974__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305974__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305974)

**适用网元：MME**

该命令用于设置NB流控参数

#### [注意事项](#ZH-CN_MMLREF_0000001126305974)

- 该命令执行后立即生效。
- 该命令主要用于NB-IoT业务的接入控制，配置不当可能导致业务受损，建议保持系统初始设置值。如需修改，请联系华为技术支持。
- 系统初次上电运行时，会执行系统初始设置值。
- 此配置涉及“基于延迟定时器的信令拥塞控制”特性（特性编号：WSFD-215201，license部件编码：LKV2LTCC01），请在设置参数前使用[**DSP LICENSE**](../../../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ON(打开)”。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305974)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305974)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305974)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NBFCSW | NB_IoT流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否开启NB-IoT流控功能。<br>数据来源：整网规划<br>取值范围：<br>- “ON（开启）”<br>- “OFF（关闭）”<br>系统初始设置值：<br>“OFF（关闭）”<br>配置原则：当NB-IoT用户可能影响普通用户正常业务时，可以通过设置该参数为<br>“ON（开启）”<br>来控制NB-IoT业务接入。<br>说明：- 该参数与基于延迟定时器的信令拥塞控制特性license共同完成NB-IoT流控功能的开启。<br>- 该参数为“ON（开启）”时，UNC根据“MINBOT（Back off timer最小值（秒））”和“MAXBOT（Back off timer最大值（秒））”的取值范围随机取得Back off timer定时器的值，发给终端。<br>- 当Back off timer定时器取值为1的时候，在Attach Reject/Service Reject/Control plane service Reject消息中携带给UE的“Back off timer定时器”值为1，单位：2s。<br>- 当Back off timer定时器取值范围2～63：在Attach Reject/Service Reject/Control plane service Reject消息中携带给UE的“Back off timer定时器”是X/2向下取整，单位：2s。<br>- 当Back off timer定时器取值范围64~1919：在Attach Reject/Service Reject/Control plane service Reject消息中携带给UE的“Back off timer定时器”是X/60向下取整，单位：min。<br>- 当Back off timer定时器值范围1920~11160：在Attach Reject/Service Reject/Control plane service Reject消息中携带给UE的“Back off timer定时器”是X/360向下取整，单位：6min。<br>- 每个用户的定时器时长有差异，依据配置的定时器范围将用户的重试分散开。 |
| CPUBTHD | CPU过载控制门限(%) | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置NB-IoT流控功能过载CPU门限。<br>前提条件：该参数在<br>“NBFCSW（NB_IoT流控开关）”<br>参数配置为<br>“ON（开启）”<br>后生效。<br>数据来源：整网规划<br>取值范围：40~80<br>系统初始设置值：65<br>说明：- 本参数设置越大，系统过载流控门限越高，对普通用户业务的影响越大。<br>- 本参数设置越小，系统过载流控门限越低，对普通用户业务的影响越小。 |
| MINTHD | 流控速率最小值（个/秒） | 可选必选说明：条件可选参数<br>参数含义：本参数用于控制每个SPP进程上每秒允许通过的NB-IoT用户接入消息包数的最小值，旨在将用户接入速率控制在一定范围内。<br>前提条件：该参数在<br>“NBFCSW（NB_IoT流控开关）”<br>参数配置为<br>“ON（开启）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0~2000<br>系统初始设置值：10<br>说明：- 本参数设置越大，系统过载时允许处理的低优先级业务越多，对普通用户业务的影响越大。<br>- 本参数设置越小，系统过载时允许处理的低优先级业务越少，对普通用户业务的影响越小。<br>- 流控速率是基于Attach流程评估的能力，并非真正的流程消息通过量。 |
| MAXTHD | 流控速率最大值（个/秒） | 可选必选说明：条件可选参数<br>参数含义：本参数用于控制每个SPP进程上每秒允许通过的NB-IoT用户接入消息包数的最大值，旨在将用户接入速率控制在一定范围内。<br>前提条件：该参数在<br>“NBFCSW（NB_IoT流控开关）”<br>参数配置为<br>“ON（开启）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0~2000<br>系统初始设置值：300<br>配置原则：该参数的取值必须大于等于<br>“MINTHD（流控速率最小值（个/秒））”<br>的取值。<br>说明：- 本参数设置的越大，则在低优先级业务突发时对普通用户业务的影响越大。<br>- 本参数设置的越小，则在低优先级业务突发时对普通用户业务的影响越小，但是如果小于实际能力过多，可能在系统能容忍的有限的突发下发生过多的流控丢包。<br>- 流控速率是基于Attach流程评估的能力，并非真正的流程消息通过量。 |
| MINBOT | Back off timer最小值（秒） | 可选必选说明：条件可选参数<br>参数含义：本参数用于设置Back off timer的最小值，用于计算发给NB-IoT终端的Back off timer时长。<br>前提条件：该参数在<br>“NBFCSW（NB_IoT流控开关）”<br>参数配置为<br>“ON（开启）”<br>后生效。<br>数据来源：本端规划<br>取值范围：1~11160<br>系统初始设置值：900 |
| MAXBOT | Back off timer最大值（秒） | 可选必选说明：条件可选参数<br>参数含义：本参数用于设置Back off timer的最大值，用于计算发给NB-IoT终端的Back off timer时长。<br>前提条件：该参数在<br>“NBFCSW（NB_IoT流控开关）”<br>参数配置为<br>“ON（开启）”<br>后生效。<br>数据来源：本端规划<br>取值范围：1~11160<br>系统初始设置值：1800<br>配置原则：该参数的取值必须大于等于<br>“MINBOT（Back off timer最小值（秒））”<br>的取值。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305974)

设置NB流控参数，设置NB_IoT流控开关为开启，设置CPU过载控制门限为65%，设置流控速率最小值为10个/秒，流控速率最大值为300个/秒，设置Back off timer最小值为900秒，设置Back off timer最大值为1800秒：

SET NBFC: NBFCSW=ON, CPUBTHD=65, MINTHD=10, MAXTHD=300, MINBOT=900, MAXBOT=1800;
