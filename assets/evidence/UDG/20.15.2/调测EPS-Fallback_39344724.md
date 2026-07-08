# 调测EPS Fallback

- [操作场景](#ZH-CN_OPI_0139344724__1.3.1)
- [必备事项](#ZH-CN_OPI_0139344724__1.3.2)
- [操作流程](#ZH-CN_OPI_0139344724__1.3.3)
- [操作步骤](#ZH-CN_OPI_0139344724__1.3.4)

## [操作场景](#ZH-CN_OPI_0139344724)

在不支持VoNR的场景下，语音业务回落到4G的VoLTE， UDG 不感知业务，只感知EPS网络和5GC网络之间的切换。

> **说明**
> 适用于UPF。

## [必备事项](#ZH-CN_OPI_0139344724)

前提条件

请仔细阅读 [GWFD-020282 EPS Fallback](../GWFD-020282 EPS Fallback_76232251.md) 。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | 用户IMSI号（IMSI） | 460000123456789 | 测试终端自带 | - |

工具

- 测试终端
- OM Portal
- 第三方抓包工具

## [操作流程](#ZH-CN_OPI_0139344724)

1. 5G Core网络上的用户进行语音业务。
2. 观察用户语音业务是否回落到EPS网络。

## [操作步骤](#ZH-CN_OPI_0139344724)

1. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09587900.md) 命令，查询 EPS Fallback 对应的License配置开关是否打开。
  ```
  LST LICENSESWITCH
  : LICITEM="LKV3G5EPSF01";
  ```
    - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0139344724__cmd444611061015)。
    - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)命令打开本特性对应的License配置开关。
2. 用户进行语音业务。
3. 执行 [**DSP SESSIONINFO**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话信息管理/会话信息查询/显示用户上下文（DSP SESSIONINFO）_86526407.md) 命令，通过IMSI查看 测试终端 激活后用户的状态。
  ```
  DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="460000123456789";
  ```
    - 如果“Qos Flow Identifier”不存在，说明当前用户在EPS网络，语音业务回落到4G的VoLTE成功，调测结束。
    - 如果“Qos Flow Identifier”存在，说明当前用户在5GC网络，语音业务回落到4G的VoLTE失败，请执行[4](#ZH-CN_OPI_0139344724__cmd1838194603163836)。
4. 收集信息并寻求技术支持。
    a. 在镜像接口或服务器上开启抓包工具，执行 [2](#ZH-CN_OPI_0139344724__cmd444611061015) 并保存报文。
    b. 执行 [**EXP MML**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md) 命令将当前配置数据导出为MML脚本文件并保存。
    c. 查看并收集对端设备配置及接口状态信息。
    d. 收集归纳所有信息并联系华为技术支持解决。
