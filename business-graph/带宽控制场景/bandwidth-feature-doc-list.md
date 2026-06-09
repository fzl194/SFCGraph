# 带宽控制特性文档清单

> 从 `feature-graph/data/UDG_feature_files.csv` 和 `feature-graph/data/UNC_feature_files.csv` 提取
> 共 24 个特性

## 总览

| # | 特性ID | 特性名称 | 产品 | 文件数 | 优先级 |
|---|--------|---------|------|--------|--------|
| 1 | GWFD-110101 | SA-Basic | UDG | 7 | ★核心 |
| 2 | GWFD-020351 | PCC基本功能 | UDG | 9 | ★核心 |
| 3 | GWFD-110311 | 基于业务感知的带宽控制 | UDG | 24 | ★核心 |
| 4 | GWFD-110312 | 基于业务累计流量的策略控制 | UDG | 3 | ★核心 |
| 5 | GWFD-110313 | 基于智能Shaping的组级带宽控制 | UDG | 4 | ★核心 |
| 6 | GWFD-020353 | 基于累计流量的策略控制 | UDG | 2 | ★核心 |
| 7 | GWFD-020354 | 基于业务的Shaping | UDG | 6 | ★核心 |
| 8 | WSFD-109101 | PCC基本功能 | UNC | 25 | ★核心 |
| 9 | WSFD-109104 | 基于累计流量的策略控制 | UNC | 6 | ★核心 |
| 10 | WSFD-211005 | 基于业务感知的带宽控制 | UNC | 4 | ★核心 |
| 11 | WSFD-211009 | 基于业务累计流量的策略控制 | UNC | 6 | ★核心 |
| 12 | GWFD-020357 | 增强的ADC基本功能 | UDG | 5 | 辅助 |
| 13 | GWFD-020358 | 业务触发的QoS保证 | UDG | 13 | 辅助 |
| 14 | GWFD-020359 | IM类业务无线资源管控 | UDG | 5 | 辅助 |
| 15 | GWFD-110301 | 基于终端系统的码率差异化控制 | UDG | 3 | 辅助 |
| 16 | GWFD-110302 | 基于上下行解耦的视频承载信令控制 | UDG | 5 | 辅助 |
| 17 | GWFD-110331 | 基于业务流标识的无线资源优化 | UDG | 4 | 辅助 |
| 18 | GWFD-110332 | 基于小区负荷上报的无线资源优化 | UDG | 4 | 辅助 |
| 19 | GWFD-020305 | 终端异常下行流量检测 | UDG | 4 | 辅助 |
| 20 | GWFD-111600 | SA特征库更新管控 | UDG | 1 | 辅助 |
| 21 | WSFD-109102 | ADC基本功能 | UNC | 6 | 辅助 |
| 22 | WSFD-109107 | 业务触发的QoS保证 | UNC | 6 | 辅助 |
| 23 | WSFD-109108 | 基于接入点策略控制 | UNC | 3 | 辅助 |
| 24 | WSFD-211101 | 基于小区负荷上报的无线资源优化 | UNC | 5 | 辅助 |
| | | **合计** | | **160** | |

---

## Batch-01: GWFD-110101 SA-Basic (UDG/UPF, 7 files)

> 业务感知基础

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic/GWFD-110101 SA-Basic参考信息_90197552.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic/GWFD-110101 SA-Basic特性概述_73565837.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic/实现原理/UNC和UDG配置映射_92963580.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic/实现原理/规则匹配原理_73618107.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic/实现原理/解析与识别_73594052.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic/实现原理/配置架构_92957237.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101 SA-Basic_24082506.md
```

---

## Batch-02: GWFD-020351 PCC基本功能 (UDG/UPF, 9 files)

> PCC框架基础

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/GWFD-020351 PCC基本功能参考信息_79592737.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/GWFD-020351 PCC基本功能特性概述_47011385.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/2_3_4_5G PCC功能差异_47013471.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/Event Trigger_47013472.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/业务流程_47013470.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/相关概念_72244993.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/激活PCC基本功能/配置动态PCC功能_74096530.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/激活PCC基本功能/配置本地PCC功能_74096529.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/调测PCC基本功能_42369277.md
```

---

## Batch-03: GWFD-110311 基于业务感知的带宽控制 (UDG/UPF, 24 files)

