---
id: UNC@20.15.2@MMLCommand@STR OFFLOADBYMME
type: MMLCommand
name: STR OFFLOADBYMME（启动MME迁移任务）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: OFFLOADBYMME
command_category: 动作类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 迁移控制
status: active
---

# STR OFFLOADBYMME（启动MME迁移任务）

## 功能

![](启动MME迁移任务（STR OFFLOADBYMME）_72345693.assets/notice_3.0-zh-cn_2.png)

执行该命令会导致4G用户迁移。

**适用网元：MME**

此命令用于启动E-UTRAN接入类型接入 UNC 的用户迁移任务。在单个MME出现过载、MME需要进行迁移或升级、网络负载出现不均衡的情况下，可以启动用户迁移任务，能够及时调整网络运行状况，实现资源合理利用，并有效减少用户接入损耗和业务中断。

## 注意事项

- 启动迁移前必须确保已通过[**SET SYS**](../../系统管理/系统参数管理/设置系统参数(SET SYS)_72345947.md)命令将MME的“设备能力”设置为0，否则将无法启动迁移任务。
- 在迁移过程中，禁止使用[**SET SYS**](../../系统管理/系统参数管理/设置系统参数(SET SYS)_72345947.md)命令修改本MME的“设备能力”为非零值，以避免eNodeB继续为MME接入新用户而导致迁移用户数出现偏差。
- 在迁移过程中，禁止针对eNodeB执行[**SND MMECFG**](../MME POOL区管理/发送MME配置信息/发送MME配置信息 (SND MMECFG)_72225769.md)命令修改“设备能力”为非零值，以避免eNodeB继续为本MME接入新用户而导致迁移用户数出现偏差。
- 当迁移结束后，如果需要MME继续接入新用户，则需通过[**SET SYS**](../../系统管理/系统参数管理/设置系统参数(SET SYS)_72345947.md)命令将MME的“设备能力”设置成对应的值。
- 如果系统当前已启动DCN迁移或POOL迁移任务且未结束，则不能再启动新的迁移任务。请执行[**DSP DCNOFFLOAD**](../DCN迁移控制/查询DCN迁移状态(DSP DCNOFFLOAD)_26305932.md)和[**DSP OFFLOAD**](显示迁移进度(DSP OFFLOAD)_72345691.md)命令查询系统迁移任务状态。
- 类型为“MSISDN(MSISDN)”的迁移主要用于拨测场景。
- 类型为“IMSI(IMSI)”的迁移主要用于拨测，若多次启动该类型迁移任务，且不配置参数“目标MME编码”，则只有最近一次启动的迁移任务生效。
- 当启动类型为“IMSI(IMSI)”的迁移，且配置参数“目标MME编码”，将用户迁移到指定目标MME迁移时，迁移启动前不需要通过[**SET SYS**](../../系统管理/系统参数管理/设置系统参数(SET SYS)_72345947.md)命令修改“设备能力”。
- 在迁移过程中，请确保eNodeB与MME的S1-MME链路正常。
- 如果有用户启用了PSM，迁移结束过程中，该类用户未主动发起信令流程，将导致该类用户迁移失败。
- 此命令只针对WB-SAE用户生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFFLOADTYPE | 迁移类型 | 可选必选说明：可选参数<br>参数含义：该参数用来指定MME迁移类型。<br>取值范围：<br>- “ALL(全部用户)”<br>- “PART(部分用户)”<br>- “RATE(百分比用户)”<br>- “IMSI(IMSI)”<br>- “MSISDN(MSISDN)”<br>默认值：<br>“ALL(全部用户)”<br>说明：- “ALL(全部用户)”类型的迁移，默认只迁移WB-SAE用户，如果软参DWORD_EX23 BIT32设置为1，同时迁移NB-IoT用户。<br>- “PART(部分用户)”或者“RATE(百分比用户)”类型的迁移，在迁移的第二阶段，若系统中存在不在eDRX寻呼窗口的用户，将导致迁移时长延长最多60分钟。<br>- “IMSI(IMSI)”类型的迁移且不配置参数“目标MME编码”，若用户处于PSM状态，系统会等待用户主动上业务之后进行迁移；若用户不在eDRX寻呼窗口内，系统会启动延迟寻呼定时器延迟迁移。 |
| OFFLOADNUM | 迁移总数 | 可选必选说明：条件必选参数<br>参数含义：该参数用来指定MME迁移卸载用户总数。<br>前提条件：该参数在<br>“迁移类型”<br>参数配置为<br>“PART(部分用户)”<br>后生效。<br>取值范围：1~17000000<br>默认值：无 |
| OFFLOADRATE | 迁移比率（%） | 可选必选说明：条件必选参数<br>参数含义：该参数用来指定MME迁移卸载比率。<br>前提条件：该参数在<br>“迁移类型”<br>参数配置为<br>“RATE(百分比用户)”<br>后生效。<br>取值范围：1~100<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定所要迁移单个用户的国际移动用户标识。<br>前提条件：该参数在<br>“迁移类型”<br>参数配置为<br>“IMSI(IMSI)”<br>后生效。<br>取值范围：1~15位字符串<br>默认值：无 |
| MMEC | 目标MME编码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定用户需要迁移到的目标MME的编码。<br>前提条件：该参数在<br>“迁移类型”<br>参数配置为<br>“IMSI(IMSI)”<br>后生效。<br>取值范围：2位16进制编码<br>默认值：无<br>配置原则:出于拨测或测试目的，需要将用户从当前MME迁移到Pool内指定目标MME时，配置此参数。<br>说明：- 当将单个用户迁移到指定目标MME上时，不需要使用[**SET SYS**](../../系统管理/系统参数管理/设置系统参数(SET SYS)_72345947.md)命令将源MME的“设备能力”设置为0。<br>- 目标MME编码可在目标MME执行[**LST MMEID**](../MME POOL区管理/MMEID管理/查询MMEID配置(LST MMEID)_72345689.md)命令查询获取。<br>- 不输入0x也取输入为十六进制值。 |
| BEGMSISDN | 起始MSISDN | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定迁移任务的起始MSISDN标识。<br>前提条件：该参数在<br>“迁移类型”<br>参数配置为<br>“MSISDN(MSISDN)”<br>后生效。<br>取值范围：1~15位字符串<br>默认值：无 |
| ENDMSISDN | 终止MSISDN | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定迁移任务的终止MSISDN标识。<br>前提条件：该参数在<br>“迁移类型”<br>参数配置为<br>“MSISDN(MSISDN)”<br>后生效。<br>取值范围：1~15位字符串<br>默认值：无 |
| WAITSPECUE | 等待特殊UE迁移完成 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定在迁移全部用户的场景下，是否等待连接态的VoLTE（包括紧急呼叫）终端都被迁移完成之后才结束迁移任务。<br>前提条件：该参数在<br>“迁移类型”<br>参数配置为<br>“ALL(全部用户)”<br>后生效。<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：<br>“NO（否）” |
| WAITHLCOMUE | 等待高延迟UE迁移完成 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在迁移全部用户的场景下，是否等待处于空闲态使用eDRX的用户都被迁移完成之后才结束迁移任务。<br>前提条件：该参数在<br>“迁移类型”<br>参数配置为<br>“ALL(全部用户)”<br>后生效。<br>取值范围：<br>- “NO(否)”<br>- “WAIT_EDRX（等待eDRX用户迁移完成）”<br>默认值：<br>“NO(否)”<br>说明：- 如果本参数配置为“NO(否)”，迁移结束时可能会存在部分eDRX用户未迁移。<br>- 如果本参数配置为“WAIT_EDRX（等待eDRX用户迁移完成）”则迁移第二阶段的时长会延迟（WB-SAE用户最大延迟60分钟，NB-IoT用户最大延迟200分钟）。如需停止迁移，请执行[**STP OFFLOAD**](停止迁移任务(STP OFFLOAD)_26146092.md) |

