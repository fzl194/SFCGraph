---
id: UDG@20.15.2@MMLCommand@ADD ERRORCODE
type: MMLCommand
name: ADD ERRORCODE（增加错误码）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ERRORCODE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- 重定向公共参数管理
- ErrorCode
status: active
---

# ADD ERRORCODE（增加错误码）

## 功能

**适用NF：PGW-U、UPF**

此命令用于配置错误码信息。运营商可以根据报文中错误码进行不同的重定向动作处理。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 单个ErrorCodeName下最多配置500组错误码范围。
- 整机最多可以配置2000组错误码范围。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ERRORCODENAME | 错误码名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置错误码配置名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |
| ERRORCODEOP | 错误码范围操作码 | 可选必选说明：必选参数<br>参数含义：该参数用于配置错误码范围操作码。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- EQUAL：等于指定值。<br>- LT：小于等于指定值。<br>- GT：大于等于指定值。<br>- RANGE：在指定范围内，包括边界值。<br>默认值：无<br>配置原则：<br>- 当运营商需要配置错误码等于指定值时，该参数需配置为EQUAL。<br>- 当运营商需要配置错误码小于等于指定值时，该参数需配置为LT。<br>- 当运营商需要配置错误码大于等于指定值时，该参数需配置为GT。<br>- 当运营商需要配置错误码在指定范围（包括边界值）时，该参数需配置为RANGE。 |
| ERRORCODESTART | 错误码范围起始值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ERRORCODEOP”配置为“EQUAL”、“GT” 或 “RANGE”时为必选参数。<br>参数含义：该参数用于配置错误码范围起始值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1000。<br>默认值：无<br>配置原则：无 |
| ERRORCODEEND | 错误码范围终止值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ERRORCODEOP”配置为“LT” 或 “RANGE”时为必选参数。<br>参数含义：该参数用于配置错误码范围终止值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ERRORCODE]] · 错误码（ERRORCODE）

## 关联任务

- [[UDG@20.15.2@Task@0-00089]]

## 使用实例

运营商规划定义一个名为“testerrorcode”的错误码：

```
ADD ERRORCODE: ERRORCODENAME="testerrorcode", ERRORCODEOP=LT, ERRORCODEEND=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加错误码（ADD-ERRORCODE）_09678504.md`
