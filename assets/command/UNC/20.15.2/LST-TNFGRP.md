---
id: UNC@20.15.2@MMLCommand@LST TNFGRP
type: MMLCommand
name: LST TNFGRP（查询目标NF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TNFGRP
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
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
- 目标NF组管理
status: active
---

# LST TNFGRP（查询目标NF组）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用于查询目标NF组的配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNFTYPE | 目标NF类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF组内的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “CHF（CHF）”：CHF<br>- “UPF（UPF）”：UPF<br>- “PCSCF（PCSCF）”：PCSCF<br>- “PCF（PCF）”：PCF<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TNFGRP]] · 目标NF组（TNFGRP）

## 使用实例

运营商A需要查询TNFTYPE为CHF的目标NF组信息。

```
%%LST TNFGRP:;%%
RETCODE = 0  操作成功

结果如下
--------
  目标NF类型  =  CHF
目标NF组索引  =  1
目标NF组名称  =  CHF_GROUP_0
( 结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-TNFGRP.md`
