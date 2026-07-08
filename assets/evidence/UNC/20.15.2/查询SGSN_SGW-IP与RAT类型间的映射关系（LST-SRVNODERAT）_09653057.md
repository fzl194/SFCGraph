# 查询SGSN/SGW IP与RAT类型间的映射关系（LST SRVNODERAT）

- [命令功能](#ZH-CN_MMLREF_0209653057__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653057__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653057__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653057__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653057__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653057)

**适用NF：GGSN**

该命令用来查看指定的SGSN的IP地址段对应的RAT类型。在根据SGSN IP地址映射RAT类型时，需要用到映射表，该命令就是用来查看这张表的配置信息。如果不指定可选参数，该命令将显示所有配置的SGSN地址段的RAT类型的信息。

## [注意事项](#ZH-CN_MMLREF_0209653057)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653057)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653057)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “IP（Service Node IP）”：表示基于SGSN/SGW的IP地址段查询记录。<br>- “RATTYPE（Rat类型）”：表示基于RAT类型查询记录。<br>默认值：无<br>配置原则：无 |
| RATTYPE | RAT类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"RATTYPE"时为条件必选参数。<br>参数含义：该参数用于指定RAT类型。<br>数据来源：全网规划<br>取值范围：<br>- “UTRAN（UTRAN）”：表示无线接入类型为UTRAN。<br>- “GERAN（GERAN）”：表示无线接入类型为GERAN。<br>- “WLAN（WLAN）”：表示无线接入类型为WLAN。<br>- “GAN（GAN）”：表示无线接入类型为GAN。<br>- “EUTRAN（EUTRAN）”：表示无线接入类型为EUTRAN。<br>- “NULL（NULL）”：NULL<br>- “EUTRAN_NB_IOT（EUTRAN_NB_IOT）”：表示无线接入类型为EUTRAN-NB-IoT。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址版本类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"IP"时为条件必选参数。<br>参数含义：该参数用于设置IP地址版本类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPV4）”：表示地址类型为IPv4。<br>- “IPV6（IPV6）”：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| SRVNODEIPV4 | Service Node IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定SGSN/SGW的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制。<br>默认值：无<br>配置原则：<br>取值范围：0.0.0.0~255.255.255.255。 |
| SRVNODEIPV6 | Service Node IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定SGSN/SGW的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209653057)

- 查询所有的rattype类型。可使用如下命令。
  ```
  LST SRVNODERAT:;
  RETCODE = 0  操作成功。

  结果如下
  --------
            IP地址版本类型  =  IPV4
                   RAT类型  =  WLAN
  Service Node的起始IP地址  =  10.1.1.1
  Service Node的结束IP地址  =  10.2.2.2
  (结果个数 = 1)
  ---    END
  ```
- 当运营商需要基于某RAT类型去映射表中查询SGSN的对应的IP地址段时，可按如下配置：
  ```
  LST SRVNODERAT: QUERYTYPE=RATTYPE, RATTYPE=WLAN ;
  RETCODE = 0  操作成功。

  结果如下
  --------
            IP地址版本类型  =  IPV4
                   RAT类型  =  WLAN
  Service Node的起始IP地址  =  10.1.1.1
  Service Node的结束IP地址  =  10.2.2.2
  (结果个数 = 1)
  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0209653057)

| 输出项名称 | 输出项解释 |
| --- | --- |
| RAT类型 | 该参数用于指定RAT类型。 |
| IP地址版本类型 | 该参数用于设置IP地址版本类型。 |
| Service Node的起始IPv4地址 | 该参数用于显示SGSN/SGW的IP地址段的起始IPv4地址。 |
| Service Node的结束IPv4地址 | 该参数用于显示SGSN/SGW的IP地址段的结束IPv4地址。 |
| Service Node的起始IPv6地址 | 该参数用于显示SGSN/SGW的IP地址段的起始IPv6地址。 |
| Service Node的结束IPv6地址 | 该参数用于显示SGSN/SGW的IP地址段的结束IPv6地址。 |
