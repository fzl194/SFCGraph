# 查询LDP BFD配置（LST LDPBFD）

- [命令功能](#ZH-CN_CONCEPT_0000001550281682__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550281682__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550281682__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550281682__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550281682__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001550281682__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550281682)

该命令用于查询LDP BFD配置。

#### [注意事项](#ZH-CN_CONCEPT_0000001550281682)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550281682)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550281682)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000001550281682)

查询LDP BFD配置：

```
LST LDPBFD:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                                  LDP BFD能力  =  TRUE
                   BFD For LDP Tunnel触发策略  =  主机
               BFD For LDP Tunnel的IP前缀名称  =  NULL
               BFD For LDP Tunnel FEC列表名称  =  NULL
BFD For LDP Tunnel的BFD最小发送时间间隔（ms）  =  45
BFD For LDP Tunnel的BFD最小接收时间间隔（ms）  =  45
        BFD For LDP Tunnel的BFD可容忍丢失次数  =  40
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001550281682)

参见SET LDPBFD的参数说明。
