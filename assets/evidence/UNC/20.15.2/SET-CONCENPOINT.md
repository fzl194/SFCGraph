# 设置集中点部署模式（SET CONCENPOINT）

- [命令功能](#ZH-CN_CONCEPT_0209896704__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896704__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896704__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896704__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896704__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896704)

**适用NF：PGW-C、SMF**

![](设置集中点部署模式（SET CONCENPOINT）_09896704.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改集中点模式可能导致Diameter链路重建或中断，进而影响用户使用业务，比如用户被去活等。涉及Diameter链路的接口为Gx、Gy、S6b接口。

此命令用于设置信令集中点的部署模式。

#### [注意事项](#ZH-CN_CONCEPT_0209896704)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- LOCALIP_PEER模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数未配置或配置为0的链路生效。LocalPort参数配置为非0的链路，允许配置下发，但是不会建链。
- LOCALPORT模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数配置为非0的链路生效。LocalPort参数未配置或配置为0的链路，允许配置下发，但是不会建链。
- 如果Gx/Gy/S6b集中点模式在LOCALIP_PEER和LOCALPORT之间切换，需要使用命令RMV SCTPASSOC删除原模式下的SCTP耦联测量对象并重新配置。
- 当前版本不支持GAPORTPERPROC参数，不允许将该参数配置超过1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | GACONCENMODE | GXCONCENMODE | GYCONCENMODE | S6BCONCENMODE | GAPORTPERPROC |
| --- | --- | --- | --- | --- | --- |
| 初始值 | SINGLE_CONNECT | LOCALIP_PEER | LOCALIP_PEER | LOCALIP_PEER | 1 |

#### [操作用户权限](#ZH-CN_CONCEPT_0209896704)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896704)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GACONCENMODE | Ga集中点模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Ga集中点的部署模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MULTI_PORT：表示使用group级接口，和对端建立多条连接，多条连接使用组级IP作为源IP，源端口号不同。<br>- SINGLE_CONNECT：表示使用group级接口，一个对端应用服务器和一个逻辑端口只有一条链路。<br>默认值：无<br>配置原则：无 |
| GXCONCENMODE | Gx集中点模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Gx应用的集中点部署模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOCALIP_PEER：按照本端源IP加对端主机名绑定Diameter应用的集中点。<br>- LOCALPORT：按照本端端口绑定Diameter集中点。<br>默认值：无<br>配置原则：无 |
| GYCONCENMODE | Gy集中点模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Gy集中点的部署模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOCALIP_PEER：按照本端源IP加对端主机名绑定Diameter应用的集中点。<br>- LOCALPORT：按照本端端口绑定Diameter集中点。<br>默认值：无<br>配置原则：无 |
| S6BCONCENMODE | S6b集中点模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S6b集中点的部署模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOCALIP_PEER：按照本端源IP加对端主机名绑定Diameter应用的集中点。<br>- LOCALPORT：按照本端端口绑定Diameter集中点。<br>默认值：无<br>配置原则：无 |
| GAPORTPERPROC | Ga每进程端口数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GACONCENMODE”配置为“MULTI_PORT”时为可选参数。<br>参数含义：该参数用于指定Ga集中点模式为MULTI_PORT时为每个Ga进程提供的端口数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~5。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896704)

根据网络规划，需要修改Ga集中点的部署模式为SINGLE_CONNECT，则可以按如下配置：

```
SET CONCENPOINT: GACONCENMODE=SINGLE_CONNECT;
```
