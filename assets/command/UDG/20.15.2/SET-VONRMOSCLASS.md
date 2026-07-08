---
id: UDG@20.15.2@MMLCommand@SET VONRMOSCLASS
type: MMLCommand
name: SET VONRMOSCLASS（配置MOS分类的区间值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: VONRMOSCLASS
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- VoNR质量监控配置
- VoNR MOS分类
status: active
---

# SET VONRMOSCLASS（配置MOS分类的区间值）

## 功能

**适用NF：UPF**

该命令用于设置MOS分类区间边界值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 配置的四个参数的值必须满足MOS值为excellent和good之间的边界值大于MOS值为good和accept之间的边界值，MOS值为good和accept之间的边界值大于MOS值为accept和poor之间的边界值，MOS值为accept和poor之间的边界值大于MOS值为poor和bad之间的边界值。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | MOSEXECGOOD | MOSGOODACCP | MOSACCPPOOR | MOSPOORBAD |
| --- | --- | --- | --- | --- |
| 初始值 | 40 | 36 | 31 | 26 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOSEXECGOOD | MOS值为excellent和good之间的边界值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MOS值为excellent和good之间的边界值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～49，粒度为100。<br>默认值：无<br>配置原则：无 |
| MOSGOODACCP | MOS值为good和accept之间的边界值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MOS值为good和accept之间的边界值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～48，粒度为100。<br>默认值：无<br>配置原则：无 |
| MOSACCPPOOR | MOS值为accept和poor之间的边界值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MOS值为accept和poor之间的边界值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～47，粒度为100。<br>默认值：无<br>配置原则：无 |
| MOSPOORBAD | MOS值为poor和bad之间的边界值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MOS值为poor和bad之间的边界值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～46，粒度为100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VONRMOSCLASS]] · MOS分类区间值（VONRMOSCLASS）

## 使用实例

设置MOS值为excellent和good之间的边界值为41：

```
SET VONRMOSCLASS: MOSEXECGOOD=41;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-VONRMOSCLASS.md`
