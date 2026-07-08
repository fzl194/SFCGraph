---
id: UNC@20.15.2@MMLCommand@SET S1APPARA
type: MMLCommand
name: SET S1APPARA（设置S1AP协议参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: S1APPARA
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1AP协议参数
status: active
---

# SET S1APPARA（设置S1AP协议参数）

## 功能

![](设置S1AP协议参数(SET S1APPARA)_72225935.assets/notice_3.0-zh-cn_2.png)

如果拥塞控制功能开启，在网络拥塞时可能导致业务受损。若要将“拥塞控制功能”参数设置为“ON”，请联系华为技术支持。

**适用网元：MME**

此命令用于设置S1AP(S1 Application Protocol)相关参数。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。
- 当系统内4G Paging流量导致接口板流量拥塞时，开启Paging消息绑定功能。“SCTP数据绑定方式”设置成“BIND_PAGING_MESSAGES(Paging消息绑定)”后，在绑定定时器时长内发给同一个eNodeB的Paging消息会组成一个包发给eNodeB。对用户的Paging时延有影响。
-
  当开启S1接口SCTP层重传消息抑制功能后，在网络正常时，SCTP发送缓存使用率基本维持在1%以下，不会进行如下处理。如果出现网络拥塞，S1接口会做如下处理：

  - 当SCTP发送缓存使用率超过30%时，会主动开启“Paging消息绑定”功能。
    - 当SCTP发送缓存使用率超过60%时，会主动丢弃重传的信令消息。
    - 当SCTP发送缓存使用率超过70%时，会主动丢弃非语音相关的非“LTE精准寻呼”的Paging消息。
    - 当SCTP发送缓存使用率超过75%时，会主动丢弃语音相关的非“LTE精准寻呼”的Paging消息。
    - 当SCTP发送缓存使用率超过80%时，会主动丢弃“LTE精准寻呼”的非首次寻呼的Paging消息。
    - 当SCTP发送缓存使用率连续两分钟低于10%时，功能恢复。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TSTUP | 等待S1 Set up Request 消息定时器（s） | 可选必选说明：可选参数<br>参数含义：该定时器用于指定等待S1 Set Up Request消息的时长。在SCTP偶联建立时启动，在收到对端eNodeB发出的S1 SET UP消息后停止，超时后将释放SCTP偶联。<br>数据来源：与对端eNodeB设备协商<br>取值范围：1~65534s<br>系统初始设置值：60s |
