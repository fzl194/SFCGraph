---
id: UNC@20.15.2@MMLCommand@MOD DMLKS
type: MMLCommand
name: MOD DMLKS（修改Diameter链路集配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DMLKS
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter链路集
status: active
---

# MOD DMLKS（修改Diameter链路集配置）

## 功能

**适用网元：SGSN、MME**

该命令用于修改一条Diameter链路集配置。当需要修改Diameter链路集的 “本地实体索引” ， “对端实体索引” ， “选路模式” 和 “链路集名称” 的全部或部分信息时，用此命令进行修改。

## 注意事项

- 该命令执行后立即生效。
- 该命令不能修改Diameter链路集索引。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKSIDX | Diameter链路集索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定准备修改的Diameter链路集的索引。<br>数据来源：本端规划<br>取值范围：0～639<br>默认值：无<br>说明：可以通过<br>[**LST DMLKS**](查询Diameter链路集配置(LST DMLKS)_26146280.md)<br>命令查看已有配置，确认所要修改的Diameter链路集的索引。 |
| LOCALIDX | 本地实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路集的本地实体索引。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD DMLE**](../Diameter本地实体/增加Diameter本端实体(ADD DMLE)_72345881.md)<br>设置此参数。<br>数据来源：本端规划<br>取值范围：0～31<br>默认值：无 |
| PEERIDX | 对端实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路集的对端实体索引。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD DMPE**](../Diameter对端实体/增加Diameter对端实体(ADD DMPE)_72225963.md)<br>设置此参数。<br>数据来源：本端规划<br>取值范围：0～639<br>默认值：无<br>说明：修改后，该链路集上业务将倒换到新的对端实体进行。与原对端实体间业务将中断。 |
| LSSELMODE | 选路模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定选路模式，用于表示Diameter链路集采用何种方式选择Diameter链路进行业务。<br>数据来源：整网规划<br>取值范围：<br>- “SELMODE_ROUND_ROBIN(轮选)”：表示存在多条链路时，采用顺序选择的方式选取各条链路。<br>- “SELMODE_LOAD_BALAN(负荷分担模式)”：表示在链路集中所有处于激活状态的链路以负荷分担的方式传输业务。<br>- “SELMODE_MASTER_SLAVE(主从)”：表示1＋N备份模式。在这种模式中，业务仅在链路集中的一条链路上传输，其余链路均处于备份状态。<br>- “SELMODE_ACTIVE(激活)”：表示使用上次使用的链路。<br>默认值：无<br>配置原则：建议值为<br>“SELMODE_LOAD_BALAN(负荷分担模式)”<br>。 |
| LINKSNAM | 链路集名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路集名称，标识Diameter链路集。<br>数据来源：本端规划<br>取值范围：0～32位字符串<br>默认值：无<br>配置原则：建议取有实际意义的名称，以方便识别。例如<br>“To-HSS0”<br>。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMLKS]] · Diameter链路集配置（DMLKS）

## 使用实例

将Diameter链路集索引为0的链路集的对端实体索引修改为1，选路模式修改为SELMODE_MASTER_SLAVE:

MOD DMLKS:LINKSIDX=0,PEERIDX=1,LSSELMODE=SELMODE_MASTER_SLAVE;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter链路集配置(MOD-DMLKS)_72345879.md`
