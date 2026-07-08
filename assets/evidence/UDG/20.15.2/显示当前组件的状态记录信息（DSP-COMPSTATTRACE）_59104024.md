# 显示当前组件的状态记录信息（DSP COMPSTATTRACE）

- [命令功能](#ZH-CN_CONCEPT_0259104024__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0259104024__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0259104024__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0259104024__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0259104024__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0259104024__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0259104024)

该命令用于显示当前组件的状态历史记录信息。

#### [注意事项](#ZH-CN_CONCEPT_0259104024)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0259104024)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0259104024)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMPCID | 组件ID | 可选必选说明：必选参数<br>参数含义：该参数表示组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| PROCESS | 进程ID | 可选必选说明：必选参数<br>参数含义：该参数表示进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### [使用实例](#ZH-CN_CONCEPT_0259104024)

显示当前组件的状态历史记录信息：

```
DSP COMPSTATTRACE:COMPCID="8BF1001C",PROCESS=1000
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
时间                                  事件                                                                                      

Jun  5 2017 20:55:06.516+02:00 DST       SEM: R_ST:NULL            R_Ver:         V_TM:0  Trans:0xffffffff Stage:InitInstCB      
Jun  5 2017 20:55:10.797+02:00 DST    SEMAGT: Create component.                                                                  
Jun  5 2017 20:55:10.797+02:00 DST    SEMAGT: Request resource.                                                                  
Jun  5 2017 20:55:10.797+02:00 DST    SEMAGT: Get request resource response.                                                     
Jun  5 2017 20:55:10.797+02:00 DST    SEMAGT: Constuct stage1 begin.                                                             
Jun  5 2017 20:55:10.825+02:00 DST    SEMAGT: Constuct stage1 end.                                                               
Jun  5 2017 20:55:10.825+02:00 DST    SEMAGT: Constuct stage2 begin.                                                             
Jun  5 2017 20:55:10.825+02:00 DST    SEMAGT: Constuct stage2 end.                                                               
Jun  5 2017 20:55:10.825+02:00 DST    SEMAGT: Request app data.                                                                  
Jun  5 2017 20:55:12.902+02:00 DST       SEM: R_ST:NULL            Stage:SndNtfCompStat                                          
Jun  5 2017 20:55:12.902+02:00 DST    SEMAGT: Receive app data response.                                                         
Jun  5 2017 20:55:12.902+02:00 DST    SEMAGT: Constuct stage3 begin.                                                             
Jun  5 2017 20:55:12.902+02:00 DST    SEMAGT: Constuct stage3 end.                                                               
Jun  5 2017 20:55:12.902+02:00 DST    SEMAGT: Send startwork to app.                                                             
Jun  5 2017 20:55:12.982+02:00 DST    SEMAGT: Receive startwork response from app.                                               
Jun  5 2017 20:55:12.982+02:00 DST    SEMAGT: Send startwork response to sem.                                                    
Jun  5 2017 20:55:12.982+02:00 DST    SEMAGT: R_ST:Primary         R_Ver:1.2.103  V_TM:1  Trans:0x7f2d     Stage:InsFsmActI      
Jun  5 2017 20:55:13.000+02:00 DST       SEM: R_ST:NULL            Stage:RefrCAMtoPeer                                           
Jun  5 2017 20:55:13.000+02:00 DST       SEM: R_ST:NULL            Stage:RefCAMRelAllLoc                                         
Jun  5 2017 20:55:13.000+02:00 DST       SEM: R_ST:NULL            Stage:RefrSubsCAM                                             
Jun  5 2017 20:55:13.000+02:00 DST       SEM: R_ST:Primary         R_Ver:1.2.103  V_TM:0  Trans:0xc031c593 Stage:ProcCompState   
Jun  5 2017 20:55:27.765+02:00 DST       SEM: R_ST:Primary         Stage:RefrCAMtoPeer                                           
Jun  5 2017 20:55:27.765+02:00 DST       SEM: R_ST:Primary         Stage:RefCAMRelAllLoc                                         
Jun  5 2017 20:55:27.765+02:00 DST       SEM: R_ST:Primary         Stage:RefrSubsCAM                                             
Jun  5 2017 20:55:27.769+02:00 DST       SEM: Update component avalible.                                                         
Jun  5 2017 20:55:27.769+02:00 DST       SEM: Update component avalible.                                                         
Jun  5 2017 20:55:27.769+02:00 DST       SEM: R_ST:BackupReady     R_Ver:1.2.103  V_TM:4  Trans:0xc031c593 Stage:ProcCompState   
Jun  5 2017 20:55:27.769+02:00 DST       SEM: R_ST:BackupReady     R_Ver:1.2.103  V_TM:4  Trans:0xc031c593 Stage:ProcCompState   
Jun  5 2017 20:55:27.769+02:00 DST       SEM: R_ST:Primary         Stage:RefrCAMtoPeer                                           
Jun  5 2017 20:55:27.769+02:00 DST       SEM: R_ST:Primary         Stage:RefCAMRelAllLoc                                         
Jun  5 2017 20:55:27.769+02:00 DST       SEM: R_ST:Primary         Stage:RefrSubsCAM                                             
Jun  5 2017 20:55:27.769+02:00 DST       SEM: R_ST:Primary         Stage:RefrSubsCAM                                             
Jun  5 2017 20:55:27.767+02:00 DST    SEMAGT: Receive newbackup response.                                                        
Jun  5 2017 20:55:27.769+02:00 DST    SEMAGT: R_ST:BackupReady     R_Ver:1.2.103  V_TM:4  Trans:0x7f2d     Stage:InsFsmActQ      
Jun  5 2017 20:55:27.769+02:00 DST    SEMAGT: Receive backupready from app.                                                                                                              
(结果个数 = 35)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0259104024)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 时间 | 表示事件发生时间。 |
| 事件 | 表示启动时发送的事件。 |
