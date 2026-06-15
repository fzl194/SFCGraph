# 带宽控制场景文档清单

> 业务感知第二子场景：带宽控制（Bandwidth Control）
> 数据来源：UDG + UNC 整个产品文档
> 特性：仅定位特性ID（用户后续单独阅读），不展开特性文件清单
> 业务专题、概念文档：列出所有md文件，等权重
> 排除：MML命令文档、与带宽控制无关的业务专题

## 总览

| 类别 | UDG | UNC | 合计 |
|------|-----|-----|------|
| 特性（24个，仅ID） | 16个 / 99文件 | 8个 / 61文件 | 24个 / 160文件 |
| 业务专题（6个，展开文件） | 4个 / 187文件 | 2个 / 94文件 | 6个 / 281文件 |
| 5G基础知识概念（8个目录） | 4个 / 18文件 | 4个 / 18文件 | 8个 / 36文件 |
| **合计** | - | - | **477 md文件** |

---

## Section 1: 特性清单（仅ID，不展开文件）

> 用户后续会单独指定特性阅读。本节仅做ID登记和优先级标注。

### 1.1 核心特性（必读）

| 特性ID | 特性名称 | 产品 | 文件数 | 说明 |
|--------|---------|------|--------|------|
| GWFD-110101 | SA-Basic | UDG | 7 | 业务感知基础（与计费场景共享，需重读） |
| GWFD-020351 | PCC基本功能 | UDG | 9 | PCC框架基础（与计费场景共享，需重读） |
| GWFD-110311 | 基于业务感知的带宽控制 | UDG | 24 | ★核心：SA触发BWM/Shaping |
| GWFD-110312 | 基于业务累计流量的策略控制 | UDG | 3 | FUP业务级 |
| GWFD-110313 | 基于智能Shaping的组级带宽控制 | UDG | 4 | 组级Shaping |
| GWFD-020353 | 基于累计流量的策略控制 | UDG | 2 | FUP基础（2_3_4G） |
| GWFD-020354 | 基于业务的Shaping | UDG | 6 | 业务级Shaping |
| WSFD-109101 | PCC基本功能 | UNC | 25 | PCC框架（与计费场景共享，需重读） |
| WSFD-109104 | 基于累计流量的策略控制 | UNC | 6 | FUP基础（Gx/N7） |
| WSFD-211005 | 基于业务感知的带宽控制 | UNC | 4 | ★核心：SA触发BWM |
| WSFD-211009 | 基于业务累计流量的策略控制 | UNC | 6 | FUP业务级（Gx/N7） |

### 1.2 辅助特性（按需阅读）

| 特性ID | 特性名称 | 产品 | 文件数 | 说明 |
|--------|---------|------|--------|------|
| GWFD-020357 | 增强的ADC基本功能 | UDG | 5 | ADC应用检测 |
| GWFD-020358 | 业务触发的QoS保证 | UDG | 13 | 专用承载/QoS Flow |
| GWFD-020359 | IM类业务无线资源管控 | UDG | 5 | IM类业务保障 |
| GWFD-110301 | 基于终端系统的码率差异化控制 | UDG | 3 | 终端系统码率 |
| GWFD-110302 | 基于上下行解耦的视频承载信令控制 | UDG | 5 | 视频承载 |
| GWFD-110331 | 基于业务流标识的无线资源优化 | UDG | 4 | 无线资源优化 |
| GWFD-110332 | 基于小区负荷上报的无线资源优化 | UDG | 4 | 小区负荷 |
| GWFD-020305 | 终端异常下行流量检测 | UDG | 4 | 异常流量检测 |
| GWFD-111600 | SA特征库更新管控 | UDG | 1 | SA特征库 |
| WSFD-109102 | ADC基本功能 | UNC | 6 | ADC应用检测 |
| WSFD-109107 | 业务触发的QoS保证 | UNC | 6 | 专用承载/QoS Flow |
| WSFD-109108 | 基于接入点策略控制 | UNC | 3 | APN/DNN策略 |
| WSFD-211101 | 基于小区负荷上报的无线资源优化 | UNC | 5 | 小区负荷 |

---

## Section 2: 业务专题（展开md文件，等权重）

### Batch-01: UDG业务感知专题 (UDG, 41 files)

