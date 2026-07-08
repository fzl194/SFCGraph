---
id: UNC@20.15.2@MMLCommand@LST TNFBINDGRP
type: MMLCommand
name: LST TNFBINDGRP（查询目标NF实例绑定组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TNFBINDGRP
command_category: 查询类
applicable_nf:
- SMF
- NCG
- SMSF
effect_mode: ''
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

# LST TNFBINDGRP（查询目标NF实例绑定组）

## 功能

**适用NF：SMF、NCG、SMSF**

该命令用于查询目标NF组绑定信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNFGRPINDEX | 目标NF组索引 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF组索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~511。<br>默认值：无<br>配置原则：<br>本参数需要与ADD TNFGRP命令中的TNFGRPINDEX值保持一致。 |
| TNFINSINDEX | 目标NF实例索引 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF实例索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2047。<br>默认值：无<br>配置原则：<br>本参数需要与ADD TNFINS命令中的TNFINSINDEX值保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TNFBINDGRP]] · 目标NF实例绑定组（TNFBINDGRP）

## 使用实例

运营商A需要查询索引为0的目标NF组的绑定信息。

```
%%LST TNFBINDGRP:;%%
RETCODE = 0 操作成功

结果如下：
------------------------
    目标NF组索引 = 0
  目标NF实例索引 = 1
          优先级 = 1
            权重 = 50
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询目标NF实例绑定组（LST-TNFBINDGRP）_09651395.md`
