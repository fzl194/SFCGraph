# 查询DNS IP地址资源列表（LST DNSIPRESOURCE）

- [命令功能](#ZH-CN_CONCEPT_0000206961928568__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206961928568__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206961928568__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206961928568__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206961928568__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000206961928568__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206961928568)

**适用NF：CloudEPSN**

该命令用于查询DNS的管理接口和业务接口IP地址资源信息。

#### [注意事项](#ZH-CN_CONCEPT_0000206961928568)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206961928568)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206961928568)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000206961928568)

查询IP地址资源信息：

```
+++    CloudEPSN/*MEID:0 MENAME:APP-VNF-CloudEPSN-X86-B003_IP60*/        2024-02-20 13:05:02
O&M    #3699
%%LST DNSIPRESOURCE:;
```

```
%%
RETCODE = 0  操作成功

结果如下
--------
接口类型  IP地址类型  IPv4地址列表             IPv6地址列表             

Dns       IPv4        192.168.0.1,192.168.0.2  NULL  
Mgt       IPv4和IPv6  NULL                     NULL                     
(结果个数 = 2)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000206961928568)

参见SET DNSIPRESOURCE的参数说明。
