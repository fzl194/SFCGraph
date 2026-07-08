# 查询基于QCI的Non-GBR承载QoS限制配置(LST QOSCAPBYQCI)

- [命令功能](#ZH-CN_MMLREF_0000001172225901__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225901__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225901__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225901__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225901__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225901__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172225901__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225901)

**适用网元：MME**

该命令用于查询用户范围和承载QCI的Non-GBR承载QoS限制配置记录。

#### [注意事项](#ZH-CN_MMLREF_0000001172225901)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225901)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225901)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225901)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数表示使用QoS限制的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”：指网络中的所有用户<br>- “IMSI_PREFIX(指定IMSI前缀)：指网络中与指定的IMSI前缀匹配的用户。”<br>- “HOME_USER(本网用户)：指网络中的本网签约用户。”<br>- “FOREIGN_USER(外网用户)：指网络中的漫游用户。”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：整网规划<br>取值范围：5~15位数字。<br>默认值：无 |
| QCI | QCI | 可选必选说明：可选参数<br>参数含义：该参数表示使用QoS限制的用户签约的承载的QCI。<br>数据来源：整网规划<br>取值范围：1~9<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225901)

1. 查询所有QoS限制配置。
  LST QOSCAP:;
  ```
  %%LST QOSCAPBYQCI:;%%
  RETCODE = 0  操作成功

  操作结果如下：
  --------------
 
  用户范围      IMSI前缀    QCI     本地配置QCI  是否覆盖网关下发的QCI  ARP的优先级别  ARP的抢占能力  ARP的被抢占能力  上行最大速率 (kbps)  下行最大速率 (kbps)  上行保证速率 (kbps)  下行保证速率 (kbps)  描述信息

  指定IMSI前缀  3080107000  5       1            否                     1              未启用         未启用           0                    0                    0                    0                    For MobileNet1  
  指定IMSI前缀  3080108000  6       1            否                     1              启用           启用             0                    0                    0                    0                    For MobileNet2

  (结果个数 = 2)

  ---    END
  ```
2. 查询所有IMSI前缀为3080107000，QCI为5的QoS限制配置。
  LST QOSCAPBYQCI: SUBRANGE=IMSI_PREFIX, IMSIPRE="3080107000", QCI=5;
  ```
  %%LST QOSCAPBYQCI: SUBRANGE=IMSI_PREFIX, IMSIPRE="3080107000", QCI=5;%%
  RETCODE = 0  操作成功

  操作结果如下：
  --------------
               用户范围  =  指定IMSI前缀
               IMSI前缀  =  3080107000
                    QCI  =  5
            本地配置QCI  =  1
  是否覆盖网关下发的QCI  =  否
          ARP的优先级别  =  1
          ARP的抢占能力  =  未启用
        ARP的被抢占能力  =  未启用
    上行最大速率 (kbps)  =  0
    下行最大速率 (kbps)  =  0
    上行保证速率 (kbps)  =  0
    下行保证速率 (kbps)  =  0
               描述信息  =  For MobileNet1
  (结果个数 = 1)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172225901)

请参考 [**ADD QOSCAPBYQCI**](增加基于QCI的Non-GBR承载QoS限制配置(ADD QOSCAPBYQCI)_26306032.md) 命令的参数标识。
