# 查询NP安全防攻击CAR规则(LST NPSECPOLICYCAR)

- [命令功能](#ZH-CN_TOPIC_0000001260241155__1.3.1.1)
- [注意事项](#ZH-CN_TOPIC_0000001260241155__1.3.2.1)
- [操作用户权限](#ZH-CN_TOPIC_0000001260241155__1.3.3.1)
- [参数说明](#ZH-CN_TOPIC_0000001260241155__1.3.4.1)
- [使用实例](#ZH-CN_TOPIC_0000001260241155__1.3.5.1)
- [输出结果说明](#ZH-CN_TOPIC_0000001260241155__1.3.6.1)

#### [命令功能](#ZH-CN_TOPIC_0000001260241155)

该命令用来查询IP的安全防攻击CAR规则。

#### [注意事项](#ZH-CN_TOPIC_0000001260241155)

该命令仅适用于NP卡加速模式场景。

#### [操作用户权限](#ZH-CN_TOPIC_0000001260241155)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_TOPIC_0000001260241155)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CARTYPE | 安全协议类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定安全协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- OSPF：OSPF协议。<br>- LDP：LDP协议。<br>- IPV6_OSPF：IPV6_OSPF协议。<br>- IPV6_BGP：IPV6_BGP协议。<br>- IPV6_RA：IPV6_RA协议。<br>- IPV6_NS：IPV6_NS协议。<br>- GRE：GRE协议。<br>- IPV6_NA：IPV6_NA协议。<br>- BGP：BGP协议。<br>- IPV6_TOO_BIG：IPV6_TOO_BIG协议。<br>- Trace：IP Trace协议。<br>- UNKNOWN：未知协议。<br>- IPV6_RS：IPV6_RS协议。<br>- ARP_MISS：ARP_MISS协议。<br>- IPV4_MFIB_MISS：IPV4_MFIB_MISS协议。<br>- IPV6_ICMP：IPV6_ICMP协议。<br>- IGMP：IGMP协议。<br>- BFD_Trace：BFD_Trace协议。<br>- ARP：ARP协议。<br>- IPV6_DHCP：IPV6_DHCP协议。<br>- PIM：PIM协议。<br>- BFD：BFD协议。<br>- ICMP：ICMP协议。<br>- DHCP：DHCP协议。<br>- TOTAL_CAR：TOTAL_CAR。<br>默认值：无 |

#### [使用实例](#ZH-CN_TOPIC_0000001260241155)

- 查询ARP协议的安全防攻击CAR规则：
  ```
  LST NPSECPOLICYCAR: CARTYPE=ARP;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  --------
           安全协议类型  =  ARP 
   承诺信息速率（kbps）  =  512 
  承诺突发尺寸（bytes）  =  60000 
   峰值信息速率（kbps）  =  0 
  峰值突发尺寸（bytes）  =  0 
  (结果个数 = 1)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_TOPIC_0000001260241155)

参见 **[SET NPSECPOLICYCAR](设置NP安全防攻击CAR规则(SET NPSECPOLICYCAR)_15401278.md)** 的参数说明。
