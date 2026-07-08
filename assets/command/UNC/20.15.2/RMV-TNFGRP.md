---
id: UNC@20.15.2@MMLCommand@RMV TNFGRP
type: MMLCommand
name: RMV TNFGRP（删除目标NF组）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV TNFGRP（删除目标NF组）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用于删除目标NF组的配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNFGRPINDEX | 目标NF组索引 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF组索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~511。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TNFGRP]] · 目标NF组（TNFGRP）

## 使用实例

运营商A需要删除TNFGRPINDEX为0的目标NF组信息。

```
RMV TNFGRP: TNFGRPINDEX=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除目标NF组（RMV-TNFGRP）_09652293.md`
