# 显示GB性能统计实时结果(DSP RTMPERFCNTGB)

- [命令功能](#ZH-CN_CONCEPT_0253163161__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0253163161__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0253163161__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0253163161__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0253163161__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0253163161__1.3.6.1)
- [参考信息](#ZH-CN_CONCEPT_0253163161__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0253163161)

**适用网元：MME**

该命令用于实时查看GB_VNFC当前性能统计的情况，即查询某一对象实例的某一单元下所有指标的当前性能统计值。

#### [注意事项](#ZH-CN_CONCEPT_0253163161)

- 系统最多支持5个用户并发执行该命令。
- 由于各进程、各类型指标的采样点不能完全统一，因此指标结果存在一定的误差，统计误差最大不超过该指标在10s内的统计变化值。
- 测量周期前10s执行该命令查看性能统计，“查询结果”会返回“Result is UnReliable”，如果出现了此现象，可等待10s再查询。
- 使用该命令查询之前需要先在U2020/MAE上创建基于该测量对象实例的话统统计任务，等待5min后再执行相应查询命令。基于SGSN对象的话统指标不需要创建统计任务，该对象的测量单元可直接查询。
- 此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

#### [本地用户权限](#ZH-CN_CONCEPT_0253163161)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0253163161)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0253163161)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象 | 可选必选说明：必选参数。<br>参数含义：测量对象类ID。<br>数据来源：本端规划。<br>取值范围：<br>- “NSE(Gb接口NSE)”<br>- “SGSN(USN function)”<br>- “BSSID(Gb接口BSSID)”<br>- “CELL(小区号)”<br>- “IMSI(IMSI号码)”<br>- “RU(资源单元)”<br>- “IP_NSVCI_ENDPOINT(Gb接口端点IP NSVC)”<br>- “ScaleGroup(ScaleGroup)”<br>默认值：无 |
| MOI | 实例名称 | 可选必选说明：必选参数。<br>参数含义：测量对象实例。<br>数据来源：本端规划。<br>前提条件：该测量实例已经在U2020/MAE上话统测量管理（通过“性能->测量管理”菜单打开）中下发，SGSN对象类实例除外。<br>取值范围：1~63位字符串<br>默认值：无 |
| MUID | 测量单元 | 可选必选说明：必选参数。<br>参数含义：测量对象对应的测量单元。<br>数据来源：本端规划。<br>取值范围：<br>该参数在<br>“MOC”<br>参数设置为<br>“NSE(Gb接口NSE)”<br>时：<br>- “PERF_TYPE_GB_NSE(指定NSE NS)”<br>- “PERF_TYPE_GB_BSSGP_NSE(指定NSE BSSGP)”<br>该参数在<br>“MOC”<br>参数设置为<br>“SGSN(USN function)”<br>时：<br>- “PERF_TYPE_GB_LLC(SGSN LLC)”<br>- “PERF_TYPE_GB_SNDCP(SGSN SNDCP)”<br>- “PERF_TYPE_GB_BSSGP_ALL(SGSN BSSGP)”<br>- “PERF_TYPE_GB_NS(SGSN NS)”<br>- “PERF_TYPE_GB_CIPHER(SGSN 加密)”<br>- “PERF_TYPE_GB_RESOURCE(SGSN Gb资源)”<br>- “PERF_TYPE_GB_IP_NS(NS子层IP测量)”<br>- “PERF_TYPE_IP_PACKETS(转发面报文统计)”<br>- “PERF_TYPE_REDUNDANCY(设备级容灾业务)”<br>该参数在<br>“MOC”<br>参数设置为<br>“IP_NSVCI_ENDPOINT(Gb接口端点IP NSVC)”<br>时：<br>- “PERF_TYPE_GB_LLC(SGSN LLC)”<br>该参数在<br>“MOC”<br>参数设置为<br>“RU(资源单元)”<br>时：<br>- “PERF_TYPE_RU_CPU_RESOURCE(资源单元CPU资源_GB)”<br>该参数在<br>“MOC”<br>参数设置为<br>“ScalGroup(ScalGroup)”<br>时:<br>- “PERF_TYPE_SCALEGROUP_WORKLOAD(ScalGroup负载_GB)” |

#### [使用实例](#ZH-CN_CONCEPT_0253163161)

查询“SGSN”对象的“NS子层IP测量”单元下的所有指标的当前实时统计值：

DSP RTMPERFCNTGB:MOC=SGSN,MOI="0",MUID=PERF_TYPE_GB_IP_NS;

```
%%DSP RTMPERFCNTGB: MOC=SGSN, MOI="0", MUID=PERF_TYPE_GB_IP_NS;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
Measurement Result

Result is Reliable!

NS Uplink packets received from IP(ENTRIES) = 0
NS Uplink data Kbytes received from IP(KBytes) = 0
NS Downlink packets sent to IP(ENTRIES) = 0
NS Downlink data Kbytes sent to IP(KBytes) = 0
NS Uplink IP packets discarded(ENTRIES) = 0
NS Uplink IP data Kbytes discarded(KBytes) = 0
NS Downlink IP packets discarded(ENTRIES) = 14
NS Downlink IP data Kbytes discarded(KBytes) = 0

(Number of results = 2)

---    END 
```

#### [参考信息](#ZH-CN_CONCEPT_0253163161)

*表1 对象实例输入格式*

| 测量对象类 | 对象实例数据获取参考 | 对象实例输入格式 | 输入格式示例 |
| --- | --- | --- | --- |
| NSE：Gb接口NSE | **[LST PERFNSE](../性能对象管理/查询NSE标识(LST PERFNSE)_72225869.md)** | NSE标识 | "12" |
| SGSN：USN function | 0 | "0" | "0" |
| IMSI：IMSI号码 | IMSI号码 | IMSI号码 | "123031600000002" |
| RU: 资源单元 | **[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)** | 资源单元名称 | "USN_SP_RU_0064" |
| CELL：小区号 | **[LST CELL](../../../Gb接口管理/小区管理/查询小区(LST CELL)_26145990.md)** | 小区号 | "123054804041026(123-05-18436-4-4134)" |
| BSSID：Gb接口BSSID | **[LST NSE](../../../Gb接口管理/信令实体管理/查询信令实体（LST NSE）_72345629.md)** | BSS编号 | "133" |
| IP_NSVCI_ENDPOINT：Gb接口端点IP NSVC | **[DSP IPNSVC](../../../Gb接口管理/Gb over IP管理/IP网络NSVC链路管理/显示IP网络NSVC配置表(DSP IPNSVC)_72345609.md)** | 本端IP地址：本端端口号：对端IP地址：对端端口号 | "192.168.152.1:31201:192.168.152.20:31201" |
| ScalGroup:ScalGroup 名字 | **[DSP WORKLOAD](../../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/VM负载管理/查询系统负载(DSP WORKLOAD)_29626911.md)** | ScaleGroup的名字 | "SG1_USN" |