> SA基础+ SA action含BWM/Shaping/重定向/阻塞/Remark

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知产生背景_92407878.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知场景举例_92407896.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知定义_92407879.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知相关概念/SA性能优化库_79488943.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知相关概念/SA识别_92407882.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知相关概念/业务感知_92407881.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知相关概念/协议特征库_92407883.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知相关概念/协议解析库_92407884.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知相关概念/协议识别_92407885.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知相关概念/策略_92407886.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知相关概念/规则_92407887.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知相关概念/过滤条件_92407888.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知过程/业务解析与识别流程_92407893.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知过程/策略执行流程_92407895.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知过程/规则匹配流程_92407894.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知过程/规则规划与获取流程/规则获取_92407892.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知过程/规则规划与获取流程/规则规划_92407891.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知过程_92407889.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/加载特征库_92882614.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/基于业务套餐的配置实例/套餐1：计费场景_93112148.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/基于业务套餐的配置实例/套餐2：带宽控制_94838085.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/基于业务套餐的配置实例/套餐3：访问限制场景_94838086.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/规则配置/规则配置全景_92882615.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/规则配置/配置Rule_87803997.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/规则配置/配置User Profile与公共策略_90601230.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/规则配置/配置流动作/配置PCC策略_87803995.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/规则配置/配置流动作/配置带宽控制策略_92145040.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/规则配置/配置流过滤条件_87803991.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/规则配置实例/七层业务阻塞功能_87804004.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/规则配置实例/七层重定向功能_92393307.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/规则配置实例/三四层业务阻塞功能_87804003.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/规则配置实例/三四层重定向功能_92153850.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/规则配置实例_92464022.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/配置特性License开关_93112151.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/调测业务感知/调测七层Remark功能_87804014.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/调测业务感知/调测七层重定向功能_87804013.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/调测业务感知/调测七层阻塞功能_87804012.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/调测业务感知/调测三四层Remark功能_87804011.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/调测业务感知/调测三四层重定向功能_87804010.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/调测业务感知/调测三四层阻塞功能_87804009.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/调测业务感知_87804007.md
```

---

### Batch-02: 5G Core FUP解决方案 (UDG, 15 files)

> FUP累计流量带宽控制方案

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述/关键参数_23928086.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述/基于Gx接口策略控制_70687837.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述/基于N7接口策略控制_70607727.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述/系统影响与约束_24087910.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述_24087908.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/调测业务级累计流量策略控制_70687839.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/配置业务级累计流量策略控制_70607729.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/原理描述/关键参数_70607723.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/原理描述/基于Gx接口策略控制_24087904.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/原理描述/基于N7接口策略控制_23928080.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/原理描述/系统影响与约束_70687833.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/调测会话级累计流量策略控制_24087906.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/配置会话级累计流量策略控制_23928082.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/变更描述/20.7.0 01（2021-08-30）_24087900.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core FUP解决方案/特性映射_23928078.md
```

---

### Batch-03: 5G Core 重点业务保障解决方案 (UDG, 89 files)

