---
id: UDG@20.15.2@MMLCommand@SET IPV6PARA
type: MMLCommand
name: SET IPV6PARA（设置IPv6参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IPV6PARA
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 资源管理
- IPv6Pmtu管理
status: active
---

# SET IPV6PARA（设置IPv6参数）

## 功能

该命令用于设置IPv6功能参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PMTUAGINGTIMER | PMTU老化时长 | 可选必选说明：必选参数。<br>参数含义：设置PMTU（Path Maximum Transmission Unit）缓存数据老化时长，单位为天。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～365。<br>系统设置初始值：1<br>默认值：无<br>配置原则：<br>- 0：关闭PMTU缓存数据老化功能。如果IP或端口经常变化，会导致PMTU缓存数据持续增长，存在PMTU缓存数据过载的风险。<br>- 1～365：PMTU缓存数据老化时长。PMTU缓存记录老化超时，会清除PMTU缓存数据，对应的IPv6网络路径使用系统默认PMTU发送消息。如果网络路径上的路由器不支持此默认PMTU，会导致短暂丢包。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的VNFC进行配置。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPV6PARA]] · IPv6参数（IPV6PARA）

## 使用实例

设置IPv6功能参数， “PMTU老化时长” 为3天：

SET IPV6PARA: PMTUAGINGTIMER=3 , SERVICEINSTANCE="CSLB_VNFC_999" ;

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-IPV6PARA.md`
