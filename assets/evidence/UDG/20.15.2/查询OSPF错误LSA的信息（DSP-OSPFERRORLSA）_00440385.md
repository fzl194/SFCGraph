# 查询OSPF错误LSA的信息（DSP OSPFERRORLSA）

- [命令功能](#ZH-CN_CONCEPT_0000001600440385__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600440385__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600440385__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600440385__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600440385__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600440385__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600440385)

该命令用于查询OSPF错误LSA的信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600440385)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600440385)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600440385)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示OSPF进程号，未指定OSPF进程号时默认查询所有OSPF进程。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600440385)

查询OSPF错误LSA的信息：

```
DSP OSPFERRORLSA:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
        OSPF进程号  =  1
        路由器标识  =  192.168.1.1
LSA的失效时长（s）  =  1
       LSA的选项域  =  2
         LSA的类型  =  Router-LSA
       LSA的状态ID  =  192.168.2.50
        发布路由器  =  192.168.2.50
         LSA的序号  =  0x80000041
       LSA的校验值  =  0xc4f5
         LSA的长度  =  36
 接收LSA的接口名称  =  Ethernet66/0/7
     接收LSA的时间  =  2017-10-24 12:01:51
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600440385)

| 输出项名称 | 输出项解释 |
| --- | --- |
| OSPF进程号 | 用于表示OSPF进程号，未指定OSPF进程号时默认查询所有OSPF进程。 |
| 路由器标识 | 用于表示路由器标识。 |
| LSA的失效时长（s） | 用于表示LSA的失效时长（s）。 |
| LSA的选项域 | 用于表示LSA的选项域。 |
| LSA的类型 | 该参数用于表示LSA的类型，包括：<br>- Router。<br>- Network。<br>- Sum-Net。<br>- Sum-Asbr。<br>- External。<br>- NSSA。<br>- Opq-Link。<br>- Opq-Area。<br>- Opq-As。<br>- Unknown-LSA。<br>- Router-LSA。<br>- Network-LSA。<br>- Inter-Area-Prefix-LSA。<br>- Inter-Area-Router-LSA。<br>- AS-External-LSA。<br>- NSSA-external-LSA。<br>- Grace LSA。<br>- Link-LSA。<br>- Intra-Area-Prefix-LSA。<br>- Link-RI-LSA。<br>- Area-RI-LSA。<br>- AS-RI-LSA。 |
| LSA的状态ID | 用于表示LSA的状态ID。 |
| 发布路由器 | 用于表示发布LSA的路由器。 |
| LSA的序号 | 用于表示LSA的序号，其他路由器根据这个值可以判断哪个LSA是最新的。 |
| LSA的校验值 | 用于表示LSA的校验值。 |
| LSA的长度 | 用于表示LSA的长度。 |
| 接收LSA的接口名称 | 用于表示接收LSA的接口名称。 |
| 接收LSA的时间 | 用于表示接收LSA的时间。 |
