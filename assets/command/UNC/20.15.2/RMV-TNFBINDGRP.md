---
id: UNC@20.15.2@MMLCommand@RMV TNFBINDGRP
type: MMLCommand
name: RMV TNFBINDGRP（删除目标NF实例绑定组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TNFBINDGRP
command_category: 配置类
applicable_nf:
- SMF
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
- 目标NF实例绑定组管理
status: active
---

# RMV TNFBINDGRP（删除目标NF实例绑定组）

## 功能

**适用NF：SMF、NCG、SMSF**

该命令用于删除目标NF实例绑定目标NF组的配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNFGRPINDEX | 目标NF组索引 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF组索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~511。<br>默认值：无<br>配置原则：<br>本参数需要与ADD TNFGRP命令中的TNFGRPINDEX值保持一致。 |
| TNFINSINDEX | 目标NF实例索引 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF实例索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2047。<br>默认值：无<br>配置原则：<br>本参数需要与ADD TNFINS命令中的TNFINSINDEX值保持一致。 |

## 操作的配置对象

- [目标NF实例绑定组（TNFBINDGRP）](configobject/UNC/20.15.2/TNFBINDGRP.md)

## 使用实例

运营商A需要将索引1的目标NF从索引为0的目标NF组中移除。

```
RMV TNFBINDGRP: TNFGRPINDEX=0, TNFINSINDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除目标NF实例绑定组（RMV-TNFBINDGRP）_09653620.md`
