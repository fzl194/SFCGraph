---
id: UNC@20.15.2@MMLCommand@DSP RUCPUUSGTHRESH
type: MMLCommand
name: DSP RUCPUUSGTHRESH（查询RU CPU占用率、告警上报门限和告警恢复门限）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RUCPUUSGTHRESH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 资源管理
- RU信息
status: active
---

# DSP RUCPUUSGTHRESH（查询RU CPU占用率、告警上报门限和告警恢复门限）

## 功能

该命令用于查询某个RU的CPU占用率、告警上报门限和告警恢复门限。

## 注意事项

该命令只适用于查询非主控的RU的CPU信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU的ID | 可选必选说明：必选参数。<br>参数含义：表示资源单元的ID号。通过<br>**[LST SERVICERUSTATE](查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>命令可以查询RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识，不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的RU状态查询。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RUCPUUSGTHRESH]] · RU CPU占用率、告警上报门限和告警恢复门限（RUCPUUSGTHRESH）

## 使用实例

查询 “RU的ID” 为64的CPU占用率及过载告警上报门限和告警恢复门限:

DSP RUCPUUSGTHRESH:RUID=64 , SERVICEINSTANCE="CSLB_VNFC_999" ;

```
%%/*4191*/DSP RUCPUUSGTHRESH:RUID=64
, SERVICEINSTANCE="CSLB_VNFC_999"
;%%
RETCODE = 0   操作成功。

结果如下
--------
告警上报门限  =  80
告警恢复门限  =  70
   CPU占用率  =  35
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RUCPUUSGTHRESH.md`
