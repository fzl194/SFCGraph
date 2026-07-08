---
id: UNC@20.15.2@MMLCommand@LST SMFFUNC
type: MMLCommand
name: LST SMFFUNC（查询SMF扩展功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFFUNC
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话管理拓展功能
- 5GC会话管理拓展功能
status: active
---

# LST SMFFUNC（查询SMF扩展功能）

## 功能

**适用NF：SMF**

该命令用于查询会话管理相关的功能控制，如是否支持兴趣区、是否支持本地数据网络、支持哪种业务和会话连续性模式等参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFFUNC]] · SMF扩展功能（SMFFUNC）

## 使用实例

查询所有SMFFUNC记录：

```
%%LST SMFFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
                                    兴趣区  =  不支持
                                  本地网络  =  不支持
                              本地网络策略  =  释放
                                   SSC模式  =  模式一
                  SMF是否支持向AMF分配EBID  =  支持
                   是否支持PaaMask私有信元  =  支持
                   是否支持QerType私有信元  =  不支持
                        IPv6本地UP分流策略  =  BP优先
                            SMF是否支持BSF  =  不支持
                        SMF是否支持AMF容灾  =  不支持
                 是否去激活故障AMF上的用户  =  不支持
         SMF是否支持隐式去订阅签约数据通知  =  不支持
            订阅签约数据通知超时时间(分钟)  =  1440
                                UE可达功能  =  不支持
                  是否在EPS获取签约的NSSAI  =  否
                       SMF是否支持野卡接入  =  不支持
                               PPI功能开关  =  使能
                 故障原因值重选UPF功能开关  =  不使能
                        事件订阅与上报功能  =  不支持
                    是否支持建立5G LAN会话  =  不支持
                        跨切片保护功能开关  =  关闭
                             V-SMF特性开关  =  不支持
                             QoS流通知控制  =  不支持
                       AMF服务发现控制开关  =  不使能
        5G LAN会话是否向UDM查询VnGroupData  =  支持
                       冗余PDU会话特性开关  =  不支持
                              ISMF核查开关  =  关闭
                            RedCap特性开关  =  不支持
              通用DNN会话UE IP地址处理开关  =  不支持
       SMF支持基于binding的AMF热备特性开关  =  支持
                        ProxySMFS8特性开关  =  不支持
BSF支持基于DNN过滤查询会话绑定信息特性开关  =  不支持
                      访地专网策略处理开关  =  不支持
     SMF支持异厂商信令安全网关热备特性开关  =  不支持
                           N16aSMF核查开关  =  关闭
                      网络切片替换功能开关  =  不支持
  WLAN切换NG-RAN失败转EPS FallBack功能开关  =  不支持
                           PDU Set Qos开关  =  不支持
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFFUNC.md`
