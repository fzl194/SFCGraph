# 调测TWAMP（Full模式）

- [操作场景](#ZH-CN_OPI_0000001142545192__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001142545192__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001142545192__1.3.3)

## [操作场景](#ZH-CN_OPI_0000001142545192)

IP传输场景下，线路带宽不稳定，运营商可以部署TWAMP功能检测网元间的传输网络QoS，如丢包、时延、抖动，实时在线监控传输网络QoS的变化。

> **说明**
> 适用于SGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0000001142545192)

前提条件

- 请仔细阅读 [GWFD-110921 支持TWAMP特性概述](GWFD-110921 支持TWAMP特性概述_42545190.md)。
- 完成[激活TWAMP（Full模式）](激活TWAMP（Full模式）_88305315.md)。

数据

无。

## [操作步骤](#ZH-CN_OPI_0000001142545192)

1. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09587900.md) 命令，查询支持TWAMP的特性开关是否打开。
  [**LST LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09587900.md) : LICITEM="LKV3G5TWMP01";
    - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0000001142545192__step2)。
    - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)命令打开本特性对应的License配置开关。
2. 执行 [**DSP TWAMPRESPONDER**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/查询TWAMP响应端状态/显示TWAMP响应端状态信息（DSP TWAMPRESPONDER）_27262284.md) 命令查看TWAMP测试报文发送情况。
    - 如果TWAMP报文正常发送，调测结束。
    - 如果TWAMP报文发送失败，请执行[2](#ZH-CN_OPI_0000001142545192__step4)。
3. 收集信息并寻求技术支持。
    a. 执行 [**EXP MML**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md) 命令将当前配置数据导出为MML脚本文件并保存。
    b. 收集归纳所有信息并联系华为技术支持解决。
