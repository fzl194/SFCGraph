---
id: UNC@20.15.2@MMLCommand@DSP HOSTSNDSTC
type: MMLCommand
name: DSP HOSTSNDSTC（查询发送方向协议报文统计计数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: HOSTSNDSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- 主机报文统计
- 发送报文统计
status: active
---

# DSP HOSTSNDSTC（查询发送方向协议报文统计计数）

## 功能

该命令用于查询发送方向协议报文统计计数。

查询之前需先配置全局协议报文统计配置；当删除全局协议报文统计配置时对应的统计计数将被清零。

当查询类型为RU_STC，不指定RUNAME参数时，查询所有资源单元的统计信息，当指定RUNAME参数时，可以查询指定资源单元的统计信息；不指定PROTTYPE参数时，查询所有协议类型的统计信息，当指定PROTTYPE参数时，可以查询指定协议类型的统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RU_STC：指定资源单元的报文统计信息。<br>- PROT_STC：指定协议类型的报文统计信息。<br>默认值：无 |
| PROTTYPE | 协议类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QUERYTYPE”配置为“RU_STC” 或 “PROT_STC”时为可选参数。<br>参数含义：该参数用于表示协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ARP：ARP协议类型。<br>- ICMP：ICMP协议类型。<br>- OSPF：OSPF协议类型。<br>- SNMP：SNMP协议类型。<br>- UDP_OTHER：其它UDP协议类型。<br>- BGP：BGP协议类型。<br>- LDP：LDP协议类型。<br>- TCP_OTHER：其它TCP协议类型。<br>- ICMPV6：ICMPv6协议类型。<br>- OSPFV3：OSPFv3协议类型。<br>- IPV6UDP_OTHER：其它IPv6 UDP协议类型。<br>- IPV6TCP_OTHER：其它IPv6 TCP协议类型。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QUERYTYPE”配置为“RU_STC”时为可选参数。<br>参数含义：该参数用于表示RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用DSP RU命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HOSTSNDSTC]] · 发送方向协议报文统计计数（HOSTSNDSTC）

## 使用实例

- 查询发送方向指定协议类型的协议报文统计计数：
  ```
  DSP HOSTSNDSTC: QUERYTYPE=PROT_STC, PROTTYPE=TCP_OTHER;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
      协议层次  =  IPv4 TCP
      协议类型  =  其它TCP协议
  发送报文总数  =  366
  (结果个数 = 1)
  ---    END
  ```
- 查询发送方向指定资源单元指定协议类型的协议报文统计计数：
  ```
  DSP HOSTSNDSTC: QUERYTYPE=RU_STC, RUNAME="VNODE_VNRS_VNFC_OMU_0001", PROTTYPE=TCP_OTHER;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
        RU名称  =  VNODE_VNRS_VNFC_OMU_0001
      协议层次  =  IPv4 TCP
      协议类型  =  其它TCP协议
  发送报文总数  =  366
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询发送方向协议报文统计计数（DSP-HOSTSNDSTC）_50281690.md`
