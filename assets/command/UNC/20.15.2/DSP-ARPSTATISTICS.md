---
id: UNC@20.15.2@MMLCommand@DSP ARPSTATISTICS
type: MMLCommand
name: DSP ARPSTATISTICS（显示ARP处理信息统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ARPSTATISTICS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP统计查询
status: active
---

# DSP ARPSTATISTICS（显示ARP处理信息统计）

## 功能

该命令用于显示ARP处理统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GETINFOTYPE | 信息类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查看信息的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Table：基于表项查询统计。<br>- Packet：基于报文查询统计。<br>默认值：无 |
| ARPPID | ARP组件PID | 可选必选说明：条件可选参数<br>前提条件：该参数在“GETINFOTYPE”配置为“Packet” 或 “Table”时为可选参数。<br>参数含义：该参数用于指定APP查看信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GETINFOTYPE”配置为“Packet”时为可选参数。<br>参数含义：该参数用于显示指定处理ARP报文的接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ARPSTATISTICS]] · ARP处理信息统计（ARPSTATISTICS）

## 使用实例

- 显示ARP报文处理统计信息计数：
  ```
  DSP ARPSTATISTICS:GETINFOTYPE=Packet;
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  -------------------------
                               收到请求报文数量  =  8518
                               收到应答报文数量  =  10803
                               发送请求报文数量  =  2
                               发送应答报文总数  =  3120
                               收到ARP Miss数量  =  2
                     发送MISS触发的请求报文数量  =  1
                           表项老化探测报文次数  =  0
                         SLA触发ARP请求报文数量  =  0
                               申请内存失败次数  =  0
                            Mbuffer处理失败次数  =  0
                  接口不存在造成ARP报文丢弃数量  =  0
                    接口Down造成ARP报文丢弃数量  =  0
                  Vlan不存在造成ARP报文丢弃数量  =  0
                PV关系不存在造成ARP报文丢弃数量  =  0
                  PV状态Down造成ARP报文丢弃数量  =  0
                          ARP报文头检查失败数量  =  0
                       ARP报文源MAC检查失败数量  =  0
                      ARP报文IP地址检查失败数量  =  701
                                免费ARP丢弃数量  =  0
                      报文与IP Pool匹配失败数量  =  0
                   ARP报文MAC有效性检查失败数量  =  0
                            ARP限速丢弃报文数量  =  0
                         缺少策略表丢弃报文数量  =  0
                         IP地址冲突丢弃报文数量  =  3121
  IP地址是网段地址或者广播地址的ARP报文丢弃数量  =  0
                           非同网段丢弃报文数量  =  15499
                        检查DAI失败丢弃报文数量  =  0
                                 MAC联动ARP次数  =  0
                             MAC联动ARP成功次数  =  0
  (结果个数 = 1)
  ---    END
  ```
- 显示ARP表项处理统计信息计数：
  ```
  DSP ARPSTATISTICS:GETINFOTYPE=Table;
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  -------------------------
                    表项老化数量 = 1
            Reset删除ARP表项数量 = 1
         接口Down删除ARP表项数量 = 0
     接口删除联动删除ARP表项数量 = 0
   接口IP删除联动删除ARP表项数量 = 0
  LocalCe删除联动删除ARP表项数量 = 0
       流删除联动删除ARP表项数量 = 0
              HA过程产生表项数量 = 0
              假表项老化删除数量 = 123
    Dot1q删除联动删除ARP表项数量 = 1
                静态表项删除数量 = 1
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ARPSTATISTICS.md`
