---
id: UDG@20.15.2@MMLCommand@ADD EXTENDCOMMUNITYFILTERNODE
type: MMLCommand
name: ADD EXTENDCOMMUNITYFILTERNODE（增加基础扩展团体属性过滤器节点）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: EXTENDCOMMUNITYFILTERNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 基础扩展团体属性过滤器节点
status: active
---

# ADD EXTENDCOMMUNITYFILTERNODE（增加基础扩展团体属性过滤器节点）

## 功能

该命令用于添加基础扩展团体属性过滤器节点。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 配置该命令前，必须已经通过ADD EXTENDCOMMUNITYFILTER配置了基本扩展团体过滤器的名字。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 扩展团体属性过滤器名字或号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扩展团体属性过滤器名字或扩展团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，团体属性过滤器名称其长度范围是1～51。<br>默认值：无<br>配置原则：扩展团体属性过滤器号为整数形式，其中基本扩展团体属性过滤器号的取值范围为1～199。扩展团体属性过滤器名称为字符串形式，区分大小写，不支持空格，长度范围是1～51，且不能都是数字。 |
| MATCHMODE | 匹配模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定匹配模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无 |
| NODESEQUENCE | 扩展团体属性过滤器节点ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定扩展团体属性过滤器节点ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| STRINGVALUE1 | 字符串1 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE2 | 字符串2 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE3 | 字符串3 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE4 | 字符串4 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE5 | 字符串5 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE6 | 字符串6 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE7 | 字符串7 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE8 | 字符串8 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE9 | 字符串9 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE10 | 字符串10 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE11 | 字符串11 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE12 | 字符串12 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE13 | 字符串13 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE14 | 字符串14 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE15 | 字符串15 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |
| STRINGVALUE16 | 字符串16 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性值。支持三种格式： 格式一：as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~4294967295。 格式二：IPv4-address : nn，其中IPv4-address为IPv4地址格式，nn取值范围为0~65535。 格式三：as-number.as-number : nn，其中as-number，取值范围为0~65535，nn取值范围为0~65535。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是3～51。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535> or AS<0-65535>:NN<0-4294967295> or AS<65536-4294967295>:NN<0-65535>。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EXTENDCOMMUNITYFILTERNODE]] · 基础扩展团体属性过滤器节点（EXTENDCOMMUNITYFILTERNODE）

## 使用实例

增加基本扩展团体属性过滤器节点：

```
ADD EXTENDCOMMUNITYFILTERNODE:NODESEQUENCE=10,NAME="a",MATCHMODE=permit,STRINGVALUE1="1:1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-EXTENDCOMMUNITYFILTERNODE.md`
