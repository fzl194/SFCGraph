# 调测TWAMP（Light模式）

- [操作场景](#ZH-CN_OPI_0000001188425147__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001188425147__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001188425147__1.3.3)

## [操作场景](#ZH-CN_OPI_0000001188425147)

当配置Light模式的TWAMP功能时，需要进行功能调测。

> **说明**
> 适用于SGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0000001188425147)

前提条件

- 请仔细阅读 [GWFD-110921 支持TWAMP特性概述](GWFD-110921 支持TWAMP特性概述_42545190.md)。
- 完成[激活TWAMP（Light模式）](激活TWAMP（Light模式）_42385398.md)。

数据

无。

## [操作步骤](#ZH-CN_OPI_0000001188425147)

1. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09587900.md) 命令，查询支持TWAMP的特性开关是否打开。
  [**LST LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09587900.md) : LICITEM="LKV3G5TWMP01";
    - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0000001188425147__step1512143124815)。
    - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)命令打开本特性对应的License配置开关。
2. 执行 [**DSP TWAMPSENDERSTATS**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/IPAPM功能管理/TWAMP/查询TWAMP发送端状态/显示TWAMP发送端详细信息（DSP TWAMPSENDERSTATS）_73142133.md) 命令，回显中显示丢包率、时延、抖动的QoS值。
    - 如果成功收集到相关QoS值，则调测结束。
      相关QoS性能指标如下。
          - **[1929392131 TWAMP LT测量sender发送包数](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392131 TWAMP LT测量sender发送包数_10814672.md)**
          - **[1929392132 TWAMP LT测量sender接收包数](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392132 TWAMP LT测量sender接收包数_10814673.md)**
          - **[1929392133 TWAMP LT测量平均丢包率](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392133 TWAMP LT测量平均丢包率_10814674.md)**
          - **[1929392134 TWAMP LT测量峰值丢包率](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392134 TWAMP LT测量峰值丢包率_10814675.md)**
          - **[1929392135 TWAMP LT测量最小双向时延](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392135 TWAMP LT测量最小双向时延_10814676.md)**
          - **[1929392136 TWAMP LT测量最大双向时延](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392136 TWAMP LT测量最大双向时延_10814677.md)**
          - **[1929392137 TWAMP LT测量平均双向时延](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392137 TWAMP LT测量平均双向时延_10814678.md)**
          - **[1929392138 TWAMP LT测量前向抖动最小值](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392138 TWAMP LT测量前向抖动最小值_10814679.md)**
          - **[1929392139 TWAMP LT测量前向抖动最大值](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392139 TWAMP LT测量前向抖动最大值_10814680.md)**
          - **[1929392140 TWAMP LT测量前向抖动平均值](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392140 TWAMP LT测量前向抖动平均值_10814681.md)**
          - **[1929392141 TWAMP LT测量后向抖动最小值](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392141 TWAMP LT测量后向抖动最小值_10814682.md)**
          - **[1929392142 TWAMP LT测量后向抖动最大值](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392142 TWAMP LT测量后向抖动最大值_10814683.md)**
          - **[1929392143 TWAMP LT测量后向抖动平均值](../../../../../OM参考/性能指标/UDG性能指标/Framework指标/性能指标/TWAMP测量/TWAMP LT性能测量/1929392143 TWAMP LT测量后向抖动平均值_10814684.md)**
    - 如果不能收集到相关QoS值，请执行[2](#ZH-CN_OPI_0000001188425147__step4)。
3. 收集信息并寻求技术支持。
    a. 执行 [**EXP MML**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md) 命令将当前配置数据导出为MML脚本文件并保存。
    b. 收集归纳所有信息并联系华为技术支持解决。
