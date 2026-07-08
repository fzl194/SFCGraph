---
id: UNC@20.15.2@MMLCommand@LST APNRDSACCTCTRL
type: MMLCommand
name: LST APNRDSACCTCTRL（查询APN RADIUS计费控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNRDSACCTCTRL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS计费管理
- APN计费控制
status: active
---

# LST APNRDSACCTCTRL（查询APN RADIUS计费控制参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用来显示指定APN的RADIUS客户端计费信令控制属性的配置。

## 注意事项

如果不输入参数，则查询全部APN的RADIUS客户端计费信令控制属性的配置。如果输入参数，则查询指定APN的RADIUS客户端计费信令控制属性的配置信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：基于该APN配置RADIUS计费控制参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN RADIUS计费控制参数（APNRDSACCTCTRL）](configobject/UNC/20.15.2/APNRDSACCTCTRL.md)

## 使用实例

- 查询名为“apn1”的APN的RADIUS计费控制参数信息：
  ```
  LST APNRDSACCTCTRL:APN="apn1";
  ```
  ```

  RETCODE = 0  操作成功。

  APN Radius计费控制参数
  ----------------------
                                                  APN名称  =  apn1
                                           时间阈值（分）  =  0
                                       流量阈值（千字节）  =  0
                   全部类型承载/PDP上下文均开启radius计费  =  全部承载
          业务报文（通过3/4层规则配置）时触发计费请求消息  =  不使能
                                   业务报文延时时间（秒）  =  0
             等待计费开始响应消息后才回应激活成功应答消息  =  不使能
                                 Acct请求超时是否去活用户  =  去活
  未收到Accounting Response （START）是否发送计费停止消息  =  不发送消息
                       未收到计费开始的响应消息前转发数据  =  不允许转发
     MME或SGSN/SGW发起PDP上下文更新时是否支持发送计费更新  =  发送消息
                         IPv4 Address释放触发计费更新消息  =  不触发消息
                                  QoS变化触发计费更新消息  =  触发消息
                                  RAT变化触发计费更新消息  =  触发消息
                             SGSN/SGW变化触发计费更新消息  =  触发消息
                                  ULI变化触发计费更新消息  =  触发消息
                             WLAN地址变化触发计费更新消息  =  不触发消息
                                 缓存Account Stop消息开关  =  不缓存
                                     等待计费更新响应消息  =  不等待
                          URL过滤规则变化触发计费更新消息  =  不触发消息
                                                  CRBN变化 = 不触发消息
  (结果个数 = 1)
  ---    END
  ```
- 查询全部APN的RADIUS计费控制参数信息：
  ```
  LST APNRDSACCTCTRL:;
  ```
  ```

  RETCODE = 0  操作成功

  APN Radius计费控制参数
  ----------------------
  APN名称      时间阈值（分）  流量阈值（千字节）  全部类型承载/PDP上下文均开启radius计费  业务报文（通过3/4层规则配置）时触发计费请求消息  MME或SGSN/SGW发起PDP上下文更新时是否支持发送计费更新  IPv4 Address释放触发计费更新消息  QoS变化触发计费更新消息  RAT变化触发计费更新消息  SGSN/SGW变化触发计费更新消息  ULI变化触发计费更新消息  WLAN地址变化触发计费更新消息  缓存Account Stop消息开关  等待计费更新响应消息  URL过滤规则变化触发计费更新消息  Acct请求超时是否去活用户  等待计费开始响应消息后才回应激活成功应答消息  未收到Accounting Response （START）是否发送计费停止消息  业务报文延时时间（秒）  CRBN变化    

  apn1         0               0                   全部承载                                不使能                                           发送消息                                              不触发消息                        触发消息                 触发消息                 触发消息                      触发消息                 不触发消息                    不缓存                    不等待                不触发消息                       去活                      不使能                                        不发送消息                                               0                       不触发消息  
  apn2         0               0                   全部承载                                不使能                                           发送消息                                              不触发消息                        触发消息                 触发消息                 触发消息                      触发消息                 不触发消息                    不缓存                    不等待                不触发消息                       去活                      不使能                                        不发送消息                                               0                       不触发消息  
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN-RADIUS计费控制参数（LST-APNRDSACCTCTRL）_09896771.md`
