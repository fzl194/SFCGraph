---
id: UNC@20.15.2@MMLCommand@SET GWOFFLOADPARA
type: MMLCommand
name: SET GWOFFLOADPARA（设置网关迁移参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GWOFFLOADPARA
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 网关故障管理
status: active
---

# SET GWOFFLOADPARA（设置网关迁移参数）

## 功能

**适用网元：MME**

该命令用于设置S-GW或P-GW故障场景下，对用户业务进行迁移的控制参数，包含迁移任务的启动时延、迁移速率以及S11/S5接口故障迁移控制开关。

## 注意事项

- 此命令执行后立即生效。
- 系统初次上电运行时，会执行系统初始设置值。
- 此命令涉及S-GW/P-GW故障下的业务恢复特性（特性编号：WSFD-201203，License部件编码：LKV2SRGF01），执行命令前请使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性License是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“打开”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DELAYTIMER | 迁移时延（分钟） | 可选必选说明：可选参数<br>参数含义：该参数用于设定系统检测到S-GW或P-GW故障后延迟启动迁移任务的时长（分钟）。<br>数据来源：整网规划<br>取值范围：0分钟～10分钟<br>系统初始设置值：3分钟<br>配置原则：<br>- 建议使用初始值。<br>- 设置时延是因为终端平均3分钟发起一次Service Request流程，在此流程中即可实现业务恢复，因此尽量依靠终端发起的信令流程来恢复业务，节省信令开销。<br>说明：- 此值为0时，系统检测网关故障后，立即启动迁移任务。<br>- 当S-GW/P-GW故障或重启，可通过该参数配置延迟一段时间后启用批量业务恢复，在此过程中个别用户终端触发的某些信令流程（Service Request、TAU等）或eNodeB发起的S1 Release等流程会触发系统提前恢复业务。 |
| RATE | 迁移速率（个/秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定迁移速率（个/秒）。<br>数据来源：整网规划<br>取值范围：0个/秒～500个/秒<br>系统初始设置值：200个/秒<br>配置原则：<br>- 迁移速率越高对性能和周边网元的影响越大，请根据实际使用场景和当前系统性能设置此参数。<br>- 迁移速率与VoLTE用户数以及迁移完成时间有关：迁移速率=VoLTE用户数/(迁移时间*60)。例如系统VoLTE用户数为36万用户，需要在30分钟内迁移完所有VoLTE用户，则迁移速率为=36*10000/(30*60)=200（个/秒）。<br>- 如果通过上面公式计算的值高于周边网元（eNodeB/S-GW/P-GW/PCRF/OCS）的实际处理能力，则以周边网元的处理能力为准。<br>- 当此值设置为0时，表示系统不批量迁移用户，只在用户Service Request、TAU流程中完成业务迁移。 |
| ITFOFFLOADSW | 接口故障迁移开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置在S11或S5接口故障场景下是否迁移用户。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>系统初始设置值：ON(开启) |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GWOFFLOADPARA]] · 网关迁移参数（GWOFFLOADPARA）

## 使用实例

假设某运营商有36万VoLTE语音用户，当S-GW发生故障时，迁移延迟时长为3分钟，希望在30分钟内完成对受影响用户的业务迁移，则迁移速率为：36*10000/(30*60)=200，即每秒需要完成200个用户的迁移。

SET GWOFFLOADPARA: DELAYTIMER=3, RATE=200, ITFOFFLOADSW=ON;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置网关迁移参数（SET-GWOFFLOADPARA）_72345681.md`
