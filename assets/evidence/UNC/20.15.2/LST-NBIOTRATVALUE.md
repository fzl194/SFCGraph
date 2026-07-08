# 查询NB-IoT终端配置的RAT值（LST NBIOTRATVALUE）

- [命令功能](#ZH-CN_CONCEPT_0209896821__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896821__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896821__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896821__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896821__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896821__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896821)

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询NB-IoT终端接入时UNC给周边网元发送消息时RAT信元中填写的值。

#### [注意事项](#ZH-CN_CONCEPT_0209896821)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896821)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896821)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209896821)

显示NB-IoT终端接入时UNC给周边网元发送消息时RAT值：

```
LST NBIOTRATVALUE:;
```

```

RETCODE = 0  操作成功

NB-IoT用户的RAT值
-----------------
          和OCS交互使用的RAT值  =  EUTRAN-NB-IoT
           和CG交互使用的RAT值  =  EUTRAN-NB-IoT
和AAA计费服务器交互使用的RAT值  =  EUTRAN-NB-IoT
和AAA鉴权服务器交互使用的RAT值  =  EUTRAN-NB-IoT
         和PCRF交互使用的RAT值  =  EUTRAN-NB-IoT
       SGW发送给PGW使用的RAT值  =  EUTRAN-NB-IoT
          和CHF交互使用的RAT值  =  EUTRAN-NB-IoT
          和PCF交互使用的RAT值  =  EUTRAN-NB-IoT
            和UPF交互使的RAT值  =  EUTRAN-NB-IoT
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896821)

参见SET NBIOTRATVALUE的参数说明。
