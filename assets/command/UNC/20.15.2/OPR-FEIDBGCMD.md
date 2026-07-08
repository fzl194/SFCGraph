---
id: UNC@20.15.2@MMLCommand@OPR FEIDBGCMD
type: MMLCommand
name: OPR FEIDBGCMD（执行FEI调试命令）
nf: UNC
version: 20.15.2
verb: OPR
object_keyword: FEIDBGCMD
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 调试命令
status: active
---

# OPR FEIDBGCMD（执行FEI调试命令）

## 功能

该命令用于在VNRS_VNFC上执行FEI调试命令。

## 注意事项

- 该命令用于收集定位信息，需要谨慎执行，请在华为工程师指导下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数。<br>参数含义：指定RU的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围1～63。<br>默认值：无。<br>配置原则：参考<br>**[DSP RU](../../../../../单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)**<br>命令查询RU编号。 |
| CMDMSG | 调试命令字符串 | 可选必选说明：必选参数。<br>参数含义：调试命令字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围1～255。<br>默认值：无。<br>配置原则：参考使用指南。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FEIDBGCMD]] · FEI调试命令（FEIDBGCMD）

## 使用实例

查询“VNRS_IP_RU_C24_0064”的不同部署模式下的启动状态信息：

```
%%OPR FEIDBGCMD: RUNAME="VNRS_IP_RU_C24_0064", CMDMSG="fei init";%%
RETCODE = 0  操作成功

结果如下:
---------
调试命令执行结果返回信息  =  
 DeployMode=0
 [FEI]    
 cpStateMachine=0
 pipeState=0 
 dpReadyFlag=0
 faultSmoothStartFlag=0
 faultSmoothEndFlag=1

 [SFE]
 dpStateMachine=0
 pipeState=0
 cpReadyFlag=0
 cpInitCfgFlag=0
 fwdAllowedFlag=0
 bfdSendAllowedFlag=0
 fwdResInitFlag=0

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/OPR-FEIDBGCMD.md`
