---
id: UDG@20.15.2@MMLCommand@RMV UPFPERFRANGE
type: MMLCommand
name: RMV UPFPERFRANGE（删除UPF上报性能指标范围配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UPFPERFRANGE
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 业务性能统计上报范围配置
status: active
---

# RMV UPFPERFRANGE（删除UPF上报性能指标范围配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来删除UPF上报性能指标范围配置。

## 注意事项

该命令执行后需要重新下发测量对象才能生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数<br>参数含义：该参数用于指示网元ID，可以通过LST ME获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |
| MOC | 测量对象类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定测量对象类型，可以通过DSP MEASMOC命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由大小写字母组成，当前版本只支持APN。<br>默认值：无<br>配置原则：无 |
| MOIRANGE | 测量对象实例范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定测量对象实例的范围。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL：表示所有测量单元或者测量对象实例。<br>- SPECIFIC：表示指定测量单元或测量对象实例。<br>默认值：无<br>配置原则：无 |
| MOIID | 测量对象实例 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MOIRANGE”配置为“SPECIFIC”时为必选参数。<br>参数含义：该参数用于指定测量对象实例，可以通过LST APN:;查询当前有效的APN对象实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPFPERFRANGE]] · UPF上报性能指标范围配置（UPFPERFRANGE）

## 使用实例

大量APN对象进行性能指标上报，需要删除指定APN上报的性能统计指标范围，执行：

```
RMV UPFPERFRANGE: MEID=0, MOC="APN", MOIRANGE=SPECIFIC, MOIID="huawei.com";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除UPF上报性能指标范围配置（RMV-UPFPERFRANGE）_01838836.md`