> GBR保障/重点业务带宽保障

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/CloudUDN侧配置/Kafka进行partition重分配_65827357.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/CloudUDN侧配置/配置小区负载预测功能_89149846.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDC侧配置/开启License开关_99140330.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDC侧配置/配置GBR保障_38159968.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDC侧配置/配置Non-GBR保障_78014166.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDC侧配置/配置智能码率识别功能_24013085.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDC侧配置/配置跨NWDAF服务区域移动_06323488.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDC侧配置/配置跨NWDAF服务区域移动（建设初期）_24516677.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDG侧配置_61101881.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UNC侧配置/配置AMF_MME选择SMF_GW-C_06542597.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UNC侧配置/配置SMF基于PCF指示选择智能UPF及下发订阅策略（典型场景）_25346953.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UNC侧配置/配置SMF基于预定义规则选择智能UPF及下发订阅策略（异厂商PCF场景）_76485152.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UNC侧配置/配置SMF选择智能PCF及下发订阅策略（异厂商PCF场景）_06831997.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UNC侧配置/配置实时位置上报_12027850.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UPCF侧配置/UPCF侧配置（典型场景）_32788309.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UPCF侧配置/配置N23策略（异厂商PCF场景）_70582966.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/典型场景全局业务数据规划_24938201.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/异厂商场景全局业务数据规划_08406001.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/调测初始业务配置/调测应用GBR保障功能_72657226.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/调测初始业务配置/调测应用Non-GBR保障功能_27810673.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/调测初始业务配置/调测智能码率识别功能_78412864.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/调测初始业务配置/调测跨NWDAF服务区域移动（建设初期）_26365357.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/调测初始业务配置/调测跨NWDAF服务区域移动（建设完成）_06163700.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置业务Portal登录IP_77403933.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置主备CloudUDN对接_10321188.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置入口说明_02548688.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置接入无线侧指标数据_17790682.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置服务化接口_17947706.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/UDC侧配置/NWDAF典型配置实例_57714293.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/UDC侧配置/NWDAF配置流程_57682729.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/UDC侧配置/调测NWDAF配置_57682741.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/UDC侧配置/配置NWDAF本局数据_57602561.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/UDC侧配置/配置SBI接口_09763604.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/UDC侧配置/配置本地NRF_09923084.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/UDG侧配置/配置Nupf接口数据_18470868.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/UNC侧配置_35434301.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/UPCF侧配置/配置UPCF与NWDAF的对接数据_88915249.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/接口对接配置/接口配置总览_24938213.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/新增保障业务/UDC侧配置/配置新增保障应用GBR保障_12266562.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/新增保障业务/UDC侧配置/配置新增保障应用Non-GBR保障_82035082.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/新增保障业务/UDG侧配置_17506332.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/新增保障业务/UPCF侧配置_36370353.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/新增保障业务/调测新增保障业务配置_80595846.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/申请License_76978890.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/部署总览/典型场景部署总览_24818349.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/部署总览/异厂商PCF场景部署总览_72646164.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/RAT切换场景的业务流程_83026385.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据分析服务订阅/典型场景数据分析去订阅_24818321.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据分析服务订阅/典型场景数据分析更新订阅_76978878.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据分析服务订阅/典型场景数据分析订阅_24938205.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据分析服务订阅/异厂商PCF场景数据分析去订阅_89667528.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据分析服务订阅/异厂商PCF场景数据分析更新订阅_89507680.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据分析服务订阅/异厂商PCF场景数据分析订阅_89667540.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据分析结果开放与执行/删除保障建议_24818325.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据分析结果开放与执行/新建保障建议_24818333.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据分析结果开放与执行/更新保障建议_24938209.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据分析结果开放与执行_24818357.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据采集上报/采集小区资源数据_24818341.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据采集上报/采集用户实时位置_48275154.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/数据采集上报/采集质差数据_24938237.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/漫游时的重点业务保障/跨NWDAF服务区域移动（建设初期）_02770065.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/漫游时的重点业务保障/跨NWDAF服务区移动（建设完成）/跨省漫游关键业务流程_44655789.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/漫游时的重点业务保障/跨NWDAF服务区移动（建设完成）/跨省漫游场景总览_09137018.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/漫游时的重点业务保障/跨NWDAF服务区移动（建设完成）/跨省漫游对信令流程的影响_09027092.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/网元选择/SMF选择_21725142.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/网元选择/UPF选择/基于PCF指示选择智能UPF_91173900.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/网元选择/UPF选择/基于预定义规则选择UPF_94646348.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/网元选择/网元选择概述_97571937.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/重点业务保障全流程_88226505.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述_76819174.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/参考信息/协议遵循_24818369.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/场景概述_76819182.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/方案约束与影响/异厂商PCF场景约束与影响_70742746.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/方案约束与影响/重点业务保障通用约束与影响_24938249.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/解决方案实现原理/小区容量评估和负载预测_24938257.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/解决方案实现原理/报表可视化/智能码率识别报表_76896222.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/解决方案实现原理/质差判断/基于KPI的体验分析及上报_76978866.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/解决方案实现原理/质差判断_98081560.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/解决方案实现原理/重点业务保障管理/保障建议判断条件_46822962.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/解决方案实现原理/重点业务保障管理/基于智能码率识别的保障建议_46646592.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/解决方案实现原理/重点业务保障管理/综合判断_92983341.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/解决方案实现原理/重点业务保障管理_76819142.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/解决方案实现原理/重点业务保障解决方案的计费原理_19118572.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/解决方案版本配套要求_76819150.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/重点业务保障解决方案概述/典型场景业务方案概述_24818361.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/重点业务保障解决方案概述/异厂商PCF场景业务方案概述_02901545.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/重点业务保障解决方案概述_25227185.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/重点业务保障解决方案组网与接口/典型场景组网与接口_76978886.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/重点业务保障解决方案组网与接口/异厂商PCF场景组网与接口_25227197.md
```

---

### Batch-04: 5G Core 体验感知解决方案 (UDG, 42 files)

> QoE体验感知支撑带宽决策

```
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/保障用户体验感知场景/调测保障用户体验感知功能_90690618.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/保障用户体验感知场景_94432534.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/普通用户体验感知场景/UDG侧配置_15642930.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/普通用户体验感知场景/调测普通用户体验信息感知功能_21534654.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/普通用户体验感知场景_36232121.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UDC侧配置_05937066.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UDG侧配置_15435520.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UNC侧配置/UNC侧配置（典型场景）_18425829.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UNC侧配置/配置SMF选择智能PCF及下发订阅策略（异厂商PCF场景）_31501709.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UNC侧配置/配置SMF选择智能UPF及下发订阅策略（异厂商PCF场景）_95822676.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UPCF侧配置/配置智能PCF N23订阅策略（典型场景）_39409773.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/UPCF侧配置/配置智能PCF N23订阅策略（异厂商PCF场景）_31342057.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/初始业务配置/重点用户体验感知场景/调测重点用户体验感知功能_11788606.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置主备CloudUDN对接_01_10010.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置入口说明_34250365.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置接入用户体验数据（NupfR）_58126773.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/CloudUDN侧配置/配置服务化接口_19148098.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UDC侧配置/NWDAF典型配置实例_90530646.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UDC侧配置/NWDAF配置流程_34250353.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UDC侧配置/调测NWDAF配置_90690582.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UDC侧配置/配置NWDAF本局数据_90690578.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UDC侧配置/配置SBI接口_90530642.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UDC侧配置/配置本地NRF_34250357.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UDG侧配置/配置NupfR接口数据_15641438.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UDG侧配置/配置Nupf接口数据_90690586.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UNC侧配置_21814228.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/UPCF侧配置/配置UPCF与NWDAF的对接数据_88928805.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/接口对接配置/接口配置总览_90530634.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/申请License_34250345.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/业务部署与调测/部署总览_90530630.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/信令流程描述/保障用户体验感知信息采集流程_90690562.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/信令流程描述/异厂商PCF场景数据分析去订阅_95378626.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/信令流程描述/异厂商PCF场景数据分析更新订阅_30778141.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/信令流程描述/异厂商PCF场景数据分析订阅_95218746.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/信令流程描述/普通用户体验感知信息采集流程_34250341.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/信令流程描述/重点用户体验感知信息采集流程_90530626.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/方案介绍_72546024.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/方案约束与影响/体验感知通用约束与影响_90530622.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/方案约束与影响/异厂商PCF场景约束与影响_30937789.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/组网与接口/典型场景组网与接口_34250333.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/组网与接口/异厂商PCF场景组网与接口_95378622.md
output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/解决方案版本配套要求_90690558.md
```

---

### Batch-05: 5G Core FUP解决方案 (UNC, 15 files)

> FUP累计流量带宽控制方案（控制面视角）

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述/关键参数_23928086.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述/基于Gx接口策略控制_70687837.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述/基于N7接口策略控制_70607727.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述/系统影响与约束_24087910.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/原理描述_24087908.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/调测业务级累计流量策略控制_70687839.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/业务级累计流量策略控制/配置业务级累计流量策略控制_70607729.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/原理描述/关键参数_70607723.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/原理描述/基于Gx接口策略控制_24087904.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/原理描述/基于N7接口策略控制_23928080.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/原理描述/系统影响与约束_70687833.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/调测会话级累计流量策略控制_24087906.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/会话级累计流量策略控制/配置会话级累计流量策略控制_23928082.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/变更描述/20.7.0 01（2021-08-30）_24087900.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G Core FUP解决方案/特性映射_23928078.md
```

