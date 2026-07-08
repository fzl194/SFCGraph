---
id: UDG@20.15.2@MMLCommand@OPR PLTMAINTAIN
type: MMLCommand
name: OPR PLTMAINTAIN（执行uniplt调试命令）
nf: UDG
version: 20.15.2
verb: OPR
object_keyword: PLTMAINTAIN
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务维护功能管理
- 操作维护
- 系统调测
- MBP调测信息
status: active
---

# OPR PLTMAINTAIN（执行uniplt调试命令）

## 功能

该命令用于在APP指定进程上执行调试命令。完整的调试命令在“CMDMSG（命令信息）”参数中下发，调试命令的详细帮助可通过如下步骤获取：

执行本命令，在“CMDMSG（命令信息）”中输入“$”获取可执行的所有调试命令。

## 注意事项

该命令用于收集定位信息，需要谨慎执行，请在华为工程师指导下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程ID | 可选必选说明：必选参数。<br>参数含义：该参数表示指定的进程ID号。通过<br>**DSP PROCESSXXX**<br>（XXX表示CSLB等服务，例如CSLB的命令为DSP PROCESSCSLB，CSDB的命令为DSP PROCESSCSDB）命令可以查询进程ID。<br>数据来源：本端规划。<br>取值范围：整型，1000～65535。<br>默认值：无。 |
| CMDMSG | 命令信息 | 可选必选说明：必选参数。<br>参数含义：该参数表示调试命令字符串。<br>数据来源：本端规划。<br>取值范围：字符串类型，长度范围1～255。“$”用于输出帮助信息。<br>默认值：无。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。该参数不能取值为VNFP、ACS、VNRS_VNFC的服务实例名称。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PLTMAINTAIN]] · uniplt调试命令（PLTMAINTAIN）

## 使用实例

输入prr_memleak config命令，显示1002进程内存泄露监控模块相关配置信息。

```
OPR PLTMAINTAIN: PROCID=1002, CMDMSG="prr_memleak config"
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功。

结果如下
--------
      进程ID  =  1002
    命令信息  =  prr_memleak config
结果报文信息  =  
   Memory Check Switch = 1
     Memory Check Time = 60000
  Memory Over Duration = 30000
   Memory Check Number = 200
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/执行uniplt调试命令（OPR-PLTMAINTAIN）_29626901.md`
