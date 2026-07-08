# 删除性能对象信息(RMV PERFOBJ)

- [命令功能](#ZH-CN_MMLREF_0000001172345787__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345787__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345787__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345787__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345787__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345787__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345787)

**适用网元：SGSN、MME**

本命令用于删除指定的性能统计对象。

#### [注意事项](#ZH-CN_MMLREF_0000001172345787)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345787)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345787)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345787)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象类型 | 可选必选说明：必选参数<br>参数含义：待删除的测量对象类型。<br>取值范围：<br>- “APN(APN)”<br>- “TAIGP(TAI组)”<br>- “HSSHOSTNAME(HSS主机名)”<br>默认值：无 |
| NAME | 对象名称 | 可选必选说明：条件可选参数<br>参数含义：待删除APN测量对象名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“APN(APN)”<br>时，才需要配置。<br>取值范围：0~63位字符串<br>默认值：无<br>说明：- 只有先确定在网管上删除了此APN对象，方可成功删除对象索引。<br>- 只能输入大小写字母、“.”、“-”、0~9的整数。 |
| INDEX | 索引 | 可选必选说明：条件可选参数<br>参数含义：待删除APN测量对象对应的索引。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“APN(APN)”<br>时，才需要配置。<br>取值范围：1~1000<br>默认值：无<br>说明：至少指定参数<br>“对象名称”<br>或者参数<br>“索引”<br>。可通过命令<br>[**LST PERFOBJ**](查询性能对象信息(LST PERFOBJ)_26306000.md)<br>获取相应的参数值。 |
| TAIGPN | TAI组名 | 可选必选说明：条件必选参数<br>参数含义：待删除TAI组测量对象的名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>时，才需要配置。<br>删除TAI组前，需要先通过命令<br>[**RMV PERFOBJRULE**](../性能对象规则管理/删除性能对象规则(RMV PERFOBJRULE)_26306006.md)<br>删除对应该TAI组的规则。删除TAI组后，此TAI组对象将无法进行性能统计。<br>取值范围：1~32位字符串<br>默认值：无 |
| HSSNAMEINDEX | HSS对象名称索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待删除的HSS对象名称索引。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“HSSHOSTNAME(HSS主机名)”<br>时，才需要配置。<br>取值范围：1~64<br>默认值：无<br>说明：- 可通过命令<br>[**LST PERFOBJ**](查询性能对象信息(LST PERFOBJ)_26306000.md)<br>获取相应的参数值。<br>- 删除HSS对象后，此对象对应的性能指标将无法进行统计。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345787)

1. 以下两种方式都可以删除APN对象“huawei.com”对应的索引:
    - RMV PERFOBJ: MOC=APN, NAME="huawei.com";
    - RMV PERFOBJ: MOC=APN, INDEX=1;
2. 以下可以删除TAI组名为“huawei”的TAI组对象：
    - RMV PERFOBJ: MOC=TAIGP, TAIGPN="huawei";
3. 以下可以删除HSS对象名称索引为“1”的HSS对象记录：
    - RMV PERFOBJ: MOC=HSSHOSTNAME, HSSNAMEINDEX=1;
