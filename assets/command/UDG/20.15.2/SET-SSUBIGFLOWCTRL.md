---
id: UDG@20.15.2@MMLCommand@SET SSUBIGFLOWCTRL
type: MMLCommand
name: SET SSUBIGFLOWCTRL（设置智能板的大流判断速率阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SSUBIGFLOWCTRL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 智能板管理
- vvip
- 大流控制速率
status: active
---

# SET SSUBIGFLOWCTRL（设置智能板的大流判断速率阈值）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置智能板的大流判断速率阈值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | VVIPFLOWRATE | CCOFLOWRATE |
| --- | --- | --- |
| 初始值 | 800 | 800 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VVIPFLOWRATE | VVIP业务大流速率（千比特/秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置智能板VVIP业务大流速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1～4294967295，单位为千比特/秒。<br>默认值：无<br>配置原则：无 |
| CCOFLOWRATE | CCO业务大流速率（千比特/秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置CCO业务大流速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1～4294967295，单位为千比特/秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SSUBIGFLOWCTRL]] · 智能板的大流判断速率阈值（SSUBIGFLOWCTRL）

## 使用实例

设置智能板的大流判断速率阈值：

```
SET SSUBIGFLOWCTRL: VVIPFLOWRATE=1000, CCOFLOWRATE=2000;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SSUBIGFLOWCTRL.md`
