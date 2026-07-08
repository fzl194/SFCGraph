# 查询OSPF LSDB的状态信息（DSP OSPFLSDBSTATEINFO）

- [命令功能](#ZH-CN_CONCEPT_0000001550120670__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550120670__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550120670__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550120670__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550120670__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001550120670__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550120670)

该命令用于显示OSPF LSDB的状态信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001550120670)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550120670)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550120670)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| LSATYPE | LSA类型 | 可选必选说明：可选参数<br>参数含义：LSA类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Router：Router LSA。<br>- Network：Network LSA。<br>- Sum_Net：ABR Summary LSA。<br>- Sum_Asbr：ASBR Summary LSA。<br>- External：AS-External LSA。<br>- NSSA：NSSA LSA。<br>- Opq_Link：Opaque Link LSA。<br>- Opq_Area：Opaque Area LSA。<br>- Opq_As：Opaque AS LSA。<br>默认值：无 |
| LINKSTATEID | LSA报头中的链路状态ID | 可选必选说明：可选参数<br>参数含义：LSA报头中的链路状态ID。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001550120670)

显示OSPF进程1下LSDB的状态信息：

```
DSP OSPFLSDBSTATEINFO:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
               OSPF进程号  =  1
                   区域号  =  0.0.0.0
               路由器标识  =  192.168.3.111
                  LSA类型  =  Router LSA
    LSA报头中的链路状态ID  =  192.168.3.111
发布或产生LSA的路由器标识  =  192.168.3.111
            LSA的老化时间  =  74
                  LSA长度  =  36
                  LSA选项  =  E
                LSA序列号  =  0x80000001
                LSA校验和  =  0xa08c
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001550120670)

| 输出项名称 | 输出项解释 |
| --- | --- |
| OSPF进程号 | 该参数用于表示OSPF进程号。 |
| 区域号 | 该参数用于表示OSPF区域号，当LSA类型为ASE时，AreaID填成0.0.0.0，实际不生效。 |
| 路由器标识 | 该参数用于表示OSPF路由器标识。 |
| LSA类型 | 该参数用于表示LSA类型。 |
| LSA报头中的链路状态ID | 该参数用于表示LSA报头中的链路状态ID，与LSA类型一起描述路由域中唯一一个LSA。 |
| 发布或产生LSA的路由器标识 | 该参数用于表示发布或产生LSA的路由器标识，当配置了共网段接口时，一些LSA的发布路由器标识为共网段接口的虚router-id，建议共网段端设备上，手动配置OSPF进程的实router-id且与接口IP地址不同的，虚router-id优先借用接口IP地址，不会与实router-id冲突。 |
| LSA的老化时间 | 该参数用于表示LSA的老化时间。 |
| LSA长度 | 该参数用于表示LSA的长度。 |
| LSA选项 | 该参数用于表示LSA选项。 |
| LSA序列号 | 该参数用于表示LSA序列号，其他路由器根据这个值可以判断哪个LSA是最新的。 |
| LSA校验和 | 该参数用于表示LSA校验和，除了LSA的老化时间外其它各域的校验和。 |
