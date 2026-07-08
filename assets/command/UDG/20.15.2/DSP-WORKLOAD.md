---
id: UDG@20.15.2@MMLCommand@DSP WORKLOAD
type: MMLCommand
name: DSP WORKLOAD（查询系统负载）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: WORKLOAD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 资源管理
- VM负载管理
status: active
---

# DSP WORKLOAD（查询系统负载）

## 功能

该命令用来查看VNFC下所有ScaleGroup的负载。当前VNFC的负载是由多项指标（内存指标、CPU指标）中取最高值得到的。其中内存指标是业务上报的多个内存相关的百分比中的最高值；CPU指标为对应ScaleGroup下所有RU的CPU占用率的平均值。

该命令在合一KPI模式下使用，在多KPI模式下不使用。查询KPI模式，请通过命令查看。

## 注意事项

- 无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识，不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的RU状态查询。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@WORKLOAD]] · 系统负载（WORKLOAD）

## 使用实例

查看VNFC负载。

```
DSP WORKLOAD:
SERVICEINSTANCE="CSLB_VNFC_999"
;
```

```
RETCODE = 0  操作成功。

结果如下
--------
ScaleGroup的名字  =  SG0_CSLB_IPFWD
        VNFC的ID  =  2
        VNFC负载  =  12%
(结果个数 = 1)
---    END 
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-WORKLOAD.md`
