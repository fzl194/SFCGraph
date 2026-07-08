---
id: UNC@20.15.2@MMLCommand@OPR DBGCMDPRXY
type: MMLCommand
name: OPR DBGCMDPRXY（通过命令代理执行调试命令）
nf: UNC
version: 20.15.2
verb: OPR
object_keyword: DBGCMDPRXY
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 系统维护
- 调试命令
status: active
---

# OPR DBGCMDPRXY（通过命令代理执行调试命令）

## 功能

该命令用于在APP VNFC上执行调试命令。完整的调试命令在“CMDMSG（调试命令字符串）”参数中下发，调试命令的详细帮助可通过如下步骤获取：

1、执行本命令，在“CMDMSG（调试命令字符串）”中输入“$”获取可执行的所有调试命令。

2、执行本命令，在“CMDMSG（调试命令字符串）”中输入要执行的调试命令、空格和“$”，显示调试命令的第一关键字。

3、执行本命令，在“CMDMSG（调试命令字符串）”中输入要执行的调试命令、第一关键字、空格和“$”，显示调试命令的第二关键字。

4、依次类推，直到显示调试命令的所有关键字。

## 注意事项

- 该命令仅用于常规维护手段无法解决问题时的特殊场景，如使用不当，会导致设备异常或者业务中断，所有操作必须在华为公司研发人员的明确确认和指导下才能操作。如果没有在华为公司研发人员的确认和指导下私自操作导致产生网络故障，华为公司不承担相应责任。
- 该命令不支持输入“？”，将其取代为“$”。
- 该命令用于收集定位信息，需要谨慎执行，请在华为公司研发人员指导下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数。<br>参数含义：指定RU的名称。可通过<br>**[DSP RU](../../../../单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)**<br>命令查询获取，对应“RU名称”表项。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围1～63。<br>默认值：无。 |
| SGID | SG进程ID号 | 可选必选说明：必选参数。<br>参数含义：指定RU上的进程ID号。可通过<br>**DSP PROCESSXXX**<br>（XXX表示CSLB等服务，例如CSLB的命令为<br>**[DSP PROCESSCSLB](../../../../CSLB功能管理/进程管理/查询CSLB进程信息(DSP PROCESSCSLB)_85585647.md)**<br>，CSDB的命令为<br>**[DSP PROCESSCSDB](../../../../CSDB功能管理/进程管理/查询CSDB进程信息(DSP PROCESSCSDB)_85002950.md)**<br>）命令查询获取，对应“进程在Ru上的实例ID”表项。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无。 |
| CMDMSG | 调试命令字符串 | 可选必选说明：必选参数。<br>参数含义：调试命令字符串，沿用console的所有命令。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围1～255。该字符串支持空格和“$”，“$”用于代替console命令中的“?”，以输出帮助信息。<br>默认值：无。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识，不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的RU状态查询。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DBGCMDPRXY]] · 通过命令代理执行调试命令（DBGCMDPRXY）

## 使用实例

查询RU名称为CSLB_OM_RU_0001的SMU进程上的当前全局时间信息：

```
OPR DBGCMDPRXY: RUNAME="CSLB_OM_RU_0001",SGID=0,CMDMSG="tick show now"
,SERVICEINSTANCE="CSLB_VNFC_999"
;
```

```
RETCODE = 0  操作成功.

结果如下
-------------------------
                       RU名称  =  CSLB_OM_RU_0001
                   SG进程ID号  =  0
               调试命令字符串  =  tick show now
     调试命令执行结果返回信息  =  
	TICK show:
	               Date = 2016-03-28_1.
	               Time = 18:01:36:961.
	    MillSecFrom1970 = 1459188096961(ms).
	               Tick = 19833809(ms).
	                    
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/OPR-DBGCMDPRXY.md`