> ★核心：SA触发BWM/Shaping

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/GWFD-110311 基于业务感知的带宽控制参考信息_06417276.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/GWFD-110311 基于业务感知的带宽控制特性概述_77219469.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/实现原理_77219470.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于APN_DNN的用户组级带宽控制_49155915.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于PCC预定义规则的带宽控制_06381676.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于切片的带宽控制_44919837.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于时间段的带宽控制_84034122.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于用户TOS的带宽控制_84034080.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于用户_用户组_整机三级的带宽控制_84034124.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于用户组TOS的带宽控制_84034121.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/基于用户组的分级带宽管理控制_95938110.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/激活基于业务感知的带宽控制/针对HTTP应用基于用户的带宽控制_84034123.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/相关术语_78496471.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于APN_DNN的用户组级带宽控制_49155922.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于PCC预定义规则的带宽控制_08247339.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于切片的带宽控制_98479796.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于时间段的带宽控制_97098914.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于用户TOS的带宽控制_84034127.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于用户_用户组_整机三级控制中的整机的带宽控制_84034130.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于用户_用户组_整机三级控制中的用户组的带宽控制_84034128.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测基于用户组TOS的带宽控制_84034129.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制/调测针对HTTP应用基于用户的流量的带宽控制_84034126.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制/调测基于业务感知的带宽控制_84034125.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110311 基于业务感知的带宽控制_77219468.md
```

---

## Batch-04: GWFD-110312 基于业务累计流量的策略控制 (UDG/UPF, 3 files)

> FUP业务级

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110312 基于业务累计流量的策略控制/GWFD-110312 基于业务累计流量的策略控制特性概述_76651884.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110312 基于业务累计流量的策略控制/实现原理_77085621.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110312 基于业务累计流量的策略控制/激活基于业务累计流量的策略控制_84034134.md
```

---

## Batch-05: GWFD-110313 基于智能Shaping的组级带宽控制 (UDG/UPF, 4 files)

> 组级Shaping

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110313 基于智能Shaping的组级带宽控制/GWFD-110313 基于智能Shaping的组级带宽控制特性概述_76026865.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110313 基于智能Shaping的组级带宽控制/实现原理_76107341.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110313 基于智能Shaping的组级带宽控制/激活基于智能Shaping的组级带宽控制_76107785.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110313 基于智能Shaping的组级带宽控制/调测基于智能Shaping的组级带宽控制_76027313.md
```

---

## Batch-06: GWFD-020353 基于累计流量的策略控制 (UDG/UPF, 2 files)

> FUP基础（2_3_4G）

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020353 基于累计流量的策略控制/GWFD-020353 基于累计流量的策略控制特性概述_83974937.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020353 基于累计流量的策略控制/实现原理_83974938.md
```

---

## Batch-07: GWFD-020354 基于业务的Shaping (UDG/UPF, 6 files)

> 业务级Shaping

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/GWFD-020354 基于业务的Shaping参考信息_83195649.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/GWFD-020354 基于业务的Shaping特性概述_83823121.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/实现原理_83823122.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/激活基于业务的Shaping/针对TOS基于用户的流量整形_83195647.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/激活基于业务的Shaping/针对URL应用基于用户的流量整形配置_83195646.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020354 基于业务的Shaping/调测基于业务的Shaping_83195648.md
```

---

## Batch-08: WSFD-109101 PCC基本功能 (UNC/SMF, 25 files)

> PCC框架基础

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/实现原理_29056158.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/Gx Failover功能_31422950.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/配置QoS能力开放功能_48518810.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/配置与PCRF对接数据_30805096.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/配置动态PCC功能_30805098.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/配置异常场景数据_31422947.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/激活PCC基本功能/配置本地PCC功能_30805097.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/特性概述_29056157.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测PCC业务_31422956.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测PCRF负荷分担功能_31422955.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测QoS能力开放功能_84718093.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测到PCRF的数据_31422954.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/WSFD-109101 PCC基本功能特性概述（适用于5G）_71770359.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/AM策略偶联修改流程_50510739.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/AM策略偶联建立流程_50510738.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/AM策略偶联终止流程_50510740.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/UE策略偶联修改流程_50510745.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/UE策略偶联建立流程_50510744.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/UE策略偶联终止流程_50510746.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/异常处理流程_53323998.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/实现原理/相关概念_71770360.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/激活PCC基本功能_72467890.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/调测PCC基本功能_45059543.md
```

---

## Batch-09: WSFD-109104 基于累计流量的策略控制 (UNC/SMF, 6 files)

