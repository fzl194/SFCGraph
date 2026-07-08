---
id: UNC@20.15.2@MMLCommand@LST SRVNODERAT
type: MMLCommand
name: LST SRVNODERAT（查询SGSN/SGW IP与RAT类型间的映射关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SRVNODERAT
command_category: 查询类
applicable_nf:
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 获取RAT管理
- IP地址映射RAT
status: active
---

# LST SRVNODERAT（查询SGSN/SGW IP与RAT类型间的映射关系）

## 功能

**适用NF：GGSN**

该命令用来查看指定的SGSN的IP地址段对应的RAT类型。在根据SGSN IP地址映射RAT类型时，需要用到映射表，该命令就是用来查看这张表的配置信息。如果不指定可选参数，该命令将显示所有配置的SGSN地址段的RAT类型的信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “IP（Service Node IP）”：表示基于SGSN/SGW的IP地址段查询记录。<br>- “RATTYPE（Rat类型）”：表示基于RAT类型查询记录。<br>默认值：无<br>配置原则：无 |
| RATTYPE | RAT类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"RATTYPE"时为条件必选参数。<br>参数含义：该参数用于指定RAT类型。<br>数据来源：全网规划<br>取值范围：<br>- “UTRAN（UTRAN）”：表示无线接入类型为UTRAN。<br>- “GERAN（GERAN）”：表示无线接入类型为GERAN。<br>- “WLAN（WLAN）”：表示无线接入类型为WLAN。<br>- “GAN（GAN）”：表示无线接入类型为GAN。<br>- “EUTRAN（EUTRAN）”：表示无线接入类型为EUTRAN。<br>- “NULL（NULL）”：NULL<br>- “EUTRAN_NB_IOT（EUTRAN_NB_IOT）”：表示无线接入类型为EUTRAN-NB-IoT。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址版本类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"IP"时为条件必选参数。<br>参数含义：该参数用于设置IP地址版本类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPV4）”：表示地址类型为IPv4。<br>- “IPV6（IPV6）”：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| SRVNODEIPV4 | Service Node IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定SGSN/SGW的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制。<br>默认值：无<br>配置原则：<br>取值范围：0.0.0.0~255.255.255.255。 |
| SRVNODEIPV6 | Service Node IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定SGSN/SGW的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVNODERAT]] · SGSN/SGW IP与RAT类型间的映射关系（SRVNODERAT）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SRVNODERAT.md`
