---
id: UNC@20.15.2@MMLCommand@ADD STATICWTPOLICY
type: MMLCommand
name: ADD STATICWTPOLICY（增加服务类型在POD实例下的静态权重）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: STATICWTPOLICY
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 权重分配管理
- 静态权重策略
status: active
---

# ADD STATICWTPOLICY（增加服务类型在POD实例下的静态权重）

## 功能

![](增加服务类型在POD实例下的静态权重（ADD STATICWTPOLICY）_51175613.assets/notice_3.0-zh-cn_2.png)

如果配置不合理会导致不同POD间负载不均衡。

**适用NF：SGW-C、PGW-C、SMF、GGSN、AMF**

该命令用于增加服务类型在POD实例下的静态权重。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入4096条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>使用DSP POD命令查询sm/am的pod Name。 |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务类型，配置对应的Token权重。<br>数据来源：本端规划<br>取值范围：<br>- “UAM_0（UAM_0）”：涉及如下类型POD：接入/移动性管理POD。<br>- “USM_0（USM_0）”：涉及如下类型POD：会话管理POD。<br>默认值：无<br>配置原则：无 |
| STATICWEIGHT | 静态权重 | 可选必选说明：必选参数<br>参数含义：该参数用于配置该服务类型在该POD实例下的静态权重。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是700~1300。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/STATICWTPOLICY]] · 服务类型在POD实例下的静态权重（STATICWTPOLICY）

## 使用实例

对POD名称为xxx，服务类型为USM_0，增加权重1000：

```
ADD STATICWTPOLICY:PODNAME="XXX",SERVICETYPE=USM_0,STATICWEIGHT=1000,CONFIRM=Y;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加服务类型在POD实例下的静态权重（ADD-STATICWTPOLICY）_51175613.md`
