---
id: UDG@20.15.2@MMLCommand@RMV DEBUGRECORD
type: MMLCommand
name: RMV DEBUGRECORD（清除异常信息记录）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: DEBUGRECORD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 异常信息
status: active
---

# RMV DEBUGRECORD（清除异常信息记录）

## 功能

该命令用于清除异常信息记录。

## 注意事项

- 该命令执行后立即生效。
- 本操作会删除异常记录信息。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：<br>- 当不输入时显示所有的资源单元或资源的信息。<br>- 当本命令在VNFP上使用时，需要先使用[**DSP RES**](../../../../单体服务平台功能管理/系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)查到“资源名称”，然后将“资源名称”的取值配置到本参数。<br>- 当本命令在VNFC上使用时，需要先使用[**DSP RU**](../../../系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)查到“RU名称”，然后将“RU名称”的取值配置到本参数。 |
| RECORDTYPE | 记录类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示异常类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- EXCEPTION：异常。<br>- ASSERT：断言。<br>- DEADLOOP：死循环。<br>- REPORTFAILURE：组件上报故障。<br>- STARVATION：消息调度不及时。<br>- MEMERROR：内存错误。<br>- PROCESSRESET：进程复位信息。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DEBUGRECORD]] · 异常信息记录（DEBUGRECORD）

## 使用实例

清除异常类信息：

```
RMV DEBUGRECORD:RECORDTYPE=EXCEPTION
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-DEBUGRECORD.md`
