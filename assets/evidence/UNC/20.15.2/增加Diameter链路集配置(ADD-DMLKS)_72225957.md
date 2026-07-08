# 增加Diameter链路集配置(ADD DMLKS)

- [命令功能](#ZH-CN_MMLREF_0000001172225957__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225957__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225957__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225957__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225957__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225957__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225957)

**适用网元：SGSN、MME**

该命令用于增加一条Diameter链路集。Diameter链路集是MME与HSS之间的链路集，用来唯一关联一个本端与一个对端。

#### [注意事项](#ZH-CN_MMLREF_0000001172225957)

- 该命令执行后立即生效。
- 该表最大记录数为640。
- 一个本端实体与一个对端实体之间只能配置一条链路集。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225957)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225957)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225957)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKSIDX | Diameter链路集索引 | 可选必选说明：必选参数<br>参数含义：该参数用于在系统范围内部唯一标识一条Diameter链路集。<br>数据来源：本端规划<br>取值范围：0～639<br>默认值：无<br>配置原则：<br>- 此链路索引在系统范围内唯一。<br>- 建议从0开始顺序取值。 |
| LOCALIDX | 本地实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路集对应的本地实体的索引。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD DMLE**](../Diameter本地实体/增加Diameter本端实体(ADD DMLE)_72345881.md)<br>设置此参数。<br>数据来源：本端规划<br>取值范围：0～31<br>默认值：无 |
| PEERIDX | 对端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路集对应的对端实体的索引。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD DMPE**](../Diameter对端实体/增加Diameter对端实体(ADD DMPE)_72225963.md)<br>设置此参数。<br>数据来源：本端规划<br>取值范围：0～639<br>默认值：无 |
| LSSELMODE | 选路模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路集采用何种方式选择Diameter链路进行业务。<br>数据来源：整网规划<br>取值范围：<br>- “SELMODE_ROUND_ROBIN(轮选)”：表示存在多条链路时，采用顺序选择的方式选取各条链路。<br>- “SELMODE_LOAD_BALAN(负荷分担模式)”：表示在链路集中所有处于激活状态的链路以负荷分担的方式传输业务。<br>- “SELMODE_MASTER_SLAVE(主从)”：表示1＋N备份模式。在这种模式中，业务仅在链路集中的一条链路上传输，其余链路均处于备份状态。<br>- “SELMODE_ACTIVE(激活)”：表示使用上次使用的链路。<br>默认值：<br>“SELMODE_LOAD_BALAN(负荷分担模式)”<br>配置原则：建议值为<br>“SELMODE_LOAD_BALAN(负荷分担模式)”<br>。 |
| LINKSNAM | 链路集名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路集名称，标识Diameter链路集。<br>数据来源：本端规划<br>取值范围：0～32位字符串<br>默认值：noname<br>配置原则：建议取有实际意义的名称，以方便识别。例如<br>“To-HSS0”<br>。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225957)

增加一条Diameter链路集索引为0，本地实体索引为0，对端索引为0，选路模式为轮选模式，链路集名称为To-HSS0的DIAMETER链路集：

ADD DMLKS: LINKSIDX=0, LOCALIDX=0, PEERIDX=0, LSSELMODE=SELMODE_ROUND_ROBIN, LINKSNAM="To-HSS0";
