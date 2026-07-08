---
id: UNC@20.15.2@MMLCommand@DSP COMPSTATTRACE
type: MMLCommand
name: DSP COMPSTATTRACE（显示当前组件的状态记录信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMPSTATTRACE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 进程和组件信息
status: active
---

# DSP COMPSTATTRACE（显示当前组件的状态记录信息）

## 功能

该命令用于显示当前组件的状态历史记录信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMPCID | 组件ID | 可选必选说明：必选参数<br>参数含义：该参数表示组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| PROCESS | 进程ID | 可选必选说明：必选参数<br>参数含义：该参数表示进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/COMPSTATTRACE]] · 当前组件的状态记录信息（COMPSTATTRACE）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示当前组件的状态记录信息（DSP-COMPSTATTRACE）_59104024.md`
