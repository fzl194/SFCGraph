---
id: UNC@20.15.2@MMLCommand@RMV NRFINSTRT
type: MMLCommand
name: RMV NRFINSTRT（删除NF实例路由）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV NRFINSTRT（删除NF实例路由）

## 功能

**适用NF：NRF**

该命令用于删除目标NF的实例标识路由信息。

## 注意事项

- 立即生效

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

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFINSTRT]] · NF实例路由（NRFINSTRT）

## 使用实例

- 运营商网络为双层网络，高层PLMN-NRF，底层L-NRF。L-NRF1归属于PLMN-NRF。 在PLMN-NRF上执行如下命令，删除条件匹配起始位置为0，条件匹配长度为0，NF实例标识匹配值为123e4567-e89b-12d3-a456-426655440000的路由信息。
  ```
  RMV NRFINSTRT: START=0, LENGTH=0, NFINSTIDMATCHINGVALUE="123e4567-e89b-12d3-a456-426655440000";
  ```
- 在PLMN-NRF上执行如下命令，删除条件匹配起始位置为0，条件匹配长度为8，NF实例标识匹配值为123e4567的路由信息。
  ```
  RMV NRFINSTRT: START=0, LENGTH=8, NFINSTIDMATCHINGVALUE="123e4567";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF实例路由（RMV-NRFINSTRT）_09651410.md`
