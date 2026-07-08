# 停止批量路径探测（STP PATHSTST）

- [命令功能](#ZH-CN_CONCEPT_0186527025__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186527025__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186527025__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186527025__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186527025__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0186527025)

**适用NF：SGW-U、PGW-U、UPF**

该命令用来停止UPF与UPF之间、UPF与gNodeB之间、SGW-U与eNodeB之间、SGW-U与RNC之间、PGW-U与RNC之间、UPF与SMF之间、PGW-U与SGW-U之间数据面路径的批量探测。

#### [注意事项](#ZH-CN_CONCEPT_0186527025)

- 该命令执行后立即生效。
- 批量探测信号发送次数有默认值，如果不停止发送，则发送完毕默认次数后，自动停止发送。

#### [操作用户权限](#ZH-CN_CONCEPT_0186527025)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186527025)

无。

#### [使用实例](#ZH-CN_CONCEPT_0186527025)

停止本次探测：

```
STP PATHSTST:;
```
