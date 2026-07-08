---
id: UNC@20.15.2@MMLCommand@MOD NRFINSTRT
type: MMLCommand
name: MOD NRFINSTRT（修改NF实例路由）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NRFINSTRT
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- NF实例路由管理
status: active
---

# MOD NRFINSTRT（修改NF实例路由）

## 功能

**适用NF：NRF**

该命令用于修改指定NF实例标识路由所归属的NRF实例组名称。

## 注意事项

- 该命令执行后立即生效。

- 当参数LENGTH等于0且参数START等于0时，参数NFINSTIDMATCHINGVALUE表示一个完整NF实例标识。
- 其他情况下，参数START加上参数LENGTH的值需要小于等于40，且参数LENGTH的值需要等于参数NFINSTIDMATCHINGVALUE的实际长度。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| START | 条件匹配起始位置 | 可选必选说明：必选参数<br>参数含义：该参数表示条件匹配的NF实例标识起始位置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~39。<br>默认值：无<br>配置原则：无 |
| LENGTH | 条件匹配长度 | 可选必选说明：必选参数<br>参数含义：该参数表示NF实例标识匹配值的长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~40。<br>默认值：无<br>配置原则：无 |
| NFINSTIDMATCHINGVALUE | NF实例标识匹配值 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF实例标识匹配值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：<br>“条件匹配长度”为非0时，此匹配值的字符串长度等于“条件匹配长度”的值。 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于NF实例路由寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## 操作的配置对象

- [NF实例路由（NRFINSTRT）](configobject/UNC/20.15.2/NRFINSTRT.md)

## 使用实例

运营商网络规划变更，当前NRF上寻址NF实例标识下一跳路由发生变化。条件匹配起始位置为3，条件匹配长度为5，NF实例标识匹配值为e4567的NF所归属NRF实例组名称由“L-NRF1”变为“L-NRF3”，需要在当前NRF上执行：

```
MOD NRFINSTRT: START=3, LENGTH=5, NFINSTIDMATCHINGVALUE="e4567", NEXTNRFGRPNAME="L-NRF3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NF实例路由（MOD-NRFINSTRT）_09653796.md`
