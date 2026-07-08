---
id: UNC@20.15.2@MMLCommand@SET GMM
type: MMLCommand
name: SET GMM（设置Gb模式MM协议参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GMM
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MM协议参数管理
- Gb模式MM协议参数
status: active
---

# SET GMM（设置Gb模式MM协议参数）

## 功能

**适用网元：SGSN**

该命令用于设置GMM(2G移动性管理)定时器及其他参数。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| T3322 | T3322（s） | 可选必选说明：可选参数<br>参数含义：此定时器用于控制SGSN发起分离请求消息与MS响应的时间间隔。在SGSN发送DETACH REQUEST消息时启动，在收到DETACH ACCEPT消息时停止，超时后SGSN会重发DETACH REQUEST消息。<br>数据来源：整网规划<br>取值范围：3s～12s<br>系统初始设置值：6s。 |
| N3322 | N3322（times） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN发送DETACH REQUEST消息时没有收到MS的响应消息，SGSN重发DETACH REQUEST消息的次数。<br>数据来源：整网规划<br>取值范围：0times～5times<br>系统初始设置值：4times。 |
| T3350 | T3350（s） | 可选必选说明：可选参数<br>参数含义：此定时器用于控制SGSN发起接受附着或路由区更新流程与MS响应流程成功的时间间隔。在SGSN发送ATTACH ACCEPT（P-TMSI/TMSI）、RAU ACCEPT（P-TMSI/TMSI）、P-TMSI REALLOC COMMAND启动，在收到ATTACH COMPLETE、RAU COMPLETE、P-TMSI REALLOC COMPLETE停止，超时后，SGSN将重发ATTACH ACCEPT、RAU ACCEPT或REALLOC COMMAND消息。<br>数据来源：整网规划<br>取值范围：3s～12s<br>系统初始设置值：6s。 |
| N3350 | N3350（times） | 可选必选说明：可选参数<br>参数含义：该参数用于指定在用户附着或路由区更新流程中没有收到MS的响应消息，SGSN重复发送ATTACH ACCEPT、ROUTING AREA UPDATE ACCEPT、PTMSI REALLOC COMMAND消息的次数。<br>数据来源：整网规划<br>取值范围：0times～5times<br>系统初始设置值：4times。 |
| T3360 | T3360（s） | 可选必选说明：可选参数<br>参数含义：此定时器用于控制网络侧发起鉴权加密流程与手机侧响应的时间间隔。在网络侧发送AUTH AND CIPH REQUEST消息启动，在收到AUTH AND CIPH RESPONSE消息停止，超时后，SGSN将重发AUTH AND CIPH REQUEST消息。<br>数据来源：整网规划<br>取值范围：3s～12s<br>系统初始设置值：6s。 |
| N3360 | N3360（times） | 可选必选说明：可选参数<br>参数含义：该参数用于指定在安全流程中，没有收到MS的响应消息，SGSN重复发送AUTHENTICATION AND CIPHERING REQUEST消息的次数。<br>数据来源：整网规划<br>取值范围：0times～5times<br>系统初始设置值：4times。 |
| T3370 | T3370（s） | 可选必选说明：可选参数<br>参数含义：此定时器用于控制SGSN发起身份识别与MS响应的时间间隔。在SGSN发送IDENTITY REQUEST消息时启动，在收到IDENTITY RESPONSE消息时停止，超时后，SGSN将重发IDENTITY REQUEST消息。<br>数据来源：整网规划<br>取值范围：3s～12s<br>系统初始设置值：6s。 |
| N3370 | N3370（times） | 可选必选说明：可选参数<br>参数含义：该参数用于指定身份识别请求消息重发次数。<br>数据来源：整网规划<br>取值范围：0times～5times<br>系统初始设置值：4times。 |
| T3313 | T3313（s） | 可选必选说明：可选参数<br>参数含义：此定时器用于控制SGSN发起寻呼与MS响应的时间间隔。在SGSN发送PAGING REQUEST消息后启动，在收到TRIGGER INDICATION (PAGING RESPONSE)消息后停止，超时后，SGSN重发PAGING REQUEST消息。<br>数据来源：整网规划<br>取值范围：4s～20s<br>系统初始设置值：6s。<br>说明：增加T3313(s)的值可能会提高寻呼成功率。 |
| N3313 | N3313（times） | 可选必选说明：可选参数<br>参数含义：该参数用于指定在寻呼流程中，没有收到MS的响应消息，SGSN重复发送PAGING REQUEST消息的次数。<br>数据来源：整网规划<br>取值范围：0times～5times<br>系统初始设置值：2times。<br>说明：增加N3313(times)的值可能会提高寻呼成功率。 |
| T3302 | T3302定时器（s） | 可选必选说明：可选参数<br>参数含义：本参数控制Attach Reject和RAU Reject消息中的<br>“T3302定时器”<br>信元的值。当UE发起附着或路由区更新请求失败超过5次后，启动该定时器。定时器超时后，UE才可以再次发起附着或路由区更新请求。<br>数据来源：整网规划<br>取值范围：0s～11160s<br>系统初始设置值：0s。<br>配置原则：<br>- 当本参数为0的时候，Attach Reject和RAU Reject消息将不携带T3302信元，定时器不开启。当本参数不为0的时候，Attach Reject和RAU Reject消息携带T3302信元下发给UE。<br>- 当参数取值为1的时候，在Attach Reject/Rau Reject消息中携带给UE的“T3302定时器”值为1，单位：2s。<br>- 当参数取值范围2～63：在Attach Reject/Rau Reject消息中携带给UE的“T3302定时器”是X/2向下取整，单位：2s。X即2~63之间的取值。<br>- 当参数取值范围64~1919：在Attach Reject/Rau Reject消息中携带给UE的“T3302定时器”是X/60向下取整，单位：min。X即64~1919之间的取值。<br>- 当参数取值范围1920~11160：在Attach Reject/Rau Reject消息中携带给UE的“T3302定时器”是X/360向下取整，单位：6min。X即1920~11160之间的取值。<br>说明：- 由于开启该定时器，会导致UE要等一段时间才能重试业务。因此系统不建议开启该定时器。如果运营商需要解决“UE Attach/RAU流程始终不成功，UE反复重试”的场景，为了降低系统资源消耗，可以开启该定时器。如开启该定时器，协议推荐取值为720s。<br>- 增加T3302定时器（s）的值会减少附着请求次数、减少附着拒绝次数、提高附着成功率、减少RAU请求次数、减少RAU失败次数、提高RAU成功率。 |
| PAGINGDELTA | 重寻呼间隔递增值（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定在寻呼流程中，没有收到MS的响应消息，SGSN重复发送PAGING REQUEST消息的间隔递增时间值。<br>数据来源：整网规划<br>取值范围：0s～20s<br>系统初始设置值：0s。<br>说明：增加重寻呼间隔递增值(s)可能会提高寻呼成功率。 |
| RDYTMR | 准备定时器（s） | 可选必选说明：可选参数<br>参数含义：此定时器用于控制MS和SGSN中MM状态处于READY状态的时间。在MS发送出一个LLC PDU后，MS中的该定时器需要重新启动；在SGSN收到一个正确的LLC PDU后，相应的READY定时器需要重启，超时后，MS和SGSN中的MM上下文将返回到STANDBY状态。<br>数据来源：整网规划<br>取值范围：<br>- 1：在Attach Accept/Rau Accept消息中携带给UE的Ready Timer值为1，单位：2秒。<br>- 2~63：在Attach Accept/Rau Accept消息中携带给UE的Ready Timer是X/2向下取整，单位：2秒。X即2~63之间的取值。<br>- 64~1919：在Attach Accept/Rau Accept消息中携带给UE的Ready Timer是X/60向下取整，单位：分。X即64~1919之间的取值。<br>- 1920~11160：在Attach Accept/Rau Accept消息中携带给UE的Ready Timer是X/360向下取整，单位：6分。X即1920~11160之间的取值。<br>系统初始设置值：44s。<br>配置原则：<br>- 该参数的值要小于[**ADD APNCTRL**](../../基于APN的MM拥塞控制_流控_寻呼优化配置/增加APN控制参数配置(ADD APNCTRL)_26145470.md)命令中的“Ready Timer定时器时长(秒)”参数的时长。<br>- 若MS签约的APN为[**ADD APNCTRL**](../../基于APN的MM拥塞控制_流控_寻呼优化配置/增加APN控制参数配置(ADD APNCTRL)_26145470.md)命令中配置的进行寻呼优化类型的APN，则准备定时器使用[**ADD APNCTRL**](../../基于APN的MM拥塞控制_流控_寻呼优化配置/增加APN控制参数配置(ADD APNCTRL)_26145470.md)命令中的“Ready Timer定时器时长(秒)”，本命令配置不生效。<br>- 根据协议3GPP 48.018的规定：- 该参数大于等于6秒时，准备定时器应该大于BSS保留PFC的时长定时器（最小值为6秒），BSS保留PFC的时长定时器可通过命令[**LST GBSM**](../../../业务安全管理/会话管理/SM协议参数管理/Gb模式SM协议参数/查询Gb模式SM协议参数(LST GBSM)_26145702.md)查看。<br>- 该参数小于6秒时，准备定时器的大小不与BSS保留PFC的时长定时器的大小关联，BSS保留PFC的时长定时器可通过命令[**LST GBSM**](../../../业务安全管理/会话管理/SM协议参数管理/Gb模式SM协议参数/查询Gb模式SM协议参数(LST GBSM)_26145702.md)查看。<br>说明：- 在STANDBY状态下，MS不能进行数据的接收和发送，但是可以接收寻呼，包括分组寻呼和电路寻呼。<br>- 寻呼成功之后，MS从STANDBY状态变迁到READY状态。MS处于READY(就绪)状态时，可以发送和接收分组数据单元。<br>- 该定时器的取值范围为离散值，根据3gpp规范24.008的10.5.7.3章节中定义的取值规则如下：当范围为2s-62s，间隔为2s；当范围为2min~31min，间隔为1min；当范围为36min-186min，间隔为6min。<br>- 增加准备定时器(s)的值会增加READY状态用户数、减少STANDBY状态用户数、减少寻呼次数、增加小区更新次数。 |
| PRDTMR | 周期路由更新定时器（min） | 可选必选说明：可选参数<br>参数含义：此定时器是用于控制MS自动发起周期性路由更新的时间间隔，该定时器作为附着接受或者路由更新接受消息的一个信元带给MS，超时后，MS将发起一次路由区更新。<br>数据来源：整网规划<br>取值范围：1min～186min<br>系统初始设置值：54min。<br>配置原则：<br>- 该定时器必须小于“MS可达定时器(min)”时长。<br>说明：- 该定时器的取值范围为离散值，根据3gpp规范24.008的10.5.7.3章节中定义的取值规则如下：当范围为1min~31min，间隔为1min；当范围为36min-186min，间隔为6min。<br>- 增加周期路由更新定时器(min)的值会减少READY状态用户数、增加STANDBY状态用户数、减少周期性RAU请求次数、增加寻呼次数、减少小区更新次数，可能会减少PTMSI重分配次数。 |
| MSRCHTMR | MS可达定时器（min） | 可选必选说明：可选参数<br>参数含义：此定时器用于控制MS可达定时器时长。在MM上下文进入STANDBY状态时启动，在MM上下文进入READY状态或者收到周期性路由区更新消息时停止，超时后，网络侧将MS标记为DETACHED。<br>数据来源：整网规划<br>取值范围：7min～198min<br>系统初始设置值：58min。<br>配置原则：<br>- 此定时器时长应大于“周期路由更新定时器(min)”时长。<br>说明：- 增加MS可达定时器(min)的值会增加STANDBY状态用户数、增加寻呼次数。<br>- 当启用M2M长周期性定时器功能后，如果UE支持长周期RAU/TAU定时器，则本参数的值将自动调整为[**DSP MMCTX**](../../../系统管理/用户数据库管理/显示MM上下文(DSP MMCTX)_26306164.md)命令的参数“使用的长周期RAU-TAU定时器（分钟）”的值加上4分钟 |
| IMDTCHTMR | 保留参数1 | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：整网规划<br>取值范围：0min～198min<br>系统初始设置值：0min<br>配置原则：参数取值为0min，表示可达定时器到期时立即隐式分离用户。 |
| T3 | T3定时器（s） | 可选必选说明：可选参数<br>参数含义：此定时器用于控制在Inter-RAU中，Old SGSN向New SGSN发送SGSN CONTEXT RESPONSE与Old SGSN删除签约数据的时间间隔。T3定时器超时后，将删除用户的签约数据。<br>数据来源：整网规划<br>取值范围：3s～60s<br>系统初始设置值：10s。 |
| DFTQOS | 缺省QoS | 可选必选说明：可选参数<br>参数含义：该参数用于指示在2.5G系统中SGSN向MS发送层3消息的QoS字段的填充值。<br>数据来源：整网规划<br>取值范围：0x000000~0xFFFFFF<br>系统初始设置值：0x0B9211。 |
| PRT | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置的用户的优先级。该优先级为配置的MM优先级，通过Gb发送给LLC，LLC会根据优先级不同进行不同的处理。<br>数据来源：整网规划<br>取值范围：0～15<br>系统初始设置值：0。<br>配置原则：<br>- 参数取值为0，表示不携带优先级。<br>- 取值为1～15，表示各优先级依次降低。 |
| RDTDELTA | 保留参数2 | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：整网规划<br>取值范围：0～5<br>系统初始设置值：0。 |

## 操作的配置对象

- [Gb模式MM协议参数（GMM）](configobject/UNC/20.15.2/GMM.md)

## 使用实例

设置T3322为6s、N3322为4次、T3350为6s、N3350为4次、T3360为6s、N3360为4次、T3370为6s、N3370为4次、T3313为6s、N3313为4次、T3302为4s、重寻呼间隔递增值为0s：

SET GMM:T3322=6, N3322=4, T3350=6, N3350=4, T3360=6, N3360=4, T3370=6, N3370=4, T3313=6, N3313=4, T3302=4, PAGINGDELTA=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置Gb模式MM协议参数(SET-GMM)_72345121.md`
