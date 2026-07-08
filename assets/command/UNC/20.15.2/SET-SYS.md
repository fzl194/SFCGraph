---
id: UNC@20.15.2@MMLCommand@SET SYS
type: MMLCommand
name: SET SYS（设置系统参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SYS
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 系统参数管理
status: active
---

# SET SYS（设置系统参数）

## 功能

![](设置系统参数(SET SYS)_72345947.assets/notice_3.0-zh-cn_2.png)

该命令设置影响系统基本功能，请根据各参数联机帮助具体描述，谨慎执行。

**适用网元：SGSN、MME**

该命令用于设置系统的基本参数。

## 注意事项

- 系统初次上电运行时，会执行系统初始设置值。
- 当本MME正在执行由[**STR OFFLOADBYMME**](../../网络管理/迁移控制/启动MME迁移任务（STR OFFLOADBYMME）_72345693.md)或者**[STR OFFLOADBYTA](../../网络管理/迁移控制/启动TA迁移任务（STR OFFLOADBYTA）_02884717.md)**命令启动的迁移任务时，禁止使用此命令修改本MME的“设备能力”为非零值，若需立即修改，可先执行[**STP OFFLOAD**](../../网络管理/迁移控制/停止迁移任务(STP OFFLOAD)_26146092.md)命令停止迁移任务。
- 当有eNodeB正在进行由[**STR OFFLOADBYENODEB**](../../网络管理/迁移控制/启动eNodeB迁移任务(STR OFFLOADBYENODEB)_26305902.md)启动的用户迁移时，执行此命令不会立即修改该eNodeB上本MME的“设备能力”，在迁移结束后，才会做修改。
- 此命令修改影响重大，请谨慎执行。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DESC | 系统描述 | 可选必选说明：可选参数<br>参数含义：该参数用于简单描述该<br>UNC<br>系统。<br>数据来源：整网规划<br>取值范围：1～64位字符串<br>系统初始设置值：“vUSN”。<br>配置原则：<br>该参数建议设置为“vUSN” |
| ID | 系统标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该<br>UNC<br>系统的标识号。<br>数据来源：整网规划<br>取值范围：0～254<br>系统初始设置值：“1”。 |
| NM | 系统名称 | 可选必选说明：可选参数<br>参数含义：该参数用于描述系统的名称。<br>数据来源：整网规划<br>取值范围：1～64位字符串<br>系统初始设置值：“vUSN_1”。<br>配置原则：<br>该参数建议设置为“vUSN” |
| LOC | 系统位置 | 可选必选说明：可选参数<br>参数含义：该参数用于描述系统的位置。<br>数据来源：整网规划<br>取值范围：1～64位字符串<br>系统初始设置值：“NO LOCATION”。<br>配置原则：<br>该参数建议设置为“vUSN” |
| SRV | 服务描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述系统提供的服务。<br>数据来源：整网规划<br>取值范围：1～64位字符串<br>系统初始设置值：“vUSN”。<br>配置原则：<br>该参数建议设置为“vUSN” |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该<br>UNC<br>所属的MCC，与<br>“MNC（移动网号）”<br>一起确定该<br>UNC<br>所属的PLMN（Public Land Mobile Network）。<br>数据来源：整网规划<br>取值范围：3位数字<br>系统初始设置值：“460”。<br>配置原则:<br>- 在系统为UNC时，该参数建议设置为“000” |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该<br>UNC<br>所属的MNC，与<br>“MCC（移动国家代码）”<br>一起确定该<br>UNC<br>所属的PLMN。<br>数据来源：整网规划<br>取值范围：2～3位数字<br>系统初始设置值：“00”。<br>配置原则：<br>- 该参数建议设置为“000” |
| PROVER | 协议版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统所使用的协议版本。<br>数据来源：整网规划<br>取值范围：<br>- “R99(R99)”<br>- “R4(R4)”<br>系统初始设置值：<br>“ R99(R99)”<br>。<br>说明：- UNC发送Supported Extension Headers Notification消息时会参考协议版本，如果是R99版本，则只支持PDCP PDU Number扩展头。如果是R4版本，则支持PDCP PDU Number、Suspend Request、Suspend Response扩展头。 |
| CNID | 核心网标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该系统的CNID（核心网标识），与<br>“MCC（移动国家代码）”<br>和<br>“MNC（移动网号）”<br>一起构成GLOBAL CN ID（全局核心网标识），在Paging等流程中，需要把此项带给RAN。 在系统使用Iu-Flex（Intra-domain Connection Of RAN Nodes To Multiple CN Nodes ：同一个域（CS/PS）内的一个RAN节点可以与多个CN节点进行连接）功能时，在同一个POOL内CNID不能重复。CNID是CS和PS共同规划，不能有冲突。<br>数据来源：整网规划<br>取值范围：0～4095或65535<br>系统初始设置值：“0”。 |
| CAP | 设备能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME负荷能力在MME Pool区中的相对权重值。<br>数据来源：整网规划<br>取值范围：0～255<br>系统初始设置值：<br>“255”<br>。<br>配置原则：<br>- 当UNC支持MME POOL时，在启动迁移任务时，需将此参数设置为0，避免新用户进行接入；当迁移任务结束后，需要恢复MME原权重。 |
| TMSIALLOC | TMSI资源分配方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统中PTMSI和GUTI的分配算法。其中非增强算法是指V100R002版本的算法；增强算法是指V100R017版本新增的算法，该算法用于提升用户标识的随机性和安全性。<br>数据来源：本端规划<br>取值范围：<br>- “ENHAN：（增强TMSI分配方式）”<br>- “UNENHAN：（非增强TMSI分配方式）”<br>系统初始设置值：<br>“ENHAN（增强TMSI分配方式）”<br>配置原则：系统初始使用增强算法，一般情况下使用增强算法。只有当增强算法存在无法解决的问题时，才使用非增强算法。<br>说明：该参数属于高危参数，TMSI分配算法修改后必须复位VNF才能生效。<br>链式备份功能开启时，不允许使用非增强TMSI分配方式。 |
| SUBSTORAG | 签约数据存储 | 可选必选说明：可选参数<br>参数含义：该参数用于指定部分用户级GPRS签约数据和EPS签约数据在系统中的存储方式。支持该功能的字段包括：Subscriber-Status、Network-Access-Mode、Operator-Determined-Barring、HPLMN-ODB、Regional-Subscription-Zone-Code、Access-Restriction-Data、3GPP-Charging-Characteristics、Roaming-Restricted-Due-To-Unsupported-Feature。<br>数据来源：本端规划<br>取值范围：<br>- “MERGE(合并存储)”：使用同一字段存储。<br>- “SEPARATE(分开存储)”：使用不同字段存储。<br>系统初始设置值：<br>“SEPARATE(分开存储)”<br>。<br>配置原则：<br>- 当现网用户级GPRS签约数据和EPS签约数据不一致时，需要将本参数设置为"SEPARATE(分开存储)"。<br>说明：- 本参数与软参DWORD_EX38 BIT25共同控制3GPP-Charging-Characteristics的存储方式。当本参数配置为“MERGE(合并存储)”并且DWORD_EX38 BIT25配置为0时，系统将GPRS和EPS签约数据的3GPP-Charging-Characteristics存储到同一字段，其他配置下，存储为不同字段。<br>- 本参数从“MERGE(合并存储)”修改为“SEPARATE(分开存储)”后，分开存储方式对新接入的用户立即生效，对已经接入的用户在下次进行移动性管理流程时生效。<br>- 本参数从“MERGE(合并存储)”修改为“SEPARATE(分开存储)”后，Gr和S6a/S6d接口的位置更新消息将会有所增加。<br>- 本参数从“SEPARATE(分开存储)”修改为“MERGE(合并存储)”后，合并存储方式对新接入的用户立即生效，对已经接入的用户逐步生效，约在10分钟内可全部生效。 |
| VERINCS11FLAG | S11标识 | 可选必选说明：可选参数<br>参数说明：该参数用于指定S11标识<br>数据来源：本端规划<br>取值范围：1～7位字符串<br>系统初始设置值：INVALID |
| NRICLFLAG | NRI容量限制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定4G用户的接入是否受到NRI容量的限制。2G、3G用户的接入不受此参数控制，会受到NRI容量的限制。<br>数据来源：整网规划<br>取值范围：<br>- “ON(开启)”：4G用户的接入受到NRI容量的限制，参见ADD LOCALNRI命令参考信息。<br>- “OFF(关闭)”：4G用户的接入不受NRI容量的限制。<br>系统初始设置值：“ON(开启)”<br>配置原则：建议值为“ON(开启)”。<br>说明：本参数为高危参数，需要ADD LOCALNRI/RMV LOCALNRI命令配合使用，操作不当会导致用户无法正常接入，请谨慎使用并联系华为技术支持协助操作。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SYS]] · 系统参数（SYS）

## 使用实例

设置系统的名称为“UNC”，协议版本为R99：

SET SYS: NM="UNC", PROVER=R99;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置系统参数(SET-SYS)_72345947.md`
