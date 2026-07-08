---
id: UDG@20.15.2@MMLCommand@SET CMFFC
type: MMLCommand
name: SET CMFFC（设置CMF流控参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CMFFC
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET CMFFC（设置CMF流控参数）

## 功能

![](设置CMF流控参数（SET CMFFC）_68820021.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置小于默认值可能会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置开启CMF流控的CPU阈值、停止CMF流控的CPU阈值和停控时间窗。

> **说明**
> - 该命令执行后立即生效。
>
> - CMF Pod单节点部署时不支持CMF流控，第三方CaaS场景不支持CMF流控，CSPEdge裸机场景不支持CMF流控。
> - 未执行本命令时，CMF流控参数默认配置为代码默认值，可通过[**DSP DBGHAFD**](显示HAFD调试命令结果（DSP DBGHAFD）_94730404.md)命令查询实际运行的值。查询时，参数DEBUGNAME取值为"cmf fc config"。
> - 配置修改可能会导致系统故障，建议保持参数初始设置值不变。
> - 如需修改，要求二级起控阈值大于二级停控阈值，二级停控阈值大于等于一级起控阈值，一级起控阈值大于一级停控阈值，停控时间窗取值范围在5-120秒之间。
> - 首次执行该命令不允许缺省参数，否则将导致命令下发失败。
> - 执行该命令时，有参数取值为0，将导致配置下发失败。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | FCTYPE | LOWSTARTTH | LOWSTOPTH | HIGHSTARTTH | HIGHSTOPTH | DELAYTIME |
> | --- | --- | --- | --- | --- | --- |
> | POD | 0 | 0 | 0 | 0 | 0 |
> | RESOURCEBOX | 0 | 0 | 0 | 0 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCTYPE | 流控功能类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示CMF流控功能类型。<br>数据来源：本端规划<br>取值范围：<br>- “POD（POD）”：CMF Pod触发的CMF流控。<br>- “RESOURCEBOX（RESOURCEBOX）”：虚机场景表示CMF Pod所在节点触发CMF流控；FST裸机场景表示CMF Pod关联的SuperPod触发CMF流控；其他场景无流控功能。<br>默认值：无。<br>配置原则：无 |
| LOWSTARTTH | 一级起控阈值(%) | 可选必选说明：可选参数<br>参数含义：该参数用于表示触发CMF一级流控的CPU阈值。当流控功能类型为POD时，该参数为CMF Pod的CPU值；当流控功能类型为RESOURCEBOX时，在虚机场景中为CMF Pod所在节点的CPU值，在FST裸机场景中为CMF Pod所关联SuperPod的CPU值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CMFFC查询当前参数配置值。<br>配置原则：无 |
| LOWSTOPTH | 一级停控阈值(%) | 可选必选说明：可选参数<br>参数含义：该参数用于表示停止CMF一级流控的CPU阈值。当流控功能类型为POD时，该参数为CMF Pod的CPU值；当流控功能类型为RESOURCEBOX时，在虚机场景中为CMF Pod所在节点的CPU值，在FST裸机场景中为CMF Pod所关联SuperPod的CPU值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CMFFC查询当前参数配置值。<br>配置原则：无 |
| HIGHSTARTTH | 二级起控阈值(%) | 可选必选说明：可选参数<br>参数含义：该参数用于表示触发CMF二级流控的CPU阈值。当流控功能类型为POD时，该参数为CMF Pod的CPU值；当流控功能类型为RESOURCEBOX时，在虚机场景中为CMF Pod所在节点的CPU值，在FST裸机场景中为CMF Pod所关联SuperPod的CPU值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CMFFC查询当前参数配置值。<br>配置原则：无 |
| HIGHSTOPTH | 二级停控阈值(%) | 可选必选说明：可选参数<br>参数含义：该参数用于表示停止CMF二级流控的CPU阈值。当流控功能类型为POD时，该参数为CMF Pod的CPU值；当流控功能类型为RESOURCEBOX时，在虚机场景中为CMF Pod所在节点的CPU值，在FST裸机场景中为CMF Pod所关联SuperPod的CPU值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CMFFC查询当前参数配置值。<br>配置原则：无 |
| DELAYTIME | 停控时间窗(s) | 可选必选说明：可选参数<br>参数含义：该参数用于表示CMF流控停止所需要的时间窗阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~120，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CMFFC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CMFFC]] · CMF流控参数（CMFFC）

## 使用实例

- 配置流控功能类型为POD，一级起控阈值为75%，一级停控阈值为70%，二级起控阈值为80%，二级停控阈值为75%，停控时间窗为30秒。
  ```
  SET CMFFC: FCTYPE=POD, LOWSTARTTH=75, LOWSTOPTH=70, HIGHSTARTTH=80, HIGHSTOPTH=75, DELAYTIME=30;
  ```
- 配置流控功能类型为RESOURCEBOX，一级起控阈值为95%，一级停控阈值为90%，二级起控阈值为98%，二级停控阈值为95%，停控时间窗为15秒。
  ```
  SET CMFFC: FCTYPE=RESOURCEBOX, LOWSTARTTH=95, LOWSTOPTH=90, HIGHSTARTTH=98, HIGHSTOPTH=95, DELAYTIME=15;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置CMF流控参数（SET-CMFFC）_68820021.md`
