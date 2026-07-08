---
id: UDG@20.15.2@MMLCommand@DSP TRCDBGINFO
type: MMLCommand
name: DSP TRCDBGINFO（查询跟踪调试信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TRCDBGINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务维护功能管理
- 操作维护
- 系统调测
- 跟踪调试信息
status: active
---

# DSP TRCDBGINFO（查询跟踪调试信息）

## 功能

该命令用于显示VNFC跟踪任务的调试信息，此信息只用于跟踪问题定位，不涉及用户私有信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程ID | 可选必选说明：可选参数<br>参数含义：该参数表示指定查询进程的ID。通过<br>**DSP PROCESSXXX**<br>（XXX表示CSLB等服务，例如CSLB的命令为DSP PROCESSCSLB，CSDB的命令为DSP PROCESSCSDB）命令可以查询进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1000～65535。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。该参数不能取值为VNFP、ACS、VNRS_VNFC的服务实例名称。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TRCDBGINFO]] · 跟踪调试信息（TRCDBGINFO）

## 使用实例

查询1003号进程上的跟踪任务的调试信息：

```
DSP TRCDBGINFO:PROCID=1003
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功。

结果如下
--------
              进程ID  =  1003
            跟踪类型  =  4103
            跟踪句柄  =  1051648
      接收的消息总数  =  1
定位比较失败的消息数  =  0
过滤比较失败的消息数  =  0
    上报成功的消息数  =  1
    上报失败的消息数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-TRCDBGINFO.md`
