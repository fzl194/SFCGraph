---
id: UNC@20.15.2@MMLCommand@LST STATICWTPOLICY
type: MMLCommand
name: LST STATICWTPOLICY（查询服务类型在POD实例下的静态权重）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: STATICWTPOLICY
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 权重分配管理
- 静态权重策略
status: active
---

# LST STATICWTPOLICY（查询服务类型在POD实例下的静态权重）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN、AMF**

该命令用于查询静态权重配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>使用DSP POD命令查询sm/am的pod Name。 |
| SERVICETYPE | 服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务类型，配置对应的Token权重。<br>数据来源：本端规划<br>取值范围：<br>- “UAM_0（UAM_0）”：涉及如下类型POD：接入/移动性管理POD。<br>- “USM_0（USM_0）”：涉及如下类型POD：会话管理POD。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [服务类型在POD实例下的静态权重（STATICWTPOLICY）](configobject/UNC/20.15.2/STATICWTPOLICY.md)

## 使用实例

- 查询所有的静态权重策略：
  ```
  LST STATICWTPOLICY:;
  ```
- 查询POD Name为xxx，服务类型为USM_0的静态权重：
  ```
  LST STATICWTPOLICY:PODNAME="xxx",SERVICETYPE=USM_0;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务类型在POD实例下的静态权重（LST-STATICWTPOLICY）_51335393.md`
