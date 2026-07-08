---
id: UDG@20.15.2@MMLCommand@SET SPECTRAFURRGRP
type: MMLCommand
name: SET SPECTRAFURRGRP（设置全局缺省费率的流量使用量上报规则组）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SPECTRAFURRGRP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 特殊流量使用量上报规则组
status: active
---

# SET SPECTRAFURRGRP（设置全局缺省费率的流量使用量上报规则组）

## 功能

**适用NF：PGW-U、UPF**

![](设置全局缺省费率的流量使用量上报规则组（SET SPECTRAFURRGRP）_36146715.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，修改URRGROUPNAME参数会导致计费使用的全局缺省费率变化或业务不计费，造成运营商计费损失。

本命令用于设置全局缺省费率的流量使用量上报规则组。

1、BIT1232软参值设置为1时，特殊流量通过该规则组进行计费。

特殊流量是指当某些业务报文丢失，未能完成七层精确匹配时，已经转发的流量。

例如，在线计费用户下线时，业务流只有信令报文，没有业务报文。在这种场景下，已经转发的信令报文的流量称为特殊流量。

2、对于没有配置任何费率的业务场景，通过该规则组进行计费。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 设置URRGROUPNAME参数时需要使用ADD URRGROUP命令配置费率组。
- 修改URRGROUPNAME参数会导致计费使用的全局缺省费率变化或业务不计费，造成运营商计费损失。
- 该命令仅支持时长和流量的计费方式，不支持基于事件的计费方式。
- 如果该命令绑定的URR出现欠费，则会影响特殊流量使用量的上报。
- 该命令不区分业务费率和信令费率。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| URRGROUPNAME | 特殊流量使用量上报规则组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置全局缺省费率的流量使用量上报规则组的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SPECTRAFURRGRP]] · 全局缺省费率的流量使用量上报规则组（SPECTRAFURRGRP）

## 使用实例

假如用户想要配置全局缺省费率的流量使用量上报规则组spec：

```
SET SPECTRAFURRGRP: URRGROUPNAME="spec";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置全局缺省费率的流量使用量上报规则组（SET-SPECTRAFURRGRP）_36146715.md`
