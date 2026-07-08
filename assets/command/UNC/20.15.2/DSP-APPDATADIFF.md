---
id: UNC@20.15.2@MMLCommand@DSP APPDATADIFF
type: MMLCommand
name: DSP APPDATADIFF（查询APP与OMU配置数据差异信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: APPDATADIFF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 配置维护
- APP配置检查
status: active
---

# DSP APPDATADIFF（查询APP与OMU配置数据差异信息）

## 功能

该命令用于查询APP配置数据和主控OMU配置数据的差异信息。

这些信息是在检查进程APP与主控OMU配置数据，发现数据不一致时，记录下来的差异信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INFOLEVEL | 信息级别 | 可选必选说明：必选参数<br>参数含义：信息级别。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TABLE：表级差异。<br>- RECORD：记录级差异。<br>- PROCESS：进程级差异。<br>默认值：无 |
| PROCESSID | 进程ID | 可选必选说明：条件必选参数，该参数在“INFOLEVEL”配置为“TABLE” 或 “RECORD”时为必选参数。<br>参数含义：进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| APPTABLENAME | APP表名称 | 可选必选说明：条件必选参数，该参数在“INFOLEVEL”配置为“RECORD”时为必选参数。<br>参数含义：进程APP表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APPDATADIFF]] · APP与OMU配置数据差异信息（APPDATADIFF）

## 使用实例

- 查询APP配置数据与OMU配置数据不一致的进程信息：
  ```
  DSP APPDATADIFF:INFOLEVEL=PROCESS
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0 操作成功

  结果如下
  ----------
  进程ID        RU名称 
  3             OMU1   
  1000          OMU1   
  1001          OMU1                           
  (结果个数 = 2)
  --- END
  ```
- 查询1000号进程APP配置数据和OMU配置数据不一致的表信息：
  ```
  DSP APPDATADIFF:INFOLEVEL=TABLE,PROCESSID=1000
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0 操作成功

  结果如下
  ---------
  进程ID        APP表名称          OMU表名称  
  1000          APPVIntfModeOne    Interface      
  1000          vVsSysCfgDam       VsSysCfg       
  1000          IFMVInterface      Interface      
  1000          IFMVIfInnerCfg     IfInnerCfg     
  1000          vACLFwdGroup       ACLGroup       
  1000          FESVifTable        Interface      
  1000          FESVIfService      Interface      
  1000          FESVIfAdmState     Interface      
  1000          APPVIntfModeThr    Interface      
  1000          VEUMSystem         VsSysCfg       
  1000          vVrrpBaseGlobal    VrrpBaseGlobal                           
  (结果个数 = 11)
  --- END
  ```
- 查询1000号进程APP表vVsSysCfgDam配置数据和OMU配置数据不一致的记录信息：
  ```
  DSP APPDATADIFF:INFOLEVEL=RECORD,PROCESSID=1000,APPTABLENAME="vVsSysCfgDam"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0 操作成功

  结果如下
  ---------
  进程ID        APP表名称         记录差异

  1000          vVsSysCfgDam      KEY( VsId              , LsId              ) 
  1000          vVsSysCfgDam       * ( 0x0               , 0x0               ) 
                    
  (结果个数 = 2)
  --- END
  ```
- 查询1000号进程APP表vACLFwdGroup配置数据和OMU配置数据不一致的记录信息：
  ```
  DSP APPDATADIFF:INFOLEVEL=RECORD,PROCESSID=1000,APPTABLENAME="vACLFwdGroup"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  ----------------------
  进程ID        APP表名称         记录差异                            

  1000          vACLFwdGroup      KEY( aclVrid           , aclGroupId        ) 
  1000          vACLFwdGroup       + ( 0x0               , 0x6               ) 
  1000          vACLFwdGroup       - ( 0x0               , 0x2               ) 
  1000          vACLFwdGroup       - ( 0x0               , 0x4               ) 
  1000          vACLFwdGroup       - ( 0x0               , 0x5               ) 
  (结果个数 = 5)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APP与OMU配置数据差异信息（DSP-APPDATADIFF）_59103640.md`
