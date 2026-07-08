# 查询TCP全局配置（LST TCPGLOBALCFG）

- [命令功能](#ZH-CN_CONCEPT_0000001600601361__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600601361__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600601361__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600601361__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600601361__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600601361__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600601361)

该命令用于查询TCP全局配置。

#### [注意事项](#ZH-CN_CONCEPT_0000001600601361)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600601361)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600601361)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000001600601361)

查询TCP全局配置：

```
LST TCPGLOBALCFG:;
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
        TCP FIN-Wait超时时间（s）  =  675
        TCP SYN-Wait超时时间（s）  =  75
                  TCP窗口值（KB）  =  8
                     PMTU功能开关  =  打开
              PMTU老化时间（min）  =  100
   IPv6 TCP FIN-Wait超时时间（s）  =  675
   IPv6 TCP SYN-Wait超时时间（s）  =  75
             IPv6 TCP窗口值（KB）  =  8
                最大MSS值（byte）  =  65535
            IPv6最大MSS值（byte）  =  65535
        (结果个数 = 1)
        ---   END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600601361)

参见SET TCPGLOBALCFG的参数说明。
