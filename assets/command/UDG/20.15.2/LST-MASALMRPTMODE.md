---
id: UDG@20.15.2@MMLCommand@LST MASALMRPTMODE
type: MMLCommand
name: LST MASALMRPTMODE（查询5G告警上报模式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MASALMRPTMODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 告警管理
- 告警上报模式
status: active
---

# LST MASALMRPTMODE（查询5G告警上报模式）

## 功能

该命令用于查询5G告警上报模式及相关参数。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALMTYPE | 告警类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定告警类型。<br>数据来源：本端规划<br>取值范围：<br>- “HTTP_LINKDOWN（HTTP链路故障）”：表示ALM-100155 HTTP链路故障告警，对应的批量告警为ALM-100311 批量HTTP链路故障。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MASALMRPTMODE]] · 5G告警上报模式（MASALMRPTMODE）

## 使用实例

查询系统中，ALM-100155 HTTP链路故障的告警上报模式：

```
LST MASALMRPTMODE: ALMTYPE=HTTP_LINKDOWN;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-MASALMRPTMODE.md`
