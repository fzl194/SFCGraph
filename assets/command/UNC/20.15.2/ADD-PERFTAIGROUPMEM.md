---
id: UNC@20.15.2@MMLCommand@ADD PERFTAIGROUPMEM
type: MMLCommand
name: ADD PERFTAIGROUPMEM（增加TAI组性能统计对象成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PERFTAIGROUPMEM
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# ADD PERFTAIGROUPMEM（增加TAI组性能统计对象成员）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于为基于TAI组的性能统计对象增加TAI成员。

## 注意事项

- 该命令执行后立即生效。

- 一个TAI组性能统计对象中可添加多个TAI，这些TAI可通过一条或多条ADD PERFTAIGROUPMEM进行配置，且这些TAI的PLMN和TAIGROUPTYPE必须一致。
- 本命令中的TAIGROUPNAME参数引用自ADD PERFTAIGROUP，在执行本命令之前，请首先通过ADD PERFTAIGROUP配置TAIGROUPNAME。
- 输入的起始TAI值必须小于或者等于终止TAI值。
- 输入的起始TAI值和终止TAI值定义的TAI号段范围不允许与其它记录定义的TAI号段范围相互交叉、包含或重合。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAIGROUPNAME | TAI组名 | 可选必选说明：必选参数<br>参数含义：该参数用于标识基于TAI组的性能统计对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写，不支持空格及“\”。 TAI组性能统计对象名称通过ADD PERFTAIGROUP命令创建。<br>默认值：无<br>配置原则：无 |
| TAIGROUPTYPE | TAI组类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAI组类型。<br>数据来源：本端规划<br>取值范围：<br>- S1Tac（S1TAC）<br>- N2Tac（N2TAC）<br>默认值：无<br>配置原则：无 |
| BEGINTAI | 起始TAI | 可选必选说明：必选参数<br>参数含义：该参数用于表示TAI组所包含的TAI起始值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是9~12。TAI由MCC、MNC和TAC组成。其中MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度；TAC编码为16进制数，S1类型TAC固定为4位，若不足则左起补0；N2类型TAC固定为6位，若不足则左起补0。<br>默认值：无<br>配置原则：无 |
| ENDTAI | 终止TAI | 可选必选说明：必选参数<br>参数含义：该参数用于表示TAI组所包含的TAI结束值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是9~12。TAI由MCC、MNC和TAC组成。其中MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度；TAC编码为16进制数，S1类型TAC固定为4位，若不足则左起补0；N2类型TAC固定为6位，若不足则左起补0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TAI组性能统计对象成员（PERFTAIGROUPMEM）](configobject/UNC/20.15.2/PERFTAIGROUPMEM.md)

## 使用实例

当需要在组名为"huawei"的TAI组对象中添加TAI类型为S1Tac、起始TAI为"100000000"、终止TAI为"10000FFFF"所对应的TAI区间，执行如下命令：

```
ADD PERFTAIGROUPMEM: TAIGROUPNAME="huawei", TAIGROUPTYPE=S1Tac, BEGINTAI="100000000", ENDTAI="10000FFFF";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加TAI组性能统计对象成员（ADD-PERFTAIGROUPMEM）_17625954.md`
