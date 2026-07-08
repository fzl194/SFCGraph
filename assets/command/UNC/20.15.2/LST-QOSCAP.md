---
id: UNC@20.15.2@MMLCommand@LST QOSCAP
type: MMLCommand
name: LST QOSCAP（查询Non-GBR承载QoS限制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSCAP
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
- Non-GBR承载QoS限制
status: active
---

# LST QOSCAP（查询Non-GBR承载QoS限制配置）

## 功能

**适用网元：MME**

该命令用于查询QoS限制配置信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug。
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATTYPE | RAT类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的接入类型，系统优先匹配与当前用户所处网络类型相同的配置数据，当相同RAT类型配置中不包含该用户时，再进行<br>“ALL”<br>类型的匹配。<br>数据来源：整网规划<br>取值范围：<br>- “ALL(ALL)”<br>- “GERAN(GERAN)”<br>- “UTRAN(UTRAN)”<br>- “E-UTRAN(E-UTRAN)”<br>- “NB-IoT(NB-IoT)”<br>默认值：无 |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待增加Non-GBR承载QoS限制配置的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “HOME_USER(本网用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数必须先由<br>[**ADD QOSCAP**](增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)<br>命令定义，才能在此处引用。<br>数据来源：整网规划<br>取值范围：0～64，128～254。<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于系统根据对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数必须先由<br>[**ADD QOSCAP**](增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)<br>命令定义，才能在此处引用。<br>取值范围：5～15位数字。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QOSCAP]] · Non-GBR承载QoS限制配置（QOSCAP）

## 使用实例

1. 不输入IMSI前缀，查询所有QoS限制配置。
  LST QOSCAP:;
  ```
  %%LST QOSCAP:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
  RAT类型   用户范围  运营商标识 IMSI前缀      上行UE AMBR （kbps）    下行UE AMBR （kbps）    上行APN AMBR （kbps）    下行APN AMBR （kbps）    QCI（Non-GBR承载）    ARP的优先级别（Non-GBR承载）    ARP的抢占能力（Non-GBR承载）    ARP的被抢占能力（Non-GBR承载）    仅使用配置QoS限制    网络提升Non-GBR承载QoS    PDN连接建立拒绝原因值    拒绝Non-GBR承载建立/修改NAS原因值    拒绝Non-GBR承载建立/修改GTPC原因值    Non-GBR专有承载控制策略    移动网络名称

  ALL   IMSI_PREFIX  NULL   3080107000    10000                   20000                   5000                     10000                    8                     10                              启用                            未启用                            是                   接受QoS                   0                        0                                    0                                     同缺省承载                 noname      
  ALL   IMSI_PREFIX  NULL   3080108000    20000                   40000                   10000                    20000                    5                     10                              未启用                          未启用                            是                   接受QoS                   0                        0                                    0                                     同缺省承载                 noname      
  (结果个数 = 2)
  ---    END
  ```
2. 输入IMSI前缀，查询所有IMSI前缀为3080107000的QoS限制配置。
  LST QOSCAP: RATTYPE=ALL, SUBRANGE=IMSI_PREFIX, IMSIPRE="3080107000";
  ```
  %%LST QOSCAP: RATTYPE=ALL, SUBRANGE=IMSI_PREFIX, IMSIPRE="3080107000";%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
                             RAT类型  =  ALL
                            用户范围  = 指定IMSI前缀
  			 运营商标识 = NULL
                            IMSI前缀  =  3080107000
                上行UE AMBR （kbps）  =  10000
                下行UE AMBR （kbps）  =  20000
               上行APN AMBR （kbps）  =  5000
               下行APN AMBR （kbps）  =  10000
                  QCI（Non-GBR承载）  =  8
        ARP的优先级别（Non-GBR承载）  =  10
        ARP的抢占能力（Non-GBR承载）  =  启用
      ARP的被抢占能力（Non-GBR承载）  =  未启用
                   仅使用配置QoS限制  =  是
              网络提升Non-GBR承载QoS  =  接受QoS
               PDN连接建立拒绝原因值  =  0
   拒绝Non-GBR承载建立/修改NAS原因值  =  0
  拒绝Non-GBR承载建立/修改GTPC原因值  =  0
             Non-GBR专有承载控制策略  =  同缺省承载
                        移动网络名称  =  noname
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-QOSCAP.md`
