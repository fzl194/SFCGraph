---
id: UNC@20.15.2@MMLCommand@SET NS
type: MMLCommand
name: SET NS（设置NS参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NS
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- NS参数
status: active
---

# SET NS（设置NS参数）

## 功能

**适用网元：SGSN**

该命令用于设置NS层系统参数。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BLOCKTMR | Block定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：整网规划<br>取值范围：1s~120s<br>系统初始设置值：10s |
| BLOCKRTYNUM | Block重试次数 | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：整网规划<br>取值范围：1~6<br>系统初始设置值：3 |
| UNBLOCKRTYNUM | Unblock重试次数 | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：整网规划<br>取值范围：1~6<br>系统初始设置值：3 |
| RSTTMR | 复位定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：整网规划<br>取值范围：1s~120s<br>系统初始设置值：10s |
| RSTRTYNUM | 复位重试次数 | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：整网规划<br>取值范围：1~6<br>系统初始设置值：3 |
| TSTTMR | 测试定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定测试过程的定时器时长。在GSM 08.16中，定义为Tns-test。当Tns-test超时时，BSS或SGSN发送NS-ALIVE PDU到检测的NSVC链路上，启动Tns-alive定时器等待NS-ALIVE-ACK PDU ，当收到响应的NS-ALIVE-ACK PDU消息时停止Tns-alive定时器，并重新启动Tns-test定时器。<br>数据来源：整网规划<br>取值范围：1s~60s<br>系统初始设置值：30s<br>配置原则：<br>- 在非OSPF组网下，建议值为30s。<br>- 在OSPF组网下，建议值为60s。现OSPF双平面的切换时间约为40s，必须满足IPNSVC链路探测的时间大于OSPF双平面切换的时间，才能保证OSPF切换时IPNSVC链路不发生故障。 |
| ALIVERTYNUM | Alive重试次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Alive过程失败的重试次数。在GSM 08.16中，定义为NS-ALIVE-RETRIES。在Tns-alive定时器超时之前没有收到NS-ALIVE-ACK PDU消息，重新启动测试过程的最大次数。<br>数据来源：整网规划<br>取值范围：5~15<br>系统初始设置值：10 |
| PROVTMR | Prov定时器 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GB OVER IP动态配置过程的定时器时长。在GSM 08.16中，定义为Tsns-prov。当SGSN发起动态配置流程时，它同时会启动一个定时器Tsns-prov。当Tsns-prov超时时，SGSN重新发起对应的流程，直到重发次数超过参数PROVRTYNUM定义的值。<br>数据来源：整网规划<br>取值范围：1s~10s<br>系统初始设置值：5s |
| PROVRTYNUM | Prov重试次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GB OVER IP动态配置过程重试次数。在GSM 08.16中，定义为SNS-PROV-RETRIES。在Tsns-prov定时器超时之前没有收到对应动态配置流程的ACK消息，重新发起该动态配置流程的最大次数。<br>数据来源：整网规划<br>取值范围：1~6<br>系统初始设置值：3 |
| NSERPTRT | 自动配置的NSE的上报速率（个/秒） | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：整网规划<br>取值范围：0~100<br>系统初始设置值：5<br>说明：上报速率过快可能导致各个业务框的小区数目不均衡，建议使用系统初始设置值。 |
| NSEFTDELLEN | 自动配置的NSE的故障删除时长（分钟） | 可选必选说明：可选参数<br>参数含义：对于自动上报的动态over IP的NSE，如果该NSE下的所有IPNSVC链路中断后，开始计时，计时时长超过本参数的配置，则对应的NSE、小区、2G寻呼表、本端IP端点、对端IP端点、IPNSVC都将被自动删除。计时过程中，如果该NSE下的任意一条IPNSVC链路恢复正常，则停止计时。<br>数据来源：本端规划<br>取值范围：0~10800<br>系统初始设置值：0<br>说明：- 若本参数设置为0，则自动上报的动态over IP的NSE，其IPNSVC故障之后，该NSE以及其对应的小区、寻呼表、本端IP端点、对端IP端点、IPNSVC，将不会被自动删除。当“自动配置的NSE的故障删除时长（分钟）”配置为其他值时，自动配置的NSE故障后经过计时时长后删除，其中1~4按照最短时长5分钟来处理。<br>- 本参数修改之后，对后续发生故障的自动上报的动态over IP的NSE生效。<br>- 可以在割接之前，在割出NSE的SGSN上，将本参数修改到一个较小的值，这样该NSE被割接到其它SGSN之后，原有SGSN可以迅速的自动删除该NSE相关的信息，完成自动割接的相关处理。 |
| ATNSEDIS | 自动配置的NSE的分布策略 | 可选必选说明：可选参数<br>参数含义：该参数为保留参数，暂未实现。<br>数据来源：本端规划<br>取值范围：<br>- “GB_IP_DISTRIBUTE(仅分布在有Gb IP出口的框)”<br>- “SYSTEM_DISTRIBUTE(整系统分布)”<br>系统初始设置值：<br>“GB_IP_DISTRIBUTE(仅分布在有Gb IP出口的框)”<br>说明：- 针对业务框只部署3G业务出口而无Gb IP出口的情况，建议将本开关设置为“GB_IP_DISTRIBUTE(仅分布在有Gb IP出口的框)”。SGSN不会将自动配置的NSE以及其小区分布在这些3G业务框，可以减少2G业务在框间的转发。<br>- 使用“SYSTEM_DISTRIBUTE(整系统分布)”的方式，可达到2G的负荷在各个业务框间负荷分担。<br>- 该配置修改后，对后续自动配置的NSE生效，配置修改之前已经上报的NSE，不会改变其所在业务框。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NS]] · NS参数（NS）

## 使用实例

设置NS参数，使BLOCK定时器为60s：

SET NS: BLOCKTMR=60;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置NS参数(SET-NS)_72225703.md`
