---
id: UDG@20.15.2@MMLCommand@ADD EXTENDPROP
type: MMLCommand
name: ADD EXTENDPROP（增加扩展属性配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: EXTENDPROP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- 扩展属性
status: active
---

# ADD EXTENDPROP（增加扩展属性配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来配置扩展属性。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 除了EXTENDPROPNAME之外必须输入任何一个其他参数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXTENDPROPNAME | 扩展属性名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置扩展属性名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| EXTEND1 | 扩展属性1 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展属性1。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：无 |
| EXTEND2 | 扩展属性2 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展属性2。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：无 |
| EXTEND3 | 扩展属性3 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展属性3。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：无 |
| EXTEND4 | 扩展属性4 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展属性4。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：无 |
| EXTEND5 | 扩展属性5 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展属性5。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EXTENDPROP]] · 扩展属性配置（EXTENDPROP）

## 使用实例

增加配置扩展属性：EXTENDPROPNAME为textcategoryprop，Extend1为1000，EXTEND2为1002，EXTEND3为5，EXTEND4为467468，EXTEND5为3786：

```
ADD EXTENDPROP:EXTENDPROPNAME="textcategoryprop",EXTEND1=1000,EXTEND2=1002,EXTEND3=5,EXTEND4=467468,EXTEND5=3786;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加扩展属性配置（ADD-EXTENDPROP）_82837595.md`
