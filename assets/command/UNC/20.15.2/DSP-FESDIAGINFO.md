---
id: UNC@20.15.2@MMLCommand@DSP FESDIAGINFO
type: MMLCommand
name: DSP FESDIAGINFO（显示FES诊断信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: FESDIAGINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎服务
- 显示FES诊断信息
status: active
---

# DSP FESDIAGINFO（显示FES诊断信息）

## 功能

该命令用于显示FES诊断信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | FES命令类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示FES命令类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BLACK-BOX：黑匣子。<br>- STATISTICS：统计计数。<br>- MESSAGE-STATISTICS：消息统计计数。<br>- LOCAL-DATA：本地数据。<br>- OPERATION-STATISTICS：操作统计计数。<br>- ATTRIBUTE：详细属性。<br>- FLOW-CONTROL：流控。<br>- MC-GROUP-STATE：多播组状态。<br>- DATA-SYNCHRONIZE-STATE：数据同步状态。<br>默认值：无 |
| IDENTITYFLAG | 身份标志位 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“ATTRIBUTE”、“OPERATION-STATISTICS”、“MESSAGE-STATISTICS”、“STATISTICS”、“LOCAL-DATA”、“BLACK-BOX”、“FLOW-CONTROL”、“MC-GROUP-STATE” 或 “DATA-SYNCHRONIZE-STATE”时为可选参数。<br>参数含义：该参数用于表示身份标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RUNAME：表示输入资源单元名称。<br>- COMPID：表示输入组件ID。<br>默认值：无 |
| ATTRFLAG | 属性标志位 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“ATTRIBUTE”时为必选参数。<br>参数含义：该参数用于表示操作标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TABLE：表数据。<br>- PATH：路径数据。<br>- RELATION：关系数据。<br>默认值：无 |
| OPERFLAG | 详细信息标志位 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“ATTRIBUTE”时为可选参数。<br>参数含义：该参数用于表示操作标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BERIF：简要信息。<br>- VERBOSE：详细信息。<br>默认值：BERIF |
| FLAGALL | 命令操作标记 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“OPERATION-STATISTICS”时为可选参数。<br>参数含义：该参数用于表示命令操作标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL：所有类型。<br>- TABLE：Table类型。<br>- PATH：Path类型。<br>- RELATION：Relation类型。<br>默认值：ALL |
| MID | 模块ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“LOCAL-DATA”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“STATISTICS”时为可选参数。<br>参数含义：该参数用于表示模块ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| PARTNERID | 对端组件PID | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“MESSAGE-STATISTICS”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“MC-GROUP-STATE” 或 “DATA-SYNCHRONIZE-STATE”时为可选参数。<br>参数含义：该参数用于表示对端组件PID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| BLKBOXID | 黑匣子ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“BLACK-BOX”时为可选参数。<br>参数含义：该参数用于表示黑匣子ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| COMPONENTID | 组件ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“IDENTITYFLAG”配置为“COMPID”时为必选参数。<br>参数含义：该参数用于表示组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| RUNAME | 资源单元名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IDENTITYFLAG”配置为“RUNAME”时为必选参数。<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：区分大小写，不支持空格，下发本MML命令前可使用DSP RU查看资源单元信息。 |
| RELATIONID | 关系ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“ATTRFLAG”配置为“RELATION”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“FLAGALL”配置为“RELATION”时为可选参数。<br>参数含义：该参数用于表示关系ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| TABLEID | 表ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“ATTRFLAG”配置为“TABLE”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“FLAGALL”配置为“TABLE”时为可选参数。<br>参数含义：该参数用于表示表ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| PATHID | 路径ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“ATTRFLAG”配置为“PATH”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“FLAGALL”配置为“PATH”时为可选参数。<br>参数含义：该参数用于表示路径ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FESDIAGINFO]] · FES诊断信息（FESDIAGINFO）

## 使用实例

显示FES诊断信息：

```
DSP FESDIAGINFO:TYPE=LOCAL-DATA,MID=1;
```

```

RETCODE = 0  Operation Success.

结果如下
------------------------
查询返回结果  =
MSG_Diagnose:
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-FESDIAGINFO.md`
