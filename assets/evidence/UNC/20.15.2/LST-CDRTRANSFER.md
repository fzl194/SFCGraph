# 查询话单发送控制参数（LST CDRTRANSFER）

- [命令功能](#ZH-CN_CONCEPT_0209896851__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896851__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896851__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896851__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896851__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896851__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896851)

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询话单发送控制参数。

#### [注意事项](#ZH-CN_CONCEPT_0209896851)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896851)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896851)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209896851)

查询话单发送控制参数：

```
LST CDRTRANSFER:;
```

```

RETCODE = 0  操作成功

话单发送控制参数
----------------
                GTP'消息最大可携带的话单字节数  =  2000
 Echo and Data Record Transfer Request重传次数  =  3
Data Record Transfer Request重传时间间隔（秒）  =  3
              Node Alive消息重传时间间隔（秒）  =  10
                                    CG选择模式  =  基于消息的负载均衡
                          GTP'报文CheckSum开关  =  允许
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896851)

参见SET CDRTRANSFER的参数说明。
