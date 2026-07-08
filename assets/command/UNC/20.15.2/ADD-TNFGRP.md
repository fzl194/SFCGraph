---
id: UNC@20.15.2@MMLCommand@ADD TNFGRP
type: MMLCommand
name: ADD TNFGRP（增加目标NF组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TNFGRP
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 目标NF组管理
status: active
---

# ADD TNFGRP（增加目标NF组）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用于增加目标NF组的配置。

目标NF组是由一个或者多个NF实例组成的负荷分担的集群，可以为特定用户群（比如指定号段、指定位置、请求DNN等）提供业务接入服务。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入512条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNFGRPINDEX | 目标NF组索引 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF组索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~511。<br>默认值：无<br>配置原则：无 |
| TNFTYPE | 目标NF类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF组内的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “CHF（CHF）”：CHF<br>- “UPF（UPF）”：UPF<br>- “PCSCF（PCSCF）”：PCSCF<br>- “PCF（PCF）”：PCF<br>默认值：无<br>配置原则：无 |
| TNFGRPNAME | 目标NF组名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [目标NF组（TNFGRP）](configobject/UNC/20.15.2/TNFGRP.md)

## 使用实例

运营商A需要添加目标NF组信息：TNFGRPINDEX为0，TNFTYPE为CHF，TNFGRPNAME为CHF_GROUP_0。

```
ADD TNFGRP: TNFGRPINDEX=0, TNFTYPE=CHF, TNFGRPNAME="CHF_GROUP_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加目标NF组（ADD-TNFGRP）_09651791.md`
