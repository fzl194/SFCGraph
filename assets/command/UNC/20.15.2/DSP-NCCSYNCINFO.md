---
id: UNC@20.15.2@MMLCommand@DSP NCCSYNCINFO
type: MMLCommand
name: DSP NCCSYNCINFO（查询NETCONFC的配置同步信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCCSYNCINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 网络配置协议客户端
status: active
---

# DSP NCCSYNCINFO（查询NETCONFC的配置同步信息）

## 功能

该命令用于查询NETCONFC的配置同步信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERID | 远端ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示远端设备ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| DATATYPE | 数据类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示配置对账信息的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SYNCCONFIG：对账信息。<br>默认值：SYNCCONFIG |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCCSYNCINFO]] · NETCONFC的配置同步信息（NCCSYNCINFO）

## 使用实例

- 查询VNF内NETCONFC的配置同步信息：
  ```
  DSP NCCSYNCINFO:PEERID=1025
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  配置同步的信息 =
  -----------------------------------------------------------
  Data sync base info:
     MaxRetryCount:    3          RetryCount:           0       
     MaxBackoffCount:  3          BackoffCount:         1       
     IsForbid:         FALSE      FsmState:             INIT
     Sync Reason:      PERIODICAL    
     PeriodSyncTime(rand in one hour):  03:00:00
     GetLocalAppDataTime(us):           8586484         
     GetPeerAppDataTime(us):            9997749         
     SyncingAppDataTime(us):            16431366        
  -----------------------------------------------------------
  ###########################################################
  Data sync process info:
     SyncRate:         100     
     SyncResult:       OK      
     SyncType:         PERIOD 
     SyncingApp:               
     BeginTime:        2018-06-13, 03:32:08:550
     EndTime:          2018-06-13, 03:32:28:188
  -----------------------------------------------------------
  APP: sampleAM_DEP
     ReadAppDBCount:    1           GetConfigCount:       2       
     LocalDataReady:    TRUE        PeerDataReady:        TRUE    
     SyncSucceed:       TRUE        GetPeerRetCode:       0x0       
     DiffRetCode:       0x0         SyncRetCode:          0x0       
     AppendXssCount:    310         MergeRpcCount:        0       
     DeleteRpcCount:    0       
     GetLocalAppDataTime(us):   90697           
     GetPeerAppDataTime(us):    133761          
     SyncingAppDataTime(us):    0               
  -----------------------------------------------------------
  APP: sampleAM_INDEP
     ReadAppDBCount:    1           GetConfigCount:       2       
     LocalDataReady:    TRUE        PeerDataReady:        TRUE    
     SyncSucceed:       TRUE        GetPeerRetCode:       0x0       
     DiffRetCode:       0x0         SyncRetCode:          0x0       
     AppendXssCount:    220         MergeRpcCount:        0       
     DeleteRpcCount:    0       
     GetLocalAppDataTime(us):   89419           
     GetPeerAppDataTime(us):    135418          
     SyncingAppDataTime(us):    0               
  -----------------------------------------------------------

  (结果个数 = 2)
  ---    END
  ```
- 查询VNF间NETCONFC的配置同步信息：
  ```
  DSP NCCSYNCINFO:PEERID=3
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  配置同步的信息 =
  -------------------------------------------
  PeriodSyncTime(rand in one hour): 03:00:00
  IsForbid:         FALSE   
  Sync Time:        2018-06-13, 03:27:52:547 - 2018-06-13, 03:28:09:541
  Get Local:        2018-06-13, 03:27:53:367 - 2018-06-13, 03:27:57:710
  File Trans:       2018-06-13, 03:27:57:710 - 2018-06-13, 03:27:59:510
  Sync-cfg-id:      4               
  Num of APP:       14              
  Progress:         100%
  SyncResult:       Sync-cfg success
  SyncType:         PERIOD   
  Sync Reason:      PERIODICAL    
  -------------------------------------------
  Feature-Name:        sampleSYS_INDEP    
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        samplePF_INDEP     
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleCM_INDEP     
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleAM_INDEP     
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleSM_INDEP     
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleDIAM_INDEP   
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        samplePCC_INDEP    
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        samplePF_DEP       
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleDIAM_DEP     
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleCM_DEP       
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleAM_DEP       
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        samplePCC_DEP      
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleSM_DEP       
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleCOMM         
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              

  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NCCSYNCINFO.md`
