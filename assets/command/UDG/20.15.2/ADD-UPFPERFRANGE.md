---
id: UDG@20.15.2@MMLCommand@ADD UPFPERFRANGE
type: MMLCommand
name: ADD UPFPERFRANGE（添加UPF上报性能指标范围配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPFPERFRANGE
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 31
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 业务性能统计上报范围配置
status: active
---

# ADD UPFPERFRANGE（添加UPF上报性能指标范围配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来添加UPF上报性能指标范围配置。

## 注意事项

- 该命令执行后需要重新下发测量对象才能生效。
- 该命令最大记录数为31。
- 整系统最多可以指定30个测量对象实例的性能指标上报范围。
- 该命令只支持配置APN对象的性能指标范围。
- APN实例不存在时不允许添加指定APN实例的性能指标范围。执行该命令将失败。
- 配置该命令后，网元向网管上报的性能指标结果可能少于网管下发的测量任务中包含的指标，未上报结果的指标在网管上查询到的结果为空，未上报结果的测量单元在网管上查询不到。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数<br>参数含义：该参数用于指示网元ID，可以通过LST ME获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |
| MOC | 测量对象类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定测量对象类型，可以通过DSP MEASMOC命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由大小写字母组成，当前版本只支持APN。<br>默认值：无<br>配置原则：无 |
| MOIRANGE | 测量对象实例范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定测量对象实例的范围。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL：表示所有测量对象实例。<br>- SPECIFIC：表示指定测量对象实例。<br>默认值：无<br>配置原则：“指定测量对象实例”的优先级高于“所有测量对象实例”。 |
| MOIID | 测量对象实例 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MOIRANGE”配置为“SPECIFIC”时为必选参数。<br>参数含义：该参数用于指定测量对象实例，可以通过LST APN:;查询当前有效的APN对象实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：当“测量对象类型”设置为APN时，本参数设置的APN需要是ADD APN命令配置的APN。 |
| RPTRANGE | 上报范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定测量对象类型支持上报的指标范围。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL：表示上报所有指标。<br>- NORTH：表示仅上报北向指标。<br>- BASIC：表示上报基础指标，包含北向指标。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPFPERFRANGE]] · UPF上报性能指标范围配置（UPFPERFRANGE）

## 使用实例

- 大量APN对象进行性能指标上报时，配置整机上报的性能统计指标范围时，执行：
  ```
  ADD UPFPERFRANGE: MEID=0, MOC="APN", MOIRANGE=ALL, RPTRANGE=NORTH;
  ```
- 大量APN对象进行性能指标上报时，需要配置指定APN上报的性能统计指标范围时，执行：
  ```
  ADD UPFPERFRANGE: MEID=0, MOC="APN", MOIRANGE=SPECIFIC, MOIID="huawei.com", RPTRANGE=ALL;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-UPFPERFRANGE.md`
