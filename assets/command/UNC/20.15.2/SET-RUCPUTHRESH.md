---
id: UNC@20.15.2@MMLCommand@SET RUCPUTHRESH
type: MMLCommand
name: SET RUCPUTHRESH（设置RU CPU占用率告警上报门限和告警恢复门限）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: RUCPUTHRESH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 资源管理
- RU配置
status: active
---

# SET RUCPUTHRESH（设置RU CPU占用率告警上报门限和告警恢复门限）

## 功能

该命令用于配置“ALM-82802 RU CPU过载”的CPU过载告警上报门限和告警恢复门限。

## 注意事项

- 该命令执行后，会直接恢复已经上报的告警。
- 该命令执行后立即生效。
- 该命令只对非主控的RU生效。
- 如果命令输入“RU的ID”在记录中不存在，则返回无记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU的ID | 可选必选说明：必选参数。<br>参数含义：表示资源单元的ID。通过<br>**[LST SERVICERUSTATE](../RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>命令可以查询RU的ID<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>系统设置初始值：无<br>默认值：无 |
| WARNTHRESH | 告警上报门限 | 可选必选说明：必选参数。<br>参数含义：CPU过载告警的上报门限，RU的CPU占用率持续超过2分钟高于该数值则上报RU CPU过载告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100，单位为%。<br>系统设置初始值 (CSLB_VNFC)：85<br>系统设置初始值 (其他VNFC类型)：80<br>默认值：无<br>配置原则：<br>“告警上报门限”<br>必须大于<br>“告警恢复门限”<br>。如果CSLB_VNFC设置的告警上报门限低于81，会在RU复位后恢复成初始值85。 |
| RECVTHRESH | 告警恢复门限 | 可选必选说明：必选参数。<br>参数含义：CPU过载告警的恢复门限，RU的CPU占用率一旦低于该数值则恢复告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100，单位为%。<br>系统设置初始值：70<br>默认值：无<br>配置原则：<br>“告警恢复门限”<br>必须小于<br>“告警上报门限”<br>。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识，不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的RU状态查询。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RUCPUTHRESH]] · RU CPU占用率告警上报门限和告警恢复门限（RUCPUTHRESH）

## 使用实例

设置 “RU的ID” 为64的CPU过载告警上报门限和告警恢复门限：

SET RUCPUTHRESH: RUID = 64,WARNTHRESH = 90,RECVTHRESH = 60 ,SERVICEINSTANCE="CSLB_VNFC_999" ;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置RU-CPU占用率告警上报门限和告警恢复门限(SET-RUCPUTHRESH)_29626959.md`