---

### Batch-06: 5G PCC之SM策略解决方案 (UNC, 79 files)

> SM策略E2E实现（含QoS、带宽、FUP）

```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略E2E实现原理/SM策略下发与执行原理/QoS Flow建立_修改_删除_86483638.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略E2E实现原理/SM策略下发与执行原理/QoS参数映射机制_86483640.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略E2E实现原理/SM策略下发与执行原理/业务识别与分流_86483639.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略E2E实现原理/SM策略生成原理/动态规则_86483635.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略E2E实现原理/SM策略生成原理/规则相关概念_17152898.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略E2E实现原理/SM策略生成原理/预定义规则_预定义规则组_本地规则_86483636.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略E2E实现原理/原理概述_15464534.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略关键内容/QoS/5G业务对QoS的诉求_87689107.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略关键内容/QoS/QoS架构/4G_5G QoS架构差异总结_11970130.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略关键内容/QoS/QoS架构/5G QoS关键参数及概念_11969173.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略关键内容/QoS/QoS架构/5G QoS架构模型_11970128.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略关键内容/QoS/QoS架构/QoS如何控制_99586315.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略关键内容/QoS/含义_12276278.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略关键内容/QoS/度量标准_12276279.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略关键内容/QoS/背景_12276277.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略关键内容/短信_邮件通知_86483632.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略关键内容/计费参数_86483630.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略关键内容/重定向_86483631.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务调测方法/动态PCC策略调测/动态规则调测/信令调测法_20602326.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务调测方法/动态PCC策略调测/动态规则调测/快速调测法_20442424.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务调测方法/动态PCC策略调测/预定义规则_预定义规则组调测/信令调测法_67363127.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务调测方法/动态PCC策略调测/预定义规则_预定义规则组调测/快速调测法_67920177.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务调测方法/本地PCC策略调测/信令调测法_67482083.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务调测方法/本地PCC策略调测/快速调测法_21200422.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务调测方法/调测原则/N7接口与N4接口的信令映射_30975312.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务调测方法/调测原则/调测方法概述_77134835.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务配置方法/业务拆解方法/单业务拆解方法_24232010.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务配置方法/业务拆解方法/多业务拆解方法_70951751.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务配置方法/动态PCC策略配置/动态规则配置/业务配置逻辑_64569729.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务配置方法/动态PCC策略配置/动态规则配置/概述_64489687.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务配置方法/动态PCC策略配置/动态规则配置/配置示例_18009858.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务配置方法/动态PCC策略配置/预定义规则_预定义规则组配置/业务配置逻辑_65059427.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务配置方法/动态PCC策略配置/预定义规则_预定义规则组配置/概述_18099670.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务配置方法/动态PCC策略配置/预定义规则_预定义规则组配置/配置示例_18259562.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务配置方法/本地PCC策略配置/业务配置逻辑_66336491.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务配置方法/本地PCC策略配置/概述_66416527.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/业务配置方法/本地PCC策略配置/配置示例_19416800.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/典型业务场景_59651633.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/5GC网元调测版本配套说明_30866774.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/业务重定向方案（预定义+动态）/E2E业务调测/动态规则场景调测/信令调测方法_08571768.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/业务重定向方案（预定义+动态）/E2E业务调测/动态规则场景调测/快速调测方法_08571789.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/业务重定向方案（预定义+动态）/E2E业务调测/预定义规则场景调测/信令调测方法_24674052.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/业务重定向方案（预定义+动态）/E2E业务调测/预定义规则场景调测/快速调测方法_71233851.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/业务重定向方案（预定义+动态）/E2E业务配置/E2E动态规则配置/PCF侧业务配置_08571786.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/业务重定向方案（预定义+动态）/E2E业务配置/E2E预定义规则配置/PCF侧业务配置_71193959.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/业务重定向方案（预定义+动态）/E2E业务配置/E2E预定义规则配置/SMF侧业务配置_71233849.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/业务重定向方案（预定义+动态）/E2E业务配置/E2E预定义规则配置/UPF侧业务配置_24674050.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/业务重定向方案（预定义+动态）/整体方案设计_08571784.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/业务重定向方案（预定义+动态）/需求描述_08571766.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于业务类别的带宽差异化控制方案设计（ADC）/E2E业务调测/信令调测方法_08571742.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于业务类别的带宽差异化控制方案设计（ADC）/E2E业务调测/快速调测方法_08571775.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于业务类别的带宽差异化控制方案设计（ADC）/E2E业务配置/PCF侧业务配置_08571772.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于业务类别的带宽差异化控制方案设计（ADC）/E2E业务配置/SMF侧业务配置_13928808.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于业务类别的带宽差异化控制方案设计（ADC）/E2E业务配置/UPF侧业务配置_13928809.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于业务类别的带宽差异化控制方案设计（ADC）/整体方案设计_08571770.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于业务类别的带宽差异化控制方案设计（ADC）/需求描述_08571740.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于位置区域的带宽差异化控制方案（预定义）/E2E业务调测/信令调测方法_08571765.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于位置区域的带宽差异化控制方案（预定义）/E2E业务调测/快速调测方法_08571782.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于位置区域的带宽差异化控制方案（预定义）/E2E业务配置/PCF侧业务配置_08571779.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于位置区域的带宽差异化控制方案（预定义）/E2E业务配置/SMF侧业务配置_08571780.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于位置区域的带宽差异化控制方案（预定义）/E2E业务配置/UPF侧业务配置_22160708.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于位置区域的带宽差异化控制方案（预定义）/整体方案设计_08571777.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于位置区域的带宽差异化控制方案（预定义）/需求描述_08571743.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于多业务场景的策略控制（动态）/E2E业务调测/信令调测方法_24058838.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于多业务场景的策略控制（动态）/E2E业务调测/快速调测方法_23899010.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于多业务场景的策略控制（动态）/E2E业务配置/业务1配置_23899008.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于多业务场景的策略控制（动态）/E2E业务配置/业务2配置_71231363.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于多业务场景的策略控制（动态）/E2E业务配置/套餐配置_24671552.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于多业务场景的策略控制（动态）/整体方案设计/PCF侧业务设计_24667722.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于多业务场景的策略控制（动态）/整体方案设计/整体拆解逻辑_71227537.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于多业务场景的策略控制（动态）/需求描述_24058834.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于用户等级的资费差异化控制方案（动态）/E2E业务调测/信令调测方法_08571739.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于用户等级的资费差异化控制方案（动态）/E2E业务调测/快速调测方法_93907887.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于用户等级的资费差异化控制方案（动态）/E2E业务配置/PCF侧业务配置_93906534.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于用户等级的资费差异化控制方案（动态）/整体方案设计_93907864.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于用户等级的资费差异化控制方案（动态）/需求描述_08571737.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/整体介绍_86483627.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/遵循标准_11969175.md
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/阅读指引_50304906.md
```

