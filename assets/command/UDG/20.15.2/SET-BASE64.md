---
id: UDG@20.15.2@MMLCommand@SET BASE64
type: MMLCommand
name: SET BASE64（设置Base64编码规则）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: BASE64
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- BASE64编码
status: active
---

# SET BASE64（设置Base64编码规则）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置Base64编码规则。当重定向进行加密操作后，设置是否要对加密结果进行base64编码，当重定向进行编码后，是否要对特殊字符进行转换。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | REDENABLEFLG | REDEQNULLFLG | RPTENABLEFLG | RPTEQNULLFLG | HEADENENABLEFLG | HEADENEQNULLFLG |
| --- | --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | NORPLC | DISABLE | NORPLC | DISABLE | NORPLC |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REDENABLEFLG | 重定向Base64编码标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置重定向Base64编码标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能Base64编码。<br>- ENABLE：使能Base64编码。<br>默认值：无<br>配置原则：<br>- 如果运营商想要对重定向加密结果进行base64编码，则使能该标识，即配置为ENABLE。<br>- 如果运营商不想对重定向加密结果进行base64编码，则不使能该标识，即配置为DISABLE。 |
| REDEQNULLFLG | 重定向等号替换标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“REDENABLEFLG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置重定向等号替换标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NORPLC：不对等号进行替换处理。<br>- NULL：删除等号。<br>- RPLC：使用指定字符替换等号。<br>默认值：无<br>配置原则：<br>- 如果不想对base64编码之后的等号进行处理，设置为NORPLC。<br>- 如果想删除base64编码之后的等号，设置为NULL。<br>- 如果想要替换base64编码之后的等号，设置为RPLC。 |
| REDEQRPLCHR | 重定向等号替换字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“REDEQNULLFLG”配置为“RPLC”时为必选参数。<br>参数含义：该参数用于设置重定向等号替换字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。<br>默认值：无<br>配置原则：无 |
| REDSLRPLCHR | 重定向斜杠替换字符串 | 可选必选说明：条件可选参数<br>前提条件：该参数在“REDENABLEFLG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置重定向斜杠替换字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| REDPLRPLCHR | 重定向加号替换字符串 | 可选必选说明：条件可选参数<br>前提条件：该参数在“REDENABLEFLG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置重定向加号替换字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| RPTENABLEFLG | 业务报表Base64编码标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置业务报表Base64编码标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能Base64编码。<br>- ENABLE：使能Base64编码。<br>默认值：无<br>配置原则：<br>- 如果运营商想要对业务报表加密结果进行base64编码，则使能该标识，即配置为ENABLE。<br>- 如果运营商不想对业务报表加密结果进行base64编码，则不使能该标识，即配置为DISABLE。 |
| RPTEQRPLCHR | 业务报表等号替换字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RPTEQNULLFLG”配置为“RPLC”时为必选参数。<br>参数含义：该参数用于设置业务报表等号替换字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。<br>默认值：无<br>配置原则：无 |
| RPTEQNULLFLG | 业务报表等号替换标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“RPTENABLEFLG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置业务报表等号替换标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NORPLC：不对等号进行替换处理。<br>- NULL：删除等号。<br>- RPLC：使用指定字符替换等号。<br>默认值：无<br>配置原则：<br>- 如果不想对base64编码之后的等号进行处理，设置为NORPLC。<br>- 如果想删除base64编码之后的等号，设置为NULL。<br>- 如果想要替换base64编码之后的等号，设置为RPLC。 |
| RPTSLRPLCHR | 业务报表斜杠替换字符串 | 可选必选说明：条件可选参数<br>前提条件：该参数在“RPTENABLEFLG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置业务报表斜杠替换字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| RPTPLRPLCHR | 业务报表加号替换字符串 | 可选必选说明：条件可选参数<br>前提条件：该参数在“RPTENABLEFLG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置业务报表加号替换字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| HEADENENABLEFLG | 头增强Base64编码标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置头增强Base64编码标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能Base64编码。<br>- ENABLE：使能Base64编码。<br>默认值：无<br>配置原则：<br>- 如果运营商想要对头增强加密结果进行base64编码，则使能该标识，即配置为ENABLE。<br>- 如果运营商不想对头增强加密结果进行base64编码，则不使能该标识，即配置为DISABLE。 |
| HEADENEQNULLFLG | 头增强等号替换标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“HEADENENABLEFLG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置头增强等号替换标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NORPLC：不对等号进行替换处理。<br>- NULL：删除等号。<br>- RPLC：使用指定字符替换等号。<br>默认值：无<br>配置原则：<br>- 如果不想对base64编码之后的等号进行处理，设置为NORPLC。<br>- 如果想删除base64编码之后的等号，设置为NULL。<br>- 如果想要替换base64编码之后的等号，设置为RPLC。 |
| HEADENEQRPLCHR | 头增强等号替换字符串 | 可选必选说明：条件必选参数<br>前提条件：该参数在“HEADENEQNULLFLG”配置为“RPLC”时为必选参数。<br>参数含义：该参数用于设置头增强等号替换字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| HEADENSLRPLCHR | 头增强斜杠替换字符串 | 可选必选说明：条件可选参数<br>前提条件：该参数在“HEADENENABLEFLG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置头增强斜杠替换字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| HEADENPLRPLCHR | 头增强加号替换字符串 | 可选必选说明：条件可选参数<br>前提条件：该参数在“HEADENENABLEFLG”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置头增强加号替换字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@BASE64]] · Base64编码规则（BASE64）

## 使用实例

假如运营商想要对重定向的加密结果进行base64编码，并将等号替换为oeq，则配置如下：

```
SET BASE64:REDENABLEFLG=ENABLE,REDEQNULLFLG=RPLC,REDEQRPLCHR="oeq";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-BASE64.md`
