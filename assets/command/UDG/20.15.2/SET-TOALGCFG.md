---
id: UDG@20.15.2@MMLCommand@SET TOALGCFG
type: MMLCommand
name: SET TOALGCFG（设置TCP算法配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TOALGCFG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 1
category_path:
- TCP优化服务管理
- TCP算法配置
status: active
---

# SET TOALGCFG（设置TCP算法配置）

## 功能

**适用NF：UPF**

该命令用于设置TCP算法配置，由于TCP算法的相关参数比较复杂，设置不当可能降低TCP优化效果，请联系华为技术支持评估后设置。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CCALG | TCPCUBICBETA | TCPCUBICHYSTART | ICWND | IRWND | HYSTARTLOWWIN | TCPFORWARDACK | LIMITOUTPUTBYTES | EBBRUSEPKTCVS | EBBRUSE2BDP | EBBRUSELCYCLE | EBBRLOTGEXSTUP | EBBRCRETGCWCP | EBBRRTTCNTINPB | EBBRSPLTACKRT | EBBRCOMPAGGR | EBBRAGGRDLEX | EBBRDRAININRB | EBBRAARCWND | EBBRAARCWNDRD | EBBRTREPBW | EBBRTREPRTT | EBBRELBTECC | EBBRTRPCYINF | EBBRTRPCYINFTR | EBBREPIFRTTTB | EBBRAGRCWNDGA | EBBRLTLOSSTH | EBBRFULLLOSSCNT | EBBRLOSTRSTART | EBBREPOCHMS | EBBRINFALWMS | EBBRAGGRDEWINS | EBBRMAXAGRDLMS | EBBREPBWUMCNT | EBBREPINFCNTTR | EBBRINFEPMAXCT | EBBRBWDIFF | EBBREPLBWMAXCT | EBBRMINDECFAC | EBBRINFUPTRSH | EBBRMAXINFUPCT | EBBRINFINCCTTR | EBBRINFINCMAXCT | EBBRENABLEPERF | EBBRPERFMINDEL | EBBRPERFMINRATE | EBBRPERFMAXRATE | EBBRPERFMAXDEL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | CUBIC | 717 | ENABLE | 64 | 64 | 512 | DISABLE | 131072 | DISABLE | DISABLE | ENABLE | ENABLE | DISABLE | DISABLE | ENABLE | ENABLE | DISABLE | ENABLE | ENABLE | ENABLE | ENABLE | DISABLE | DISABLE | ENABLE | ENABLE | 0 | 128 | 7 | 8 | 4 | 50 | 0 | 4 | 100 | 3 | 7 | 60 | 4194 | 3 | 768 | 5 | 10 | 6 | 12 | ENABLE | 50 | 1000 | 2000000 | 1000000 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCALG | TCP拥塞控制算法 | 可选必选说明：可选参数<br>参数含义：设置TCP拥塞控制算法。<br>数据来源：本端规划<br>取值范围：<br>- CUBIC：CCALG_CUBIC。<br>- MW3：CCALG_MW3。<br>- BIC：CCALG_BIC。<br>- BBR：CCALG_BBR。<br>- EBBR：CCALG_EBBR。<br>默认值：无<br>配置原则：无 |
| TCPCUBICBETA | 慢启动阶段的门限值计算因子 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“CUBIC”时为可选参数。<br>参数含义：设置当拥塞控制算法是cubic算法时，慢启动阶段的门限值计算因子。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1～1024。<br>默认值：无<br>配置原则：无 |
| TCPCUBICHYSTART | 启动hybrid slow start算法 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“CUBIC”时为可选参数。<br>参数含义：设置是否启动hybrid slow start算法。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| ICWND | 初始拥塞窗口 | 可选必选说明：可选参数<br>参数含义：设置TCP初始拥塞窗口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～255。<br>默认值：无<br>配置原则：无 |
| IRWND | TCP初始接收窗口 | 可选必选说明：可选参数<br>参数含义：设置TCP初始接收窗口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～1024。<br>默认值：无<br>配置原则：无 |
| HYSTARTLOWWIN | 启动hybrid slow start算法的最小拥塞窗口门限值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“CUBIC”时为可选参数。<br>参数含义：设置启动hybrid slow start算法的最小拥塞窗口门限值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为16～1000。<br>默认值：无<br>配置原则：无 |
| TCPFORWARDACK | Forward Acknowledgement算法 | 可选必选说明：可选参数<br>参数含义：设置是否启动(Forward Acknowledgement)FACK算法。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| LIMITOUTPUTBYTES | 每个套接字TCP队列的大小 | 可选必选说明：可选参数<br>参数含义：设置每个套接字TCP队列的大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1024～100000000。<br>默认值：无<br>配置原则：无 |
| EBBRUSEPKTCVS | 是否使用内核BBR丢包应对机制 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置在计算拥塞窗口时是否使用内核BBR的丢包应对机制。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRUSE2BDP | 是否基于两倍BDP | 可选必选说明：条件必选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为必选参数。<br>参数含义：该参数用于设置计算拥塞窗口时是否基于两倍BDP。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRUSELCYCLE | 是否使用测速长周期 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置PROBE_BW状态下测速时是否使用测速长周期。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRLOTGEXSTUP | 是否会触发退出慢启动 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为必选参数。<br>参数含义：该参数用于设置高丢包时是否会触发退出慢启动。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRCRETGCWCP | 是否强制使用保守态拥塞窗口 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置连接处于丢包恢复状态时是否强制使用保守态拥塞窗口。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRRTTCNTINPB | PROBE_RTT状态时是否更新rtt_cnt | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置连接处于PROBE_RTT状态时是否更新rtt_cnt成员变量。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRSPLTACKRT | 短时间窗对数据确认速率进行采样 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置是否基于短时间窗对数据确认速率进行采样。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRCOMPAGGR | 头阻塞聚合时延补偿拥塞窗口 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置是否用头阻塞聚合时延补偿拥塞窗口。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRAGGRDLEX | 头阻塞聚合时延是否会过期 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置采样得到的头阻塞聚合时延是否会过期。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRDRAININRB | 是否根据BDP和头阻塞聚合时延充分消耗inflight | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：在PROBE_BW状态下pacing gain=0.75时是否根据BDP和头阻塞聚合时延充分消耗inflight。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRAARCWND | 是否允许连接采用激进态的拥塞窗口 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置是否允许连接采用激进态的拥塞窗口。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRAARCWNDRD | PROBE_BW状态下是否仍然允许拥塞窗口采取激进态 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置PROBE_BW状态下pacing gain=0.75时是否仍然允许拥塞窗口采取激进态。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRTREPBW | 是否基于短时间窗监测带宽变化 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为必选参数。<br>参数含义：该参数用于设置是否基于短时间窗监测带宽变化。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRTREPRTT | 是否基于短时间窗监测时延增长趋势 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为必选参数。<br>参数含义：该参数用于设置是否基于短时间窗监测时延增长趋势。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRELBTECC | 是否提前切换至保守态拥塞窗口 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置当发现至少两个连续短时间窗有低带宽时是否提前切换至保守态拥塞窗口。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRTRPCYINF | 是否对inflight增长进行计数 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为必选参数。<br>参数含义：该参数用于设置在PROBE_BW状态下是否在每个测速cycle phase结束时对inflight增长进行计数。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRTRPCYINFTR | 是否监测inflight长期增长趋势 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为必选参数。<br>参数含义：该参数用于设置在PROBE_BW状态下是否监测每个测速cycle phase结束时的inflight长期增长趋势。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBREPIFRTTTB | 探测到时延增长趋势时应该采取的控制行为 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置决定探测到时延增长趋势时应该采取的控制行为。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0～2。<br>默认值：无<br>配置原则：无 |
| EBBRAGRCWNDGA | 计算拥塞窗口的头阻塞补偿时使用的增益值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置在计算拥塞窗口的头阻塞补偿时使用的增益值（基于128的缩放因子，即参数值为128时等效的增益值为1）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1～1280。<br>默认值：无<br>配置原则：无 |
| EBBRLTLOSSTH | 流量管制时的丢包率阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置流量管制时的丢包率阈值（基于128的缩放因子，即参数值为128时等效的丢包率阈值为100%）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1～128。<br>默认值：无<br>配置原则：无 |
| EBBRFULLLOSSCNT | 观测到丢包事件的最小数量 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置由丢包触发退出慢启动时需要在一个还回内观测到丢包事件的最小数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1～15。<br>默认值：无<br>配置原则：无 |
| EBBRLOSTRSTART | 单还回丢包率阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置由丢包触发退出慢启动时的单还回丢包率阈值（基于128的缩放因子，即参数值为128时等效的丢包率阈值为100%）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0～128。<br>默认值：无<br>配置原则：无 |
| EBBREPOCHMS | 短时间窗的时长(毫秒) | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置监测带宽、时延增长时一个短时间窗的时长，单位毫秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围10～500。<br>默认值：无<br>配置原则：无 |
| EBBRINFALWMS | 可容忍的时延膨胀值(毫秒) | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置监测时延增长时可容忍的时延膨胀值，单位毫秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0～1000。<br>默认值：无<br>配置原则：无 |
| EBBRAGGRDEWINS | 单个样本的生命周期长度(秒) | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置头阻塞聚合时延样本存在过期时单个样本的生命周期长度，单位秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1～15。<br>默认值：无<br>配置原则：无 |
| EBBRMAXAGRDLMS | 最大头阻塞聚合时延(毫秒) | 可选必选说明：条件必选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为必选参数。<br>参数含义：该参数用于设置在补偿拥塞窗口时允许的最大头阻塞聚合时延，单位毫秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0～500。<br>默认值：无<br>配置原则：无 |
| EBBREPBWUMCNT | 连续短时间窗个数最大阈值(激进态) | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置允许切换到激进态拥塞窗口时均观测到最大带宽增长的连续短时间窗个数最大阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围3～7。<br>默认值：无<br>配置原则：无 |
| EBBREPINFCNTTR | 连续短时间窗个数最大阈值(保守态拥塞窗口) | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置强制使用保守态拥塞窗口时持续观测到时延增长趋势的连续短时间窗个数最大阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围3～63。<br>默认值：无<br>配置原则：无 |
| EBBRINFEPMAXCT | 时延增长趋势持续时间的时间窗 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置若观测到的时延增长趋势持续时间达到相应数量的短时间窗，则将重设时延增长趋势，重新开始检测。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围3～63。<br>默认值：无<br>配置原则：无 |
| EBBRBWDIFF | 带宽增长最大阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置允许切换到激进态拥塞窗口时连续若干个短时间窗的带宽增长最大阈值，单位Mpps（基于16777216的缩放因子，即参数值为16777216时等效的带宽增长最大阈值为1Mpps）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1～16777216。<br>默认值：无<br>配置原则：无 |
| EBBREPLBWMAXCT | 短时间窗个数最大阈值(触发降速时) | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置触发降速时最大带宽均低于连接最大带宽样本的75%的连续短时间窗个数最大阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围3～7。<br>默认值：无<br>配置原则：无 |
| EBBRMINDECFAC | 最低降速乘性因子 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置观测到时延增长趋势并触发降速时的最低降速乘性因子（基于1024的缩放因子，即参数值为1024时等效的最低降速乘性因子为1）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1～1024。<br>默认值：无<br>配置原则：无 |
| EBBRINFUPTRSH | Inflight增长阈值(强制切换保守态拥塞窗口) | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置当inflight监测的增长计数达到该阈值时，强制切换至保守态拥塞窗口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围3～10。<br>默认值：无<br>配置原则：无 |
| EBBRMAXINFUPCT | Inflight增长阈值(保守态下降低门限值) | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置在保守态下，当inflight监测的增长计数达到该阈值时，降低inflight门限值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围5～15。<br>默认值：无<br>配置原则：无 |
| EBBRINFINCCTTR | Inflight增长切换阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置当监测到inflight增长趋势持续时间达到该阈值数量的测速cycle phase时，切换至保守态拥塞窗口或降低inflight门限值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围3～10。<br>默认值：无<br>配置原则：无 |
| EBBRINFINCMAXCT | Inflght增长重设阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置当监测到inflight增长趋势持续时间达到该阈值数量的测速cycle phase时，则将重设inflight增长趋势，重新开始检测。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围5～15。<br>默认值：无<br>配置原则：无 |
| EBBRENABLEPERF | 是否观测指标计数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置是否进行观测指标的计数。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| EBBRPERFMINDEL | 报文数最小阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置数据流进行观测时的总确认报文数最小阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0～1000。<br>默认值：无<br>配置原则：无 |
| EBBRPERFMINRATE | 数据流速率下限 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置数据流进行观测时的业务速率下限，单位Mbps（基于16777216的缩放因子，即参数值为3000时等效的业务速率下限为2.15Mbps）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0～3000。<br>默认值：无<br>配置原则：无 |
| EBBRPERFMAXRATE | 数据流速率上限 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置数据流进行观测时的业务速率上限，单位Mbps（基于16777216的缩放因子，即参数值为2000000时等效的业务速率限为1430.51Mbps）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围300000～2000000。<br>默认值：无<br>配置原则：无 |
| EBBRPERFMAXDEL | 报文数最大阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCALG”配置为“EBBR”时为可选参数。<br>参数含义：该参数用于设置数据流进行观测时的总确认报文数最大阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围10000～100000000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOALGCFG]] · TCP算法配置（TOALGCFG）

## 使用实例

设置TCP拥塞控制算法为CCALG_CUBIC，设置慢启动阶段的门限值计算因子为717，启动hybrid slow start算法，设置初始拥塞窗口大小为64，设置TCP初始接收窗口大小为64，设置启动hybrid slow start算法的最小拥塞窗口门限值为512，启动Forward Acknowledgement算法，设置每个套接字TCP队列的大小为131072：

```
SET TOALGCFG: CCALG=CUBIC, TCPCUBICBETA=717, TCPCUBICHYSTART=ENABLE, ICWND=64, IRWND=64, HYSTARTLOWWIN=512, TCPFORWARDACK=ENABLE, LIMITOUTPUTBYTES=131072;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-TOALGCFG.md`
