---
id: UNC@20.15.2@MMLCommand@LST NGMMPROCTRL
type: MMLCommand
name: LST NGMMPROCTRL（查询5G移动性管理流程控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGMMPROCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM流程管理
- 5G移动性管理流程控制参数
status: active
---

# LST NGMMPROCTRL（查询5G移动性管理流程控制参数）

## 功能

**适用NF：AMF**

此命令用于查询5G移动性管理流程控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROT | 流程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流程类型，根据场景来确认是否需要配置相应的流程。<br>数据来源：全网规划<br>取值范围：<br>- “AUSF_DISCOVERY（AUSF发现流程）”：AUSF发现流程<br>- “AIR（获取鉴权集流程）”：获取鉴权集流程<br>- “AUTHENTICATION（鉴权流程）”：鉴权流程<br>- “SMC（安全算法协商流程）”：UE和NAS安全算法协商流程<br>- “CHECK_IMEI（检查IMEI流程）”：检查IMEI流程<br>- “UDM_DISCOVERY（UDM发现流程）”：UDM发现流程<br>- “UDM_REGISTRATION（UDM注册流程）”：到UDM注册流程<br>- “UDM_GET_SUBSCRIBER_DATA（UDM获取签约数据流程）”：从UDM获取签约数据流程<br>- “UDM_SUBSCIBE（UDM订阅流程）”：向UDM订阅流程<br>- “PCF_DISCOVERY（PCF发现流程）”：PCF发现流程<br>- “PCF_POLICY（PCF策略交互流程）”：向PCF创建/更新策略流程<br>- “OTHER_PROC（其它流程）”：其它流程<br>- “CAG（CAG限制）”：CAG限制<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G移动性管理流程控制参数（NGMMPROCTRL）](configobject/UNC/20.15.2/NGMMPROCTRL.md)

## 使用实例

- 查询“流程类型”为“AUTHENTICATION（鉴权流程）”的5G移动性管理流程控制参数，执行如下命令：
  ```
  %%LST NGMMPROCTRL: PROT=AUTHENTICATION;%%
  RETCODE = 0  操作成功

  结果如下
  --------
          Authentication拒绝原因值(RES检查失败)  =  0
    Authentication拒绝原因值(UE返回MAC Failure)  =  0
  Authentication拒绝原因值(UE返回Synch failure)  =  0
                        AUTH HTTP过载拒绝原因值  =  0
  (结果个数 = 1)

  ---    END
  ```
- 查询全量5G移动性管理流程控制参数，执行如下命令：
  ```
  %%LST NGMMPROCTRL:;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
                Authentication拒绝原因值(RES检查失败)  =  0
          Authentication拒绝原因值(UE返回MAC Failure)  =  0
        Authentication拒绝原因值(UE返回Synch failure)  =  0
                   Check IMEI拒绝原因值(IMEI检查失败)  =  0
                                   漫游受限拒绝原因值  =  0
                        AIR拒绝原因值(USER_NOT_FOUND)  =  0
        AIR拒绝原因值(SERVING_NETWORK_NOT_AUTHORIZED)  =  0
               AIR拒绝原因值(AUTHENTICATION_REJECTED)  =  0
      AIR拒绝原因值(INVALID_HN_PUBLIC_KEY_IDENTIFIER)  =  0
                     AIR拒绝原因值(CONTEXT_NOT_FOUND)  =  0
                 AIR拒绝原因值(INVALID_SCHEME_OUTPUT)  =  0
         AIR拒绝原因值(UNSUPPORTED_PROTECTION_SCHEME)  =  0
                    UDM注册拒绝原因值(USER_NOT_FOUND)  =  0
                 UDM注册拒绝原因值(CONTEXT_NOT_FOUND)  =  0
          UDM注册拒绝原因值(UNKNOWN_5GS_SUBSCRIPTION)  =  0
                UDM注册拒绝原因值(NO_PS_SUBSCRIPTION)  =  0
               UDM注册拒绝原因值(ROAMING_NOT_ALLOWED)  =  0
                UDM注册拒绝原因值(ACCESS_NOT_ALLOWED)  =  0
                   UDM注册拒绝原因值(RAT_NOT_ALLOWED)  =  0
         UDM注册拒绝原因值(REAUTHENTICATION_REQUIRED)  =  0
                                        强制向UDM注册  =  否
            UDM获取签约数据拒绝原因值(USER_NOT_FOUND)  =  0
            UDM获取签约数据拒绝原因值(DATA_NOT_FOUND)  =  0
                    UDM订阅拒绝原因值(USER_NOT_FOUND)  =  0
          UDM订阅拒绝原因值(UNSUPPORTED_RESOURCE_URI)  =  0
                AIR拒绝原因值(SUBSCRIPTION_NOT_FOUND)  =  0
                                   区域限制拒绝原因值  =  0
                                   接入限制拒绝原因值  =  0
                     AIR拒绝原因值(Too Many Requests)  =  0
                   AIR拒绝原因值(Service Unavailable)  =  0
                                  AIR拒绝原因值(超时)  =  0
    UDM获取签约数据拒绝原因值(SUBSCRIPTION_NOT_FOUND)  =  0
         UDM获取签约数据拒绝原因值(Too Many Requests)  =  0
       UDM获取签约数据拒绝原因值(Service Unavailable)  =  0
                      UDM获取签约数据拒绝原因值(超时)  =  0
                 UDM注册拒绝原因值(Too Many Requests)  =  0
               UDM注册拒绝原因值(Service Unavailable)  =  0
                              UDM注册拒绝原因值(超时)  =  0
                 UDM订阅拒绝原因值(Too Many Requests)  =  0
               UDM订阅拒绝原因值(Service Unavailable)  =  0
                              UDM订阅拒绝原因值(超时)  =  0
               AUSF发现失败拒绝原因值(USER_NOT_FOUND)  =  0
                         AUSF发现拒绝原因值(其他原因)  =  0
                             AUSF发现拒绝原因值(流控)  =  0
                         UDM发现拒绝原因值(Not Found)  =  0
                          UDM发现拒绝原因值(其他原因)  =  0
                        	     服务区域限制拒绝原因值  =  0
                             无可用网络切片拒绝原因值  =  0
                             TA级网络切片不可用原因值  =  0
                                          强制发现UDM  =  是
  PCF策略拒绝原因值(RESOURCE_URI_STRUCTURE_NOT_FOUND)  =  0
                          PCF策略拒绝原因值(其他原因)  =  0
                         PCF发现拒绝原因值(Not Found)  =  0
                          PCF发现拒绝原因值(其他原因)  =  0
                                        ODB拒绝原因值  =  0
                               终端消息非法拒绝原因值  =  0
                                        SMC拒绝原因值  =  2
                                        SMC超时原因值  =  3		      
                                        CAG拒绝原因值  =  0	  
                              AUTH HTTP过载拒绝原因值  =  0
                    获取UDM签约数据HTTP过载拒绝原因值  =  0
                       Serving Plmn变更注册拒绝原因值  =  0
                               AUTH HTR流控拒绝原因值  =  0
                     获取UDM签约数据HTR流控拒绝原因值  =  0
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G移动性管理流程控制参数（LST-NGMMPROCTRL）_09654392.md`
