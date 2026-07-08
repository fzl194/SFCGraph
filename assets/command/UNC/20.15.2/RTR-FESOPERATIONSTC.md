---
id: UNC@20.15.2@MMLCommand@RTR FESOPERATIONSTC
type: MMLCommand
name: RTR FESOPERATIONSTC（清除FES操作统计信息）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: FESOPERATIONSTC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎服务
- 清除FES operation统计计数
status: active
---

# RTR FESOPERATIONSTC（清除FES操作统计信息）

## 功能

该命令用于清除FES TABLE，PATH，RELATION的操作统计信息，以便进行重新统计。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDENTITYFLAG | 身份标志位 | 可选必选说明：可选参数<br>参数含义：该参数用于表示身份标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RUNAME：表示输入资源单元名称。<br>- COMPID：表示输入组件ID。<br>默认值：无<br>配置原则：如果不输入该参数，则表示清除所有FES操作统计信息。 |
| FLAGALL | 清除类型 | 可选必选说明：可选参数<br>参数含义：该参数用来表示数据清除的操作类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL：所有类型。<br>- TABLE：Table类型。<br>- PATH：Path类型。<br>- RELATION：Relation类型。<br>默认值：ALL |
| COMPONENTID | 组件ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“IDENTITYFLAG”配置为“COMPID”时为必选参数。<br>参数含义：该参数用来表示组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| RUNAME | 资源单元名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IDENTITYFLAG”配置为“RUNAME”时为必选参数。<br>参数含义：该参数用来表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：区分大小写，不支持空格，下发本MML命令前可使用DSP RU查看资源单元信息。 |

## 操作的配置对象

- [FES操作统计信息（FESOPERATIONSTC）](configobject/UNC/20.15.2/FESOPERATIONSTC.md)

## 使用实例

重置FES操作统计信息：

```
RTR FESOPERATIONSTC:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除FES操作统计信息（RTR-FESOPERATIONSTC）_00866769.md`
