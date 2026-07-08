---
id: UNC@20.15.2@MMLCommand@LST QOSCAPBYQCI
type: MMLCommand
name: LST QOSCAPBYQCI（查询基于QCI的Non-GBR承载QoS限制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSCAPBYQCI
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- EPS QoS
- QoS限制配置
- 基于QCI的承载级QoS限制
status: active
---

# LST QOSCAPBYQCI（查询基于QCI的Non-GBR承载QoS限制配置）

## 功能

**适用网元：MME**

该命令用于查询用户范围和承载QCI的Non-GBR承载QoS限制配置记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数表示使用QoS限制的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”：指网络中的所有用户<br>- “IMSI_PREFIX(指定IMSI前缀)：指网络中与指定的IMSI前缀匹配的用户。”<br>- “HOME_USER(本网用户)：指网络中的本网签约用户。”<br>- “FOREIGN_USER(外网用户)：指网络中的漫游用户。”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：整网规划<br>取值范围：5~15位数字。<br>默认值：无 |
| QCI | QCI | 可选必选说明：可选参数<br>参数含义：该参数表示使用QoS限制的用户签约的承载的QCI。<br>数据来源：整网规划<br>取值范围：1~9<br>默认值：无 |

## 操作的配置对象

- [基于QCI的Non-GBR承载QoS限制配置（QOSCAPBYQCI）](configobject/UNC/20.15.2/QOSCAPBYQCI.md)

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于QCI的Non-GBR承载QoS限制配置(LST-QOSCAPBYQCI)_72225901.md`