> FUP基础（Gx/N7）

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109104 基于累计流量的策略控制/WSFD-109104 基于累计流量的策略控制参考信息_29056192.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109104 基于累计流量的策略控制/实现原理（Gx）_29961018.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109104 基于累计流量的策略控制/实现原理（N7）_29961017.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109104 基于累计流量的策略控制/激活基于累计流量的策略控制_29056190.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109104 基于累计流量的策略控制/特性概述_29056168.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109104 基于累计流量的策略控制/调测基于累计流量的策略控制_29056191.md
```

---

## Batch-10: WSFD-211005 基于业务感知的带宽控制 (UNC/SMF, 4 files)

> ★核心：SA触发BWM

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211005 基于业务感知的带宽控制/WSFD-211005 基于业务感知的带宽控制参考信息_79619228.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211005 基于业务感知的带宽控制/激活基于业务感知的带宽控制_79619226.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211005 基于业务感知的带宽控制/特性概述_79619204.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211005 基于业务感知的带宽控制/调测基于业务感知的带宽控制_79619227.md
```

---

## Batch-11: WSFD-211009 基于业务累计流量的策略控制 (UNC/SMF, 6 files)

> FUP业务级（Gx/N7）

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211009 基于业务累计流量的策略控制/WSFD-211009 基于业务累计流量的策略控制参考信息_27915158.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211009 基于业务累计流量的策略控制/实现原理（Gx）_29039989.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211009 基于业务累计流量的策略控制/实现原理（N7）_27915155.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211009 基于业务累计流量的策略控制/激活基于业务累计流量的策略控制_27915156.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211009 基于业务累计流量的策略控制/特性概述_27915154.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211009 基于业务累计流量的策略控制/调测基于业务累计流量的策略控制_27915157.md
```

---

## Batch-12: GWFD-020357 增强的ADC基本功能 (UDG/UPF, 5 files)

> ADC应用检测

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/GWFD-020357 增强的ADC基本功能参考信息_84866922.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/GWFD-020357 增强的ADC基本功能特性概述_84866818.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/实现原理_84866819.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/激活增强的ADC基本功能_84866820.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/调测增强的ADC基本功能_84866921.md
```

---

## Batch-13: GWFD-020358 业务触发的QoS保证 (UDG/UPF, 13 files)

> 专用承载/QoS Flow

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/GWFD-020358 业务触发的QoS保证特性概述_80966039.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/参考信息_92206303.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/实现原理/专有QoS Flow相关流程（适用于5G）_10779227.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/实现原理/专有承载相关流程（适用于2_3_4G）_81656835.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/实现原理_81656834.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/激活业务触发的QoS保证/配置七层业务触发的QOS保证（PGW-U、UPF）_80361858.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/激活业务触发的QoS保证/配置三四层业务触发的QoS保证（PGW-U、UPF）_80318438.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/相关术语/QoS Flow_11153135.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/相关术语/专有承载_84864577.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/相关术语/缺省承载_84864576.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/调测业务触发的QoS保证/调测七层业务触发的QoS保证_10883660.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/调测业务触发的QoS保证/调测三四层业务触发的QoS保证_10507253.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020358 业务触发的QoS保证/调测业务触发的QoS保证/调测基于协议或协议组的专有承载创建功能_10883659.md
```

---

## Batch-14: GWFD-020359 IM类业务无线资源管控 (UDG/UPF, 5 files)

> IM类业务保障

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020359 IM类业务无线资源管控/GWFD-020359 IM类业务无线资源管控参考信息_39436330.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020359 IM类业务无线资源管控/GWFD-020359 IM类业务无线资源管控特性概述_39436333.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020359 IM类业务无线资源管控/实现原理_39436128.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020359 IM类业务无线资源管控/激活IM类业务无线资源管控_39436118.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020359 IM类业务无线资源管控/调测IM类业务无线资源管控_39436123.md
```

---

## Batch-15: GWFD-110301 基于终端系统的码率差异化控制 (UDG/UPF, 3 files)

> 终端系统码率

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110301 基于终端系统的码率差异化控制/GWFD-110301 基于终端系统的码率差异化控制特性概述_69712148.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110301 基于终端系统的码率差异化控制/激活基于终端系统的码率差异化控制_69722139.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110301 基于终端系统的码率差异化控制/调测基于终端系统的码率差异化控制_69722252.md
```

---

## Batch-16: GWFD-110302 基于上下行解耦的视频承载信令控制 (UDG/UPF, 5 files)

> 视频承载

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110302 基于上下行解耦的视频承载信令控制/GWFD-110302 基于上下行解耦的视频承载信令控制参考信息_15119104.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110302 基于上下行解耦的视频承载信令控制/GWFD-110302 基于上下行解耦的视频承载信令控制特性概述_59558143.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110302 基于上下行解耦的视频承载信令控制/实现原理_27342644.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110302 基于上下行解耦的视频承载信令控制/激活基于上下行解耦的视频承载信令控制_62146691.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110302 基于上下行解耦的视频承载信令控制/调测基于上下行解耦的视频承载信令控制_62266683.md
```