| TRMMECFG | 重发MME配置更新定时器(s) | 可选必选说明：可选参数<br>参数含义：该定时器用于指定重发MME配置更新的时长。在MME向eNodeB发送了MME CFG UPT消息时启动，在收到eNodeB发出的MME CFG UPT ACK消息后停止，超时后MME将重发MME CFG UPT消息。<br>数据来源：与对端eNodeB设备协商<br>取值范围：1~65534s<br>系统初始设置值：20s<br>说明：超时后重发次数由参数<br>“MME配置更新定时器超时重发次数”<br>确定。如果重发次数达到配置的最大次数仍没收到eNodeB回应，则停止发送该消息。 |
| MMECFGCNT | MME配置更新定时器超时重发次数（times） | 可选必选说明：可选参数<br>参数含义：该计数器用于指定MME配置更新定时器超时后的重发次数。<br>数据来源：与对端eNodeB设备协商<br>取值范围：1~3times<br>系统初始设置值：3times |
| TSCTPDOWN | 防闪断定时器（s） | 可选必选说明：可选参数<br>参数含义：该定时器用于指定防闪断的时长。在MME监测到SCTP偶联断时启动，超时后检测SCTP偶联是否重建，如果重建则恢复eNodeB信息，如果没有重建则删除eNodeB信息。<br>数据来源：与对端eNodeB设备协商<br>取值范围：10~65534s<br>系统初始设置值：40s |
| TRST | Reset超时定时器（s） | 可选必选说明：可选参数<br>参数含义：该定时器用于指定Reset消息超时的时长。在MME向eNodeB发送RESET消息时启动，在收到eNodeB发出的确认消息时停止，超时后MME重发RESET消息。<br>数据来源：与对端eNodeB设备协商<br>取值范围：1~65534s<br>系统初始设置值：20s<br>说明：超时后重发次数由参数<br>“Reset定时器超时重发次数”<br>确定。如果重发次数达到配置的最大次数仍没收到eNodeB回应，则停止发送该消息。 |
| RSTCNT | Reset定时器超时重发次数（times） | 可选必选说明：可选参数<br>参数含义：该计数器用于指定Reset定时器超时重发次数。<br>数据来源：与对端eNodeB设备协商<br>取值范围：1~3times<br>系统初始设置值：3times |
| TIMETOWAIT | Time to Wait（s） | 可选必选说明：可选参数<br>参数含义：此参数用于设置S1 Setup Failure消息中Time to Wait信元的值。该信元用于指示eNodeB再次发起S1 Setup流程的等待时间。该参数在<br>[**SET S1CMPT**](../S1接口兼容性/设置S1接口兼容性(SET S1CMPT)_72345837.md)<br>命令的<br>“是否携带Time to Wait信元”<br>参数设置为<br>“YES(是)”<br>时有效。<br>数据来源：整网规划<br>取值范围：<br>- “ONE(1)”<br>- “TWO(2)”<br>- “FIVE(5)”<br>- “TEN(10)”<br>- “TWENTY(20)”<br>- “SIXTY(60)”<br>系统初始设置值：<br>“SIXTY(60)”<br>说明：商用局点建议Time to Wait信元的值设置为60秒，以避免S1建立失败时eNodeB快速发起S1 Setup流程，对MME造成冲击。 |
| BUNDLETYPE | SCTP数据绑定方式 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否把多个S1接口消息组在一个SCTP包中发给eNodeB。<br>数据来源：本端规划<br>取值范围：<br>- “NOT_BIND(不绑定)”<br>- “BIND_PAGING_MESSAGES(Paging消息绑定)”<br>系统初始设置值：<br>“NOT_BIND(不绑定)” |
| BUNDLETIME | 绑定等待时长（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于控制S1接口消息一次组包的时间间隔。<br>数据来源：本端规划<br>取值范围：10~100ms<br>系统初始设置值：20ms<br>配置原则：以10ms为粒度配置<br>说明：- 此参数设置越大，对业务增加的时延越大，为兼顾业务时延和组包效率，建议使用系统初始设置值20ms。<br>- “SCTP数据绑定方式”配置成“NOT_BIND(不绑定)”，该参数不生效。<br>- “SCTP数据绑定方式”配置成“BIND_PAGING_MESSAGES(Paging消息绑定)”，则会把该时间段内，发给同一个eNodeB的Paging消息组成一个SCTP包发给eNodeB。<br>- 如果在绑定等待时长内，需要组包的包长超过MTU值，则会按照MTU的长度组包。<br>- 本参数取值为特定话务模型下的评估结果，考虑到现网的话务模型和Paging业务的时延要求，本参数取值强依赖具体的话务模型，请联系华为公司本地机构提供专业的网络评估服务支持。 |
| IPPLC | S1-U地址携带策略 | 可选必选说明：可选参数<br>参数含义：当S1-U地址为IPv4v6双栈时，控制发送给eNodeB消息中transportLayerAddress信元和发送给S-GW消息中s1-u-sgw-f-teid信元的地址填写策略，同时也控制从eNodeB收到消息中transportLayerAddress信元的读取策略。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4IPV6(先IPV4后IPV6)”<br>- “IPV6IPV4(先IPV6后IPV4)”<br>- “S1MME(与S1MME相同)”<br>系统初始设置值：<br>“IPV4IPV6(先IPV4后IPV6)”<br>说明：- “IPV4IPV6(先IPV4后IPV6)”：发送给eNodeB消息中transportLayerAddress信元的地址顺序为先IPv4后IPv6；读取eNodeB发送的transportLayerAddress信元时按照先IPv4后IPv6的顺序读取；发送给S-GW消息中s1-u-sgw-f-teid信元的地址同时携带IPv4和IPv6。<br>- “IPV6IPV4(先IPV6后IPV4)”：发送给eNodeB消息中transportLayerAddress信元的地址顺序为先IPv6后IPv4；读取eNodeB发送的transportLayerAddress信元时按照先IPv6后IPv4的顺序读取；发送给S-GW消息中s1-u-sgw-f-teid信元的地址同时携带IPv4和IPv6。<br>- “S1MME(与S1MME相同)”：发送给eNodeB消息中transportLayerAddress信元的地址只携带与S1-MME地址类型相同的地址；读取eNodeB发送的transportLayerAddress信元时按照先IPv4后IPv6的顺序读取；发送给S-GW消息中s1-u-sgw-f-teid信元的地址只携带与S1-MME地址类型相同的地址。 |
| RESTRNSCONTROL | SCTP消息重发抑制功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否需要开启S1接口SCTP层重传消息抑制功能。<br>数据来源：本端规划<br>取值范围：<br>- “ON(开启)”<br>- “OFF(关闭)”<br>系统初始设置值：<br>“ON(开启)”<br>说明：由于此功能开启后，在出现网络拥塞时会有消息组包和主动丢消息的情况，对寻呼时延有一定的影响。当用于时延测试时可以关闭此功能。 |
| BUNDLENUM | 最大绑定包数 | 可选必选说明：可选参数<br>参数含义：该参数用于指示SCTP开启组包功能后，一个SCTP包中最大能组的包数（个）。<br>数据来源：本端规划<br>取值范围：2~10<br>系统初始设置值：2 |
| CCTRL | 拥塞控制功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指示SCTP层拥塞控制功能是否开启。<br>数据来源：本端规划<br>取值范围：<br>- “ON(开启)”<br>- “OFF(关闭)”<br>系统初始设置值：<br>“OFF(关闭)”<br>说明：当<br>**[SET SCTPCCTRLPARA](../../信令传输管理/SCTP管理/设置RAN侧拥塞检测功能参数(SET SCTPCCTRLPARA)_56488512.md)**<br>命令<br>“CCTRLSW（拥塞控制功能）”<br>配置为<br>“ON(开启)”<br>且<br>“CCTRLALGTYPE（拥塞控制算法）”<br>选择了<br>“BBR（BBR拥塞控制算法）”<br>时，该拥塞控制功能不生效。 |
| CTHD | 拥塞控制启控门限 | 可选必选说明：条件可选参数<br>参数含义：当SCTP偶联连续未收到的确认包数（个）超过此门限后，SCTP进入流控状态。<br>前提条件：该参数在<br>“拥塞控制功能”<br>参数配置为<br>“ON(开启)”<br>后生效。<br>数据来源：本端规划<br>取值范围：3~128<br>系统初始设置值：4 |
| CRTHD | 拥塞控制恢复门限 | 可选必选说明：条件可选参数<br>参数含义：当SCTP偶联连续收到的确认包数(个)超过此门限后，SCTP解除流控状态。<br>前提条件：该参数在<br>“拥塞控制功能”<br>参数配置为<br>“ON(开启)”<br>后生效。<br>数据来源：本端规划<br>取值范围：4~255<br>系统初始设置值：5<br>配置原则：拥塞控制恢复门限要大于拥塞控制启控门限。 |
| ENBIPALMSW | eNodeB IP重复告警上报功能开关 | 可选必选说明：可选参数<br>数据来源：本端规划<br>取值范围：<br>- “YES(是)”：表示功能开启。<br>- “NO(否)”：表示功能禁止。<br>系统初始设置值：NO(否)<br>说明：该参数开启后，如果存在eNodeB IP冲突，会上报“ALM-80716 eNodeB IP重复”告警，需要人工确认冲突解决后，手工恢复该告警。该功能为局点定制功能，其它局点开启前需要评估是否满足客户诉求。 |

## 操作的配置对象

- [S1AP协议参数（S1APPARA）](configobject/UNC/20.15.2/S1APPARA.md)

## 使用实例

设置S1AP定时器相关参数等待S1 Set up Request消息定时器为61秒，重发MME配置更新定时器为21秒，MME配置更新定时器超时重发次数为1次，防闪断定时器为42秒，Reset超时定时器为22秒，Reset定时器超时重发次数为2次，Time to Wait(s)为60秒，SCTP数据绑定方式为不绑定，S1-U地址携带策略为与S1MME相同，SCTP消息重发抑制功能开关为开启：

SET S1APPARA: TSTUP=61, TRMMECFG=21, MMECFGCNT=1, TSCTPDOWN=42, TRST=22, RSTCNT=2, TIMETOWAIT=SIXTY, BUNDLETYPE=NOT_BIND, IPPLC=S1MME, RESTRNSCONTROL=ON;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置S1AP协议参数(SET-S1APPARA)_72225935.md`
