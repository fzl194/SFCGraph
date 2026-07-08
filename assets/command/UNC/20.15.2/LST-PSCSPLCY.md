---
id: UNC@20.15.2@MMLCommand@LST PSCSPLCY
type: MMLCommand
name: LST PSCSPLCY（查询联合接入策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PSCSPLCY
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- 联合接入管理
status: active
---

# LST PSCSPLCY（查询联合接入策略）

## 功能

**适用网元：MME**

该命令用于查询联合接入策略。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/PSCSPLCY]] · 联合接入策略（PSCSPLCY）

## 使用实例

查询联合接入策略：

```
+++    UNC/*MEID:0 MENAME:unc*/        2023-08-15 10:57:34 
O&M    #1018 
%%LST PSCSPLCY:;%% RETCODE = 0  操作成功  
查询结果如下 
------------           
            是否开启联合接入限制功能  =  否               
                联合接入限制通用条件  =  IMS APN&IMSCAP&STNSR                       
                        预设STN-SR值  =  NULL                         
                          白名单策略  =  HSS标识           
            是否开启联合附着限制功能  =  否            
             是否开启联合TAU限制功能  =  否     
      无IMS PDN连接时是否限制联合TAU  =  否               
                联合接入是否响应成功  =  是           
            UE发起CS业务时是否驻留4G  =  否     
      手动HSS Bypass时用户是否驻留4G  =  否                 
                  联合接入限制原因值  =  CS_DOMAIN_NOT_AVAILABLE(#18 CS domain not available)               
                是否开启无CS控制策略  =  否                   
                    无CS规划识别条件  =  TAILAI                       
                        用户识别条件  =  IMS APN&IMSCAP 
  无CS规划用户是否响应联合接入假成功  =  否 
  无CS规划的UE发起CS业务时是否驻留4G  =  是       
        无CS规划的联合接入限制原因值  =  CS_DOMAIN_NOT_AVAILABLE(#18 CS domain not available)    
     联合接入响应假成功时LAI填写策略  =  TAI映射                      
                       LAI固定填充值  =  NULL 
(结果个数 = 1)  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PSCSPLCY.md`
