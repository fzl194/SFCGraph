---
id: UNC@20.15.2@MMLCommand@ADD TNFBINDGRP
type: MMLCommand
name: ADD TNFBINDGRP（增加目标NF实例绑定组）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD TNFBINDGRP（增加目标NF实例绑定组）

## 功能

**适用NF：SMF、NCG、SMSF**

该命令用于增加目标NF实例绑定目标NF组的配置。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入4096条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNFGRPINDEX | 目标NF组索引 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF组索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~511。<br>默认值：无<br>配置原则：<br>本参数需要与ADD TNFGRP命令中的TNFGRPINDEX值保持一致。 |
| TNFINSINDEX | 目标NF实例索引 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF实例索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2047。<br>默认值：无<br>配置原则：<br>本参数需要与ADD TNFINS命令中的TNFINSINDEX值保持一致。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF的优先级（与其他同类型NF实例相比）。在NF选择过程中，NF会选择高优先级的NF，如果两个或多个NF的优先级一样，NF则会根据“权重”做进一步的判断。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。值越小优先级越高。<br>默认值：10<br>配置原则：无 |
| WEIGHT | 权重 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF的相对权重（与其他同类型NF实例相比）。特别地，如果NF权重的绝对值不超过本参数的取值范围，那么本参数可以直接取用权重绝对值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。值越大表示权重越大。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [目标NF实例绑定组（TNFBINDGRP）](configobject/UNC/20.15.2/TNFBINDGRP.md)

## 使用实例

运营商A需要将索引1的目标NF添加到索引为0的目标NF组中，优先级为1，权重为50。

```
ADD TNFBINDGRP: TNFGRPINDEX=0, TNFINSINDEX=1, PRIORITY=1, WEIGHT=50;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加目标NF实例绑定组（ADD-TNFBINDGRP）_09651533.md`
