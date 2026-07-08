# 测试GTP-C路径(TST GTPCPATH)

- [命令功能](#ZH-CN_MMLREF_0000001126145912__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145912__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145912__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145912__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145912__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145912__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145912)

**适用网元：SGSN、MME**

该命令用于通过发送GTP Echo request消息的方法测试本局与对端GSN之间的GTP-C路径是否正常。

#### [注意事项](#ZH-CN_MMLREF_0000001126145912)

- 该命令执行后立即生效。
- 该命令只用于UPP进程。
- 该命令探测过程中临时会产生一条维护路径，探测结束后删除该维护路径。该命令探测只探测路径是否通断，与该路径上是否存在信令消息无关。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145912)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145912)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145912)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPVER | GTP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的协议版本。<br>数据来源：整网规划<br>取值范围：<br>- “GTPv0(GTPv0)”<br>- “GTPv1(GTPv1)”<br>- “GTPv2(GTPv2)”<br>默认值：无<br>说明：输入参数时，先选择<br>“GTP版本”<br>，先指明GTP-C路径的协议版本是<br>“GTPv0(GTPv0)”<br>，<br>“GTPv1(GTPv1)”<br>还是<br>“GTPv2(GTPv2)”<br>，其次选择对端的<br>“IP类型”<br>，再输入IP地址。 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端GSN的IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| LOCIPV4ADDR | 本端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本端GSN IPV4地址。<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV4(IPV4)”<br>时此参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端GSN IPV4地址。<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV4(IPV4)”<br>时此参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| LOCIPV6ADDR | 本端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本端GSN IPV6地址。<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV6(IPV6)”<br>时此参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| PEERIPV6ADDR | 对端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端GSN IPV6地址。<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV6(IPV6)”<br>时此参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145912)

测试GTP-C Path，路径版本GTPv1版本，本端IP地址为192.168.14.20，对端IP地址为192.168.9.20：

TST GTPCPATH: GTPVER=GTPv1, IPTYPE=IPV4, LOCIPV4ADDR="192.168.14.20", PEERIPV4ADDR="192.168.9.20";

```
%%TST GTPCPATH: GTPVER=GTPv1, IPTYPE=IPV4, LOCIPV4ADDR="192.168.14.20", PEERIPV4ADDR="192.168.9.20";%%
RETCODE = 0  操作成功。

输出结果如下
-----------
本端IPv4地址  =  192.168.14.20
对端IPv4地址  =  192.168.9.20
     GTP版本  =  GTPv1
(结果个数 = 1)

---    END
```