---

## Section 3: 5G基础知识概念文档（等权重）

### UDG - QoS概念 (1 files)

```
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/QoS/QoS_42268275.md
```

---

### UDG - 业务感知（SA）解读 (6 files)

```
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：业务感知（SA）/业务感知原理——How？/业务感知概览_32946283.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：业务感知（SA）/业务感知原理——How？/业务感知流程_85850060.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：业务感知（SA）/业务感知原理——How？/相关概念_86169670.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：业务感知（SA）/何为业务感知——What？_86009700.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：业务感知（SA）/使用业务感知——Why？_32687383.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：业务感知（SA）/结语_32789113.md
```

---

### UDG - PCC策略之E2E QoS管理机制 (7 files)

```
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/SM策略之QoS的管理机制/SM策略之QoS的下发与执行_33030755.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/SM策略之QoS的管理机制/SM策略之QoS的更新、下发与执行/PCF发起的策略更新_86168492.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/SM策略之QoS的管理机制/SM策略之QoS的更新、下发与执行/SMF发起的策略更新_85720414.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/SM策略之QoS的管理机制/SM策略之QoS的更新、下发与执行/更新后的QoS策略下发与执行_86008546.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/SM策略之QoS的管理机制/SM策略之QoS的生成_85848900.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/SM策略之QoS的管理机制_32686211.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制_32945129.md
```

