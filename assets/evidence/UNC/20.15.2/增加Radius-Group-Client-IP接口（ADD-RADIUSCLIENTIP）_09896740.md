# 增加Radius Group Client IP接口（ADD RADIUSCLIENTIP）

- [命令功能](#ZH-CN_CONCEPT_0209896740__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896740__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896740__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896740__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896740__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896740)

**适用NF：PGW-C、SMF**

ADD RADIUSCLIENTIP命令用来增加Radius Group Client IP接口，输入值为RdsSvrGrpName、AuthOrAcct和IntfName。

#### [注意事项](#ZH-CN_CONCEPT_0209896740)

- 该命令执行后立即生效。
- 该命令最大记录数为2000。
- RADIUS server仅选择相同IP版本的逻辑接口通信。
- RADIUS group内同时配置IPv4和IPv6 RADIUS server时，Client IP对应的逻辑接口也需要同时配置IPv4和IPv6地址。
- 对象RadiusClientIp中的RdsSvrGrpName对应的IntfName和AuthOrAcct的组合记录数不大于6，并且不能有相同记录，则添加成功。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896740)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896740)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | Radius Server Group名称 | 可选必选说明：必选参数<br>参数含义：指定Radius Server Group名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD RDSSVRGRP命令配置生成。<br>- 需要先使用ADD RDSSVRGRP命令配置RADIUS服务器组信息。 |
| AUTHORACCT | 鉴权或计费 | 可选必选说明：可选参数<br>参数含义：指定鉴权或计费。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ACCOUNTING：表示指定的Gi接口的IP地址是计费时的radius client ip。<br>- AUTHENTICATION：表示指定的Gi接口的IP地址是鉴权时的radius client ip。<br>- ACCT_AND_AUTH：表示指定的Gi接口的IP地址既是鉴权时的radius client ip，也是计费时的radius client ip。<br>默认值：ACCT_AND_AUTH<br>配置原则：<br>- ACCOUNTING：表示计费。<br>- AUTHENTICATION：表示鉴权。<br>- ACCT_AND_AUTH：表示计费和鉴权。 |
| INTFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～13。用户输入形式例如：giif1/0/0。其中giif为逻辑接口类型；1/0/0中第一个数字为组号，第二个数字为实例类型；第三个数字为逻辑接口号，各逻辑接口类型有各自的配置范围。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896740)

如果想要增加Radius Group Client IP接口，可以配置RADIUS服务器组名为"aaa"，指定为计费，接口名称为"giif1/0/0"，例如：

```
ADD RADIUSCLIENTIP: RDSSVRGRPNAME="aaa",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/0";
```
