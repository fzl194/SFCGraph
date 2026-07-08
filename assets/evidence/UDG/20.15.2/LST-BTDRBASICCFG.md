# 查询BTDR单据上报参数（LST BTDRBASICCFG）

- [命令功能](#ZH-CN_CONCEPT_0000203719881190__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203719881190__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203719881190__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203719881190__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203719881190__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000203719881190__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203719881190)

**适用NF：PGW-U、UPF**

该命令用于查询BTDR单据上报参数。

#### [注意事项](#ZH-CN_CONCEPT_0000203719881190)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203719881190)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203719881190)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000203719881190)

查询BTDR单据上报参数：

```
%%LST BTDRBASICCFG:;
```

```
%%
RETCODE = 0  Operation succeeded

Parameters for reporting BTDRs
------------------------------
                         Reporting Switch  =  ENABLE
                     Reporting Period (s)  =  50
UDP Packet Payload Maximum Length (bytes)  =  520
       Cache Duration of Sent Packets (s)  =  30
                  Pseudonymization Switch  =  ENABLE
                    Pseudonymization Mode  =  PRE_DEFINED
               Pseudonymization Algorithm  =  HMACSHA256
(Number of results = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000203719881190)

参见SET BTDRBASICCFG的参数说明。