---

### UDG - PCC策略之静态规则解读 (4 files)

```
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读 -5G PCC策略之静态规则解读/PCC静态规则原理——How？_86009740.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读 -5G PCC策略之静态规则解读/何为PCC静态规则——What？_86169704.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读 -5G PCC策略之静态规则解读/使用PCC静态规则——Why？_32946325.md
output/UDG_Product_Documentation_CH_20.15.2/5G基础知识/一望5G/5G Core业务解决方案解读 -5G PCC策略之静态规则解读/结语_33031965.md
```

---

### UNC - QoS概念 (1 files)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/QoS/QoS_42268275.md
```

---

### UNC - 业务感知（SA）解读 (6 files)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：业务感知（SA）/业务感知原理——How？/业务感知概览_32946283.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：业务感知（SA）/业务感知原理——How？/业务感知流程_85850060.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：业务感知（SA）/业务感知原理——How？/相关概念_86169670.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：业务感知（SA）/何为业务感知——What？_86009700.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：业务感知（SA）/使用业务感知——Why？_32687383.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：业务感知（SA）/结语_32789113.md
```

---

### UNC - PCC策略之E2E QoS管理机制 (7 files)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/SM策略之QoS的管理机制/SM策略之QoS的下发与执行_33030755.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/SM策略之QoS的管理机制/SM策略之QoS的更新、下发与执行/PCF发起的策略更新_86168492.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/SM策略之QoS的管理机制/SM策略之QoS的更新、下发与执行/SMF发起的策略更新_85720414.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/SM策略之QoS的管理机制/SM策略之QoS的更新、下发与执行/更新后的QoS策略下发与执行_86008546.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/SM策略之QoS的管理机制/SM策略之QoS的生成_85848900.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制/SM策略之QoS的管理机制_32686211.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/5G PCC策略—E2E QoS管理机制_32945129.md
```

---

### UNC - PCC策略之静态规则解读 (4 files)

```
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之静态规则解读/PCC静态规则原理——How？_86009740.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之静态规则解读/何为PCC静态规则——What？_86169704.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之静态规则解读/使用PCC静态规则——Why？_32946325.md
output/UNC 20.15.2 产品文档(裸机容器) 05/5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之静态规则解读/结语_33031965.md
```

---

## Section 4: 排除说明

### 4.1 命令文档（不单独读取）

- `output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/`
- `output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/`
- 说明：用户指定命令不单独读取；如需命令细节，从特性文档中提取。

### 4.2 与带宽控制无关的业务专题

UDG排除的业务专题：
- 5G Core 计费解决方案（已纳入计费场景）
- 5G Core IPv6组网解决方案（组网相关，非带宽）
- 5G Core 国际漫游解决方案（漫游相关，非带宽）
- 5G Core 流控解决方案（如有，信令流控非用户面带宽）
- 5G Core 媒体中继解决方案（媒体中继，非带宽）
- 5G Core 容灾解决方案（容灾相关）
- 5G Core 用户IP地址管理解决方案（地址管理）
- 5G Core 智家随行解决方案（智家专用）
- UDG NAT/UDG SFIP/UDG vTCP_OPT/UDG报表/UDG防欺诈/UDG头增强 功能专题（与带宽无关）

UNC排除的业务专题：
- 5G Core 4_5G互操作解决方案（互操作）
- 5G Core IPv6组网解决方案（组网）
- 5G Core NRF解决方案（NRF）
- 5G Core ULCL分流解决方案（ULCL，属于第三子场景：访问限制/分流）
- 5G Core 计费解决方案（已纳入计费场景）
- 5G Core 流控解决方案（信令流控，非用户面带宽）
- 5G Core 容灾解决方案（容灾）
- 5G Core 用户IP地址管理解决方案（地址管理）
- 5GC国际漫游解决方案（漫游）
- UNC UPF选择/UNC接入控制/UNC网元选择 专题（接入控制属于第三子场景）

### 4.3 边界判断

**纳入带宽控制场景**：
- 用户面带宽限制/整形（Shaping、Policing、BWM）
- 累计流量触发带宽重定向（FUP）
- GBR保障（保证比特速率，带宽下限）
- 业务触发QoS（专用承载，间接影响带宽）
- ADC（应用检测控制，触发带宽策略）
- PCC/SA基础框架（带宽控制依赖的底座）

**未纳入（属于其他子场景）**：
- 访问限制（URL过滤、重定向、阻塞）→ 第三子场景
- 接入控制（APN接入、UPF选择）→ 第三子场景
- 纯信令流控（NRF/AMF/SMF流控）→ 不属于业务感知
