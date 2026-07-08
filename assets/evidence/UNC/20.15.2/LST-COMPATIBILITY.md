# 查询QoS兼容性配置(LST COMPATIBILITY)

- [命令功能](#ZH-CN_MMLREF_0000001126146236__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126146236__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126146236__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126146236__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126146236__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126146236__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126146236__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126146236)

**适用网元：SGSN、MME**

此命令用于查询QoS兼容性配置信息。兼容性配置是为了满足不同的运营商对协议的不同要求而作的配置。

#### [注意事项](#ZH-CN_MMLREF_0000001126146236)

此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126146236)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126146236)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126146236)

无。

#### [使用实例](#ZH-CN_MMLREF_0000001126146236)

查询QoS兼容性配置参数：

LST COMPATIBILITY:;

```
%%LST COMPATIBILITY:;%%
RETCODE = 0  操作成功。

QoS兼容性配置
-------------
               QoS映射规则  =  标准协议QoS映射规则
    Reliable Class映射规则  =  允许使用确认模式LLC
                   QoS纠正  =  是
              流量等级调整  =  不定制调整
                     APNNI  =  NULL
              上行流量调整  =  否
              上行最大速率  =  0
          扩展上行最大速率  =  0
              下行流量调整  =  否
              下行最大速率  =  0
          扩展下行最大速率  =  0
            平均吞吐量调整  =  否
              发送次序调整  =  是
GTPV1通道允许发送QoS98信元  =  否
              SAPI协商模式  =  流量等级
    Gb模式Service Handover  =  不支持
    Iu模式Service Handover  =  不支持
                       H值  =  5
                       M值  =  10
            纠正扩展比特率  =  是
                   限制MBR  =  不限制下行速率
         WCDMA到LTE网络优选 =  否
          GPRS到LTE网络优选 =  否
     发送EPS QoS Extended-2 = 否
       GTPV2通道发送扩展QCI = 支持
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126146236)

参见 [**SET COMPATIBILITY**](设置QoS兼容性配置(SET COMPATIBILITY)_72345835.md) 的参数说明。
