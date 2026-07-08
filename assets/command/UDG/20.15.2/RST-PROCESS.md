---
id: UDG@20.15.2@MMLCommand@RST PROCESS
type: MMLCommand
name: RST PROCESS（复位进程）
nf: UDG
version: 20.15.2
verb: RST
object_keyword: PROCESS
command_category: 动作类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务维护功能管理
- 操作维护
- 系统调测
- 进程管理
status: active
---

# RST PROCESS（复位进程）

## 功能

![](复位进程(RST PROCESS)_29626893.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，复位进程可能会导致RU复位引起业务中断，请确认是否继续执行。

该命令用于按照进程ID来复位系统中的进程。

## 注意事项

- 复位UNIPLT_MPU_SMU、UNIPLT_LPU_SMU会导致RU复位，请谨慎使用。
- 复位有主备模式的主进程，会导致备升主。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程ID | 可选必选说明：必选参数<br>参数含义：该参数表示指定复位进程的ID。通过<br>**DSP PROCESSXXX**<br>（XXX表示CSLB等服务，例如CSLB的命令为DSP PROCESSCSLB，CSDB的命令为DSP PROCESSCSDB）命令可以查询进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1000～65535。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。该参数不能取值为VNFP、ACS、VNRS_VNFC的服务实例名称。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PROCESS]] · 复位进程（PROCESS）

## 使用实例

复位进程ID号为1002的进程：

```
RST PROCESS:PROCID=1002
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RST-PROCESS.md`
