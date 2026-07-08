# 激活基于TA List的寻呼自动流控（适用于AMF）

- [操作场景](#ZH-CN_OPI_0000001923057817__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001923057817__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001923057817__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001923057817__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001923057817)

本操作指导在运行网络中激活基于TA List的寻呼自动流控功能。

## [必备事项](#ZH-CN_OPI_0000001923057817)

前提条件

- 请仔细阅读[WSFD-010901 基于TA List的寻呼流控特性概述](WSFD-010901 基于TA List的寻呼自动流控特性概述（适用于AMF）_77098496.md)和[实现原理（适用于AMF）](实现原理（适用于AMF）_23137445.md)。
- AMF已对接网管系统，并且在网管上创建5分钟周期的性能测量任务，并勾选如下指标和待监控的测量对象：
    - [1929450177 指定TAI组的N2模式寻呼请求次数](../../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/AMF 移动性管理/指定TAI组的N2模式寻呼/1929450177 指定TAI组的N2模式寻呼请求次数_10377525.md)
    - [1929449489 指定TAI组的N2模式寻呼成功率](../../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/AMF 移动性管理/指定TAI组的N2模式寻呼/1929449489 指定TAI组的N2模式寻呼成功率_65026970.md)
    - [1929447376 指定TAI组的N2模式二次寻呼请求次数](../../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/AMF_SMF_GW-C_NRF_NSSF_SMSF_NCG业务性能指标/AMF 移动性管理/指定TAI组的N2模式寻呼/1929447376 指定TAI组的N2模式二次寻呼请求次数_64787784.md)

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[ADD PERFNGTAIGROUP](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/性能统计管理/AMF性能对象管理/增加NG TAI组性能统计对象（ADD PERFNGTAIGROUP）_09653102.md)** | NG TAI组名（NGTAIGPN） | NG12300101000<br>NG12300101001<br>NG12300101002<br>NG12300101003<br>NG12300101004 | 全网规划 | 增加NG TAI组性能测量对象。<br>说明：NG TAI组测量对象最多可以增加6000个，但仅能监控其中的2000个。 |
| **[ADD NGTAIGRPMEM](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/性能统计管理/AMF性能对象管理/增加5G TAI组性能统计对象成员（ADD NGTAIGRPMEM）_96241743.md)** | NG TAI组名（NGTAIGPN） | NG12300101000<br>NG12300101001<br>NG12300101002<br>NG12300101003<br>NG12300101004 | 全网规划 | 为NG TAI组性能测量对象增加TAI成员。 |
| **[ADD NGTAIGRPMEM](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/性能统计管理/AMF性能对象管理/增加5G TAI组性能统计对象成员（ADD NGTAIGRPMEM）_96241743.md)** | 起始TAI（BGNTAI） | 12300101000<br>12300101001<br>12300101002<br>12300101003<br>12300101004 | 全网规划 | 为NG TAI组性能测量对象增加TAI成员。 |
| **[ADD NGTAIGRPMEM](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/性能统计管理/AMF性能对象管理/增加5G TAI组性能统计对象成员（ADD NGTAIGRPMEM）_96241743.md)** | 终止TAI（ENDTAI） | 12300101000<br>12300101001<br>12300101002<br>12300101003<br>12300101004 | 全网规划 | 为NG TAI组性能测量对象增加TAI成员。 |
| **[SET NGTAIPAGMONPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/拥塞控制/TA LIST流控/设置NG TAI组寻呼异常监控功能参数（SET NGTAIPAGMONPARA）_75982876.md)** | TAI寻呼异常监控开关（SWITCH） | ON | 本端规划 | 设置NG TAI组对象寻呼异常监控功能参数。<br>说明：除<br>“TA List范围寻呼最大重试次数”<br>和<br>“语音业务TAI寻呼流控开关”<br>参数外，本命令的其它任何参数修改都会导致学习到的基准值被清除，已经发生的流控被取消，待AMF重新检测到指标异常后再次进行流控。 |
| **[SET NGTAIPAGMONPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/拥塞控制/TA LIST流控/设置NG TAI组寻呼异常监控功能参数（SET NGTAIPAGMONPARA）_75982876.md)** | N2模式TAI组寻呼成功率初始值（%）（PAGSUCRATDEFVAL） | 90 | 本端规划 | 设置NG TAI组对象寻呼异常监控功能参数。<br>说明：除<br>“TA List范围寻呼最大重试次数”<br>和<br>“语音业务TAI寻呼流控开关”<br>参数外，本命令的其它任何参数修改都会导致学习到的基准值被清除，已经发生的流控被取消，待AMF重新检测到指标异常后再次进行流控。 |
| **[SET NGTAIPAGMONPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/拥塞控制/TA LIST流控/设置NG TAI组寻呼异常监控功能参数（SET NGTAIPAGMONPARA）_75982876.md)** | N2模式TAI组寻呼请求次数起始监控阈值（MINPAGREQTHD） | 1000 | 本端规划 | 设置NG TAI组对象寻呼异常监控功能参数。<br>说明：除<br>“TA List范围寻呼最大重试次数”<br>和<br>“语音业务TAI寻呼流控开关”<br>参数外，本命令的其它任何参数修改都会导致学习到的基准值被清除，已经发生的流控被取消，待AMF重新检测到指标异常后再次进行流控。 |
| **[SET NGTAIPAGMONPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/拥塞控制/TA LIST流控/设置NG TAI组寻呼异常监控功能参数（SET NGTAIPAGMONPARA）_75982876.md)** | N2模式TAI组寻呼成功率降幅阈值（%）（PAGRATEEXPTHD） | 5 | 本端规划 | 设置NG TAI组对象寻呼异常监控功能参数。<br>说明：除<br>“TA List范围寻呼最大重试次数”<br>和<br>“语音业务TAI寻呼流控开关”<br>参数外，本命令的其它任何参数修改都会导致学习到的基准值被清除，已经发生的流控被取消，待AMF重新检测到指标异常后再次进行流控。 |
| **[SET NGTAIPAGMONPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/拥塞控制/TA LIST流控/设置NG TAI组寻呼异常监控功能参数（SET NGTAIPAGMONPARA）_75982876.md)** | N2模式TAI组二次寻呼请求次数增幅阈值（%）（PAGREQEXPTHD） | 20 | 本端规划 | 设置NG TAI组对象寻呼异常监控功能参数。<br>说明：除<br>“TA List范围寻呼最大重试次数”<br>和<br>“语音业务TAI寻呼流控开关”<br>参数外，本命令的其它任何参数修改都会导致学习到的基准值被清除，已经发生的流控被取消，待AMF重新检测到指标异常后再次进行流控。 |
| **[SET NGTAIPAGMONPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/拥塞控制/TA LIST流控/设置NG TAI组寻呼异常监控功能参数（SET NGTAIPAGMONPARA）_75982876.md)** | TAI寻呼消息启控连续异常周期个数（PAGEXPTIMESTHD） | 1 | 本端规划 | 设置NG TAI组对象寻呼异常监控功能参数。<br>说明：除<br>“TA List范围寻呼最大重试次数”<br>和<br>“语音业务TAI寻呼流控开关”<br>参数外，本命令的其它任何参数修改都会导致学习到的基准值被清除，已经发生的流控被取消，待AMF重新检测到指标异常后再次进行流控。 |
| **[SET NGTAIPAGMONPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/拥塞控制/TA LIST流控/设置NG TAI组寻呼异常监控功能参数（SET NGTAIPAGMONPARA）_75982876.md)** | TA List范围寻呼最大重试次数（PAGRETRYTIMES） | 0 | 本端规划 | 设置NG TAI组对象寻呼异常监控功能参数。<br>说明：除<br>“TA List范围寻呼最大重试次数”<br>和<br>“语音业务TAI寻呼流控开关”<br>参数外，本命令的其它任何参数修改都会导致学习到的基准值被清除，已经发生的流控被取消，待AMF重新检测到指标异常后再次进行流控。 |
| **[SET NGTAIPAGMONPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/拥塞控制/TA LIST流控/设置NG TAI组寻呼异常监控功能参数（SET NGTAIPAGMONPARA）_75982876.md)** | 语音业务TAI寻呼流控开关（IMSPAGINGSW） | OFF | 本端规划 | 设置NG TAI组对象寻呼异常监控功能参数。<br>说明：除<br>“TA List范围寻呼最大重试次数”<br>和<br>“语音业务TAI寻呼流控开关”<br>参数外，本命令的其它任何参数修改都会导致学习到的基准值被清除，已经发生的流控被取消，待AMF重新检测到指标异常后再次进行流控。 |

## [操作步骤](#ZH-CN_OPI_0000001923057817)

1. 增加NG TAI组性能测量对象。
  **[ADD PERFNGTAIGROUP](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/性能统计管理/AMF性能对象管理/增加NG TAI组性能统计对象（ADD PERFNGTAIGROUP）_09653102.md)**
2. 为NG TAI组性能测量对象增加TAI成员。
  **[ADD NGTAIGRPMEM](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/性能统计管理/AMF性能对象管理/增加5G TAI组性能统计对象成员（ADD NGTAIGRPMEM）_96241743.md)**
3. 设置NG TAI组对象寻呼异常监控功能参数。
  **[SET NGTAIPAGMONPARA](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/拥塞控制/TA LIST流控/设置NG TAI组寻呼异常监控功能参数（SET NGTAIPAGMONPARA）_75982876.md)**

## [任务示例](#ZH-CN_OPI_0000001923057817)

任务描述

开启基于TA List的寻呼自动流控功能。

脚本

//增加NG TAI组性能测量对象。

```
ADD PERFNGTAIGROUP:NGTAIGPN="NG12300101000";
ADD PERFNGTAIGROUP:NGTAIGPN="NG12300101001";
ADD PERFNGTAIGROUP:NGTAIGPN="NG12300101002";
ADD PERFNGTAIGROUP:NGTAIGPN="NG12300101003";
ADD PERFNGTAIGROUP:NGTAIGPN="NG12300101004";
```

//为NG TAI组性能测量对象增加TAI成员。

```
ADD NGTAIGRPMEM: NGTAIGPN="NG12300101000", BGNTAI="12300101000", ENDTAI="12300101000";
ADD NGTAIGRPMEM: NGTAIGPN="NG12300101001", BGNTAI="12300101001", ENDTAI="12300101001";
ADD NGTAIGRPMEM: NGTAIGPN="NG12300101002", BGNTAI="12300101002", ENDTAI="12300101002";
ADD NGTAIGRPMEM: NGTAIGPN="NG12300101003", BGNTAI="12300101003", ENDTAI="12300101003";
ADD NGTAIGRPMEM: NGTAIGPN="NG12300101004", BGNTAI="12300101004", ENDTAI="12300101004";
```

//设置NG TAI组对象寻呼异常监控功能参数。

```
SET NGTAIPAGINGMONPARA:SWITCH=ON,PAGSUCRATDEFVAL=90, MINPAGREQTHD=1000, PAGRATEEXPTHD=5, PAGREQEXPTHD=20, PAGEXPTIMESTHD=1, PAGRETRYTIMES=0, IMSPAGINGSW=OFF;
```
