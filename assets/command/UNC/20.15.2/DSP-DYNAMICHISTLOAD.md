---
id: UNC@20.15.2@MMLCommand@DSP DYNAMICHISTLOAD
type: MMLCommand
name: DSP DYNAMICHISTLOAD（显示各业务pod历史的忙时负载、权重和部署位置信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DYNAMICHISTLOAD
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 权重分配管理
- 展示动态权重信息
status: active
---

# DSP DYNAMICHISTLOAD（显示各业务pod历史的忙时负载、权重和部署位置信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询指定的服务类型的业务pod近七天的忙时负载、权重和部署位置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务类型，查看对应的Token、权重和负载信息。<br>数据来源：本端规划<br>取值范围：1.UAM会话管理组（UEAM与UEM） 2. USM会话管理服务（UESM、SMC、UPC、SM5GCM、STG、SM5GPOLICY）<br>- “UAM_0（UAM_0）”：涉及如下类型POD：接入/移动性管理POD。<br>- “USM_0（USM_0）”：涉及如下类型POD：会话管理POD。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [各业务pod历史的忙时负载、权重和部署位置信息（DYNAMICHISTLOAD）](configobject/UNC/20.15.2/DYNAMICHISTLOAD.md)

## 使用实例

查询“服务类型”为“UAM_0”的pod的动态权重信息，执行如下命令：

```
%%DSP DYNAMICHISTLOAD
: SERVICETYPE=UAM_0;%%
RETCODE = 0  操作成功

结果如下
--------
服务类型  日期  POD名称  Node ID  Host ID  忙时时间段  忙时负载  权重  TOKEN数量
UAM_0  2022-04-24  usn-pod-0  192.168.1.4  192.168.1.5  19:30:22  65  1.000  1500
(结果个数 = 1)

---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示各业务pod历史的忙时负载、权重和部署位置信息（DSP-DYNAMICHISTLOAD）_51175617.md`