## 操作的配置对象

- [MME迁移任务（OFFLOADBYMME）](configobject/UNC/20.15.2/OFFLOADBYMME.md)

## 使用实例

1. 将本MME上所有用户迁移到其它MME，且等待连接态的VoLTE（包括紧急呼叫）终端都被迁移完成之后才结束迁移任务：
  STR OFFLOADBYMME: OFFLOADTYPE=ALL, WAITSPECUE=YES;
2. 将本MME上的10000个用户迁移到其它MME：
  STR OFFLOADBYMME: OFFLOADTYPE=PART, OFFLOADNUM=10000;
3. 将本MME上30%的用户迁移到其它MME：
  STR OFFLOADBYMME: OFFLOADTYPE=RATE, OFFLOADRATE=30;
4. 将本MME上IMSI为123006666666663的用户迁移到其它MME：
  STR OFFLOADBYMME: OFFLOADTYPE=IMSI, IMSI="123006666666663";
5. 将本MME上IMSI为123006666666663的用户迁移到MMEC为08的MME：
  STR OFFLOADBYMME: OFFLOADTYPE=IMSI, IMSI="123006666666663", MMEC="08";
6. 将本MME上MSISDN区段从861390000到861399999的用户迁移到其它MME：
  STR OFFLOADBYMME: OFFLOADTYPE=MSISDN, BEGMSISDN="861390000", ENDMSISDN="861399999";
7. 将本MME上所有用户迁移到其它MME，且等待处于空闲态使用eDRX的用户都被迁移完成之后才结束迁移任务：
  STR OFFLOADBYMME: OFFLOADTYPE=ALL, WAITHLCOMUE=WAIT_EDRX;

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动MME迁移任务（STR-OFFLOADBYMME）_72345693.md`
