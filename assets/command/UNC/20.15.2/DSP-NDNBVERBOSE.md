---
id: UNC@20.15.2@MMLCommand@DSP NDNBVERBOSE
type: MMLCommand
name: DSP NDNBVERBOSE（查询邻居表项详细信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NDNBVERBOSE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- ND
status: active
---

# DSP NDNBVERBOSE（查询邻居表项详细信息）

## 功能

该命令用于查询邻居表项详细信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFQUERYTYPE | 查询接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定接口查询类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IFINDEX：接口索引。<br>- IFNAME：接口名称。<br>默认值：无 |
| IFINDEX | 接口索引 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IFQUERYTYPE”配置为“IFINDEX”时为必选参数。<br>参数含义：该参数用来指定接口索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967294。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IFQUERYTYPE”配置为“IFNAME”时为必选参数。<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| IPV6ADDR | IPv6地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NDNBVERBOSE]] · 邻居表项详细信息（NDNBVERBOSE）

## 使用实例

- 基于接口名查询邻居表项详细信息：
  ```
  DSP NDNBVERBOSE:IFQUERYTYPE=IFNAME,IFNAME="Ethernet64/0/3",IPV6ADDR="2001:db8::1";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  邻居表项详细信息  =
      uiIfIndex              : 6
      stNbAddr               : 2001:db8::1
      uiReachableTimeElapsed : 102278
      uiPreDetectReachTime   : 102278
      uiTimeStamp            : 10239029
      uiExpire               : 103478
      aucLLAddr              : 00E0-FC40-1504
      ucLLAddrFlag           : 1
      ucIsRouter             : 1
      ucState                : 1
      ucIsStaticEntry        : 0
      ucNsTimes              : 0
      ucNdMissFlag           : 0
      ucToBeDelete           : 0
      uiHaLastUpdateTime     : 0
      uiHaState              : 0
      uiHaTransNo            : 0
      ucMustNotifyFes        : 0
      ucNotifyFesNbState     : 1
      ucNdReqFlag            : 0
      uiNdReqTime            : 25313
      uiWorkIfIndex          : 0
      usVlanID               : 0
      uiVrIndex              : 0
      uiVrfindex             : 0
      uiIfPhyType            : 0
      uiParentIfPhyType      : 0
      uiIfLinkType           : 0
      uiIfEncapType          : 255
      uiFlowId               : 4294967295
      ucNetWorkRole          : 0
      linkinfo               : [
       ETH_INFO(TlvType = 0, TlvLength = 20, SrcMac = 00E0-FC40-1504, DstMac = 00E0-FC20-1504, IfIndex = 6, Priority = 0, Reserved = 0, Flag = 0)
       OTHER_INFO(TlvType = 255, TlvLength = 16)
      ]

  (结果个数 = 1)
  ---    END
  ```
- 基于接口索引查询邻居表项详细信息：
  ```
  DSP NDNBVERBOSE:IFQUERYTYPE=IFINDEX,IFINDEX=6,IPV6ADDR="2001:db8::1";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  邻居表项详细信息  =
      uiIfIndex              : 6
      stNbAddr               : 2001:db8::1
      uiReachableTimeElapsed : 102278
      uiPreDetectReachTime   : 102278
      uiTimeStamp            : 10359054
      uiExpire               : 104678
      aucLLAddr              : 00E0-FC40-1504
      ucLLAddrFlag           : 1
      ucIsRouter             : 1
      ucState                : 2
      ucIsStaticEntry        : 0
      ucNsTimes              : 0
      ucNdMissFlag           : 0
      ucToBeDelete           : 0
      uiHaLastUpdateTime     : 0
      uiHaState              : 0
      uiHaTransNo            : 0
      ucMustNotifyFes        : 0
      ucNotifyFesNbState     : 1
      ucNdReqFlag            : 0
      uiNdReqTime            : 25313
      uiWorkIfIndex          : 0
      usVlanID               : 0
      uiVrIndex              : 0
      uiVrfindex             : 0
      uiIfPhyType            : 0
      uiParentIfPhyType      : 0
      uiIfLinkType           : 0
      uiIfEncapType          : 255
      uiFlowId               : 4294967295
      ucNetWorkRole          : 0
      linkinfo               : [
       ETH_INFO(TlvType = 0, TlvLength = 20, SrcMac = 00E0-FC40-1504, DstMac = 00E0-FC20-1504, IfIndex = 6, Priority = 0, Reserved = 0, Flag = 0)
       OTHER_INFO(TlvType = 255, TlvLength = 16)
      ]

  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NDNBVERBOSE.md`
