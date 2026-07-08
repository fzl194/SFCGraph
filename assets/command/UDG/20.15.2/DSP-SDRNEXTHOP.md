---
id: UDG@20.15.2@MMLCommand@DSP SDRNEXTHOP
type: MMLCommand
name: DSP SDRNEXTHOP（查询SDRC中缓存的下一跳信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRNEXTHOP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRNEXTHOP（查询SDRC中缓存的下一跳信息）

## 功能

该命令用于查询SDRC中缓存的下一跳信息，需要用户指定APPTYPE以及相应的下一跳组ID。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPTYPE | App类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示业务类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| NEXTHOPGROUPID | 下一跳组ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示下一跳组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SDRC中缓存的下一跳信息（SDRNEXTHOP）](configobject/UDG/20.15.2/SDRNEXTHOP.md)

## 使用实例

使用如下命令查询指定APPTYPE和下一跳组中的下一跳信息：

```
%%DSP SDRNEXTHOP: APPTYPE=140, NEXTHOPGROUPID=65;%%
RETCODE = 0  操作成功

结果如下
--------
App 类型  下一跳组ID  下一跳索引  FABRIC TB  FABRIC TP    

140      65          1           1119      2217811712  
140      65          0           1107      2217811712  
(结果个数 = 2)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SDRC中缓存的下一跳信息（DSP-SDRNEXTHOP）_94730430.md`
