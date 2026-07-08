---
id: UNC@20.15.2@MMLCommand@OPR FESSEARCHTABLE
type: MMLCommand
name: OPR FESSEARCHTABLE（模拟触发FES表项搜索）
nf: UNC
version: 20.15.2
verb: OPR
object_keyword: FESSEARCHTABLE
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎服务
- 模拟搜索FES表项
status: active
---

# OPR FESSEARCHTABLE（模拟触发FES表项搜索）

## 功能

该命令用于模拟FES表项搜索。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TABLEID | 表ID | 可选必选说明：必选参数<br>参数含义：该参数用来表示表ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| IDENTITYFLAG | 身份标志位 | 可选必选说明：可选参数<br>参数含义：该参数用于表示身份标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RUNAME：表示输入资源单元名称。<br>- COMPID：表示输入组件ID。<br>默认值：无<br>配置原则：如果不输入该参数，则表示模拟搜索FES表项的全部记录信息。 |
| RECNUM | 记录数量 | 可选必选说明：可选参数<br>参数含义：该参数用来表示记录数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～50。<br>默认值：无<br>配置原则：如果不输入该参数，则表示输出所有条目。 |
| OPERFLAG | 下发标记位 | 可选必选说明：可选参数<br>参数含义：该参数用来表示下发标记位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DOWNLOAD：搜索并下发。<br>- NODOWNLOAD：搜索不下发。<br>默认值：NODOWNLOAD |
| FILTERFLAG | 过滤字段标志位 | 可选必选说明：可选参数<br>参数含义：该参数用来表示过滤字段的标志位。用来指定1-5组过滤条件字段名称和过滤条件字段取值。Parameter为过滤条件字段名称。Parameter Value为过滤条件字段取值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NOFILTER：不过滤。<br>- ONE：过滤一组字段。<br>- TWO：过滤二组字段。<br>- THREE：过滤三组字段。<br>- FOUR：过滤四组字段。<br>- FIVE：过滤五组字段。<br>默认值：NOFILTER |
| FIELD | 第一个字段名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERFLAG”配置为“ONE”、“TWO”、“THREE”、“FOUR” 或 “FIVE”时为必选参数。<br>参数含义：该参数用来表示第一个字段名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无 |
| FIELD2 | 第二个字段名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERFLAG”配置为“TWO”、“THREE”、“FOUR” 或 “FIVE”时为必选参数。<br>参数含义：该参数用来表示第二个字段名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无 |
| FIELD3 | 第三个字段名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERFLAG”配置为“THREE”、“FOUR” 或 “FIVE”时为必选参数。<br>参数含义：该参数用来表示第三个字段名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无 |
| FIELD4 | 第四个字段名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERFLAG”配置为“FOUR” 或 “FIVE”时为必选参数。<br>参数含义：该参数用来表示第四个字段名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无 |
| FIELD5 | 第五个字段名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERFLAG”配置为“FIVE”时为必选参数。<br>参数含义：该参数用来表示第五个字段名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无 |
| VALUE | 第一个参数值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERFLAG”配置为“ONE”、“TWO”、“THREE”、“FOUR” 或 “FIVE”时为必选参数。<br>参数含义：该参数用来表示第一个参数值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| VALUE2 | 第二个参数值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERFLAG”配置为“TWO”、“THREE”、“FOUR” 或 “FIVE”时为必选参数。<br>参数含义：该参数用来表示第二个参数值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| VALUE3 | 第三个参数值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERFLAG”配置为“THREE”、“FOUR” 或 “FIVE”时为必选参数。<br>参数含义：该参数用来表示第三个参数值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| VALUE4 | 第四个参数值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERFLAG”配置为“FOUR” 或 “FIVE”时为必选参数。<br>参数含义：该参数用来表示第四个参数值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| VALUE5 | 第五个参数值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILTERFLAG”配置为“FIVE”时为必选参数。<br>参数含义：该参数用来表示第五个参数值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| COMPONENTID | 组件ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“IDENTITYFLAG”配置为“COMPID”时为必选参数。<br>参数含义：该参数用来表示组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| RUNAME | 资源单元名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IDENTITYFLAG”配置为“RUNAME”时为必选参数。<br>参数含义：该参数用来表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：区分大小写，不支持空格，下发本MML命令前可使用DSP RU查看资源单元信息。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@FESSEARCHTABLE]] · 模拟触发FES表项搜索（FESSEARCHTABLE）

## 使用实例

模拟FES表项搜索：

```
OPR FESSEARCHTABLE:TABLEID=1082;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/OPR-FESSEARCHTABLE.md`
