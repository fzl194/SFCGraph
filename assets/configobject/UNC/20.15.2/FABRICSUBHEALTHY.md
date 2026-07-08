---
id: UNC@20.15.2@ConfigObject@FABRICSUBHEALTHY
type: ConfigObject
name: FABRICSUBHEALTHY（FABRIC内联口亚健康信息）
nf: UNC
version: 20.15.2
object_name: FABRICSUBHEALTHY
object_kind: global_setting
status: active
---

# FABRICSUBHEALTHY（FABRIC内联口亚健康信息）

## 说明

![](设置Fabric亚健康全局配置（SET FABRICSUBHEALTHY）_92520011.assets/notice_3.0-zh-cn_2.png)

如果修改阈值，需要注意：阈值过小，链路切换敏感，选路频繁变化，在网络负荷很大的场景下，频繁切换会导致网络传输质量下降。

该命令用来设置全局亚健康相关配置：包括亚健康阈值和亚健康检测周期。

Fabric亚健康检测基于Fabric OAM和业务报文，通过统计两个资源之间的Fabric OAM CCM报文和业务报文收发，实现链路级别的丢包检测功能。通过Fabric亚健康检测，可以计算有效链路的亚健康值，从而更新链路状态表。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-FABRICSUBHEALTHY]] · DSP FABRICSUBHEALTHY
- [[command/UNC/20.15.2/LST-FABRICSUBHEALTHY]] · LST FABRICSUBHEALTHY
- [[command/UNC/20.15.2/SET-FABRICSUBHEALTHY]] · SET FABRICSUBHEALTHY

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示FABRIC内联口亚健康信息（DSP-FABRICSUBHEALTHY）_92520048.md`
- 原始手册：`evidence/UNC/20.15.2/查询Fabric亚健康全局配置（LST-FABRICSUBHEALTHY）_92520019.md`
- 原始手册：`evidence/UNC/20.15.2/设置Fabric亚健康全局配置（SET-FABRICSUBHEALTHY）_92520011.md`
