# 执行FEI调试命令（OPR FEIDBGCMD）

- [命令功能](#ZH-CN_CONCEPT_0000001707465522__1.4.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001707465522__1.4.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001707465522__1.4.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001707465522__1.4.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001707465522__1.4.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001707465522__1.4.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001707465522)

该命令用于在VNRS_VNFC上执行FEI调试命令。

#### [注意事项](#ZH-CN_CONCEPT_0000001707465522)

- 该命令用于收集定位信息，需要谨慎执行，请在华为工程师指导下执行。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001707465522)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001707465522)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数。<br>参数含义：指定RU的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围1～63。<br>默认值：无。<br>配置原则：参考<br>**[DSP RU](../../../../../单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)**<br>命令查询RU编号。 |
| CMDMSG | 调试命令字符串 | 可选必选说明：必选参数。<br>参数含义：调试命令字符串。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围1～255。<br>默认值：无。<br>配置原则：参考使用指南。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001707465522)

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

#### [输出结果说明](#ZH-CN_CONCEPT_0000001707465522)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 调试命令执行结果返回信息 | 调试命令的执行结果信息。<br>字符串类型，长度为：1～32765。 |