---

## Batch-17: GWFD-110331 基于业务流标识的无线资源优化 (UDG/UPF, 4 files)

> 无线资源优化

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110331 基于业务流标识的无线资源优化/GWFD-110331 基于业务流标识的无线资源优化参考信息_05184026.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110331 基于业务流标识的无线资源优化/GWFD-110331 基于业务流标识的无线资源优化特性概述_05031130.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110331 基于业务流标识的无线资源优化/激活基于业务流标识的无线资源优化_51849611.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110331 基于业务流标识的无线资源优化/调测基于业务流标识的无线资源优化_51649579.md
```

---

## Batch-18: GWFD-110332 基于小区负荷上报的无线资源优化 (UDG/UPF, 4 files)

> 小区负荷

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110332 基于小区负荷上报的无线资源优化/GWFD-110332 基于小区负荷上报的无线资源优化参考信息_80649081.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110332 基于小区负荷上报的无线资源优化/GWFD-110332 基于小区负荷上报的无线资源优化特性概述_31087646.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110332 基于小区负荷上报的无线资源优化/实现原理_76967393.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110332 基于小区负荷上报的无线资源优化/激活基于小区负荷上报的无线资源优化_30927860.md
```

---

## Batch-19: GWFD-020305 终端异常下行流量检测 (UDG/UPF, 4 files)

> 异常流量检测

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-020305 终端异常下行流量检测/GWFD-020305 终端异常下行流量检测参考信息_02455578.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-020305 终端异常下行流量检测/GWFD-020305 终端异常下行流量检测特性概述_02456812.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-020305 终端异常下行流量检测/激活终端异常下行流量检测_02455576.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-020305 终端异常下行流量检测/调测终端异常流量下行检测_02455577.md
```

---

## Batch-20: GWFD-111600 SA特征库更新管控 (UDG/UPF, 1 files)

> SA特征库

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-111600 SA特征库更新管控/GWFD-111600 SA特征库更新管控特性概述_73163205.md
```

---

## Batch-21: WSFD-109102 ADC基本功能 (UNC/SMF, 6 files)

> ADC应用检测

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/WSFD-109102 ADC基本功能参考信息_92582138.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/实现原理(Gx)_92855755.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/实现原理(N7)_92582135.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/激活ADC基本功能_92582136.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/特性概述_92582134.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/调测ADC基本功能_92582137.md
```

---

## Batch-22: WSFD-109107 业务触发的QoS保证 (UNC/SMF, 6 files)

> 专用承载/QoS Flow

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/WSFD-109107 业务触发的QoS保证参考信息_85397060.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/实现原理/专有QoS Flow相关流程（适用于5G）_85678418.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/实现原理/专有承载相关流程（适用于2_3_4G）_85678417.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/激活业务触发的QoS保证_85397058.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/特性概述_85397056.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109107 业务触发的QoS保证/调测业务触发的QoS保证_85397059.md
```

---

## Batch-23: WSFD-109108 基于接入点策略控制 (UNC/SMF, 3 files)

> APN/DNN策略

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109108 基于接入点策略控制/WSFD-109108 基于接入点策略控制参考信息_79067215.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109108 基于接入点策略控制/特性概述_79067211.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109108 基于接入点策略控制/调测基于接入点策略控制_79943605.md
```

---

## Batch-24: WSFD-211101 基于小区负荷上报的无线资源优化 (UNC/SMF, 5 files)

> 小区负荷

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211101 基于小区负荷上报的无线资源优化/WSFD-211101 基于小区负荷上报的无线资源优化参考信息_34615790.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211101 基于小区负荷上报的无线资源优化/实现原理_89376139.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211101 基于小区负荷上报的无线资源优化/激活基于小区负荷上报的无线资源优化_80495435.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211101 基于小区负荷上报的无线资源优化/特性概述_80615373.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-211101 基于小区负荷上报的无线资源优化/调测基于小区负荷上报的无线资源优化_34456008.md
```

---
