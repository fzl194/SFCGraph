# 查询PCC QoS相关控制参数（LST PCCRULECTRL）

- [命令功能](#ZH-CN_CONCEPT_0208342474__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0208342474__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0208342474__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0208342474__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0208342474__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0208342474__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0208342474)

**适用NF：PGW-U、UPF**

此命令用于显示PCC动态Rule生成的QoS Rule优先级是否按照PCF下发的优先级进行控制。

#### [注意事项](#ZH-CN_CONCEPT_0208342474)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0208342474)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0208342474)

无。

#### [使用实例](#ZH-CN_CONCEPT_0208342474)

当运营商需要查询QosRulePrio参数当前的值时，需要执行：

```
LST PCCRULECTRL:;
```

```

RETCODE = 0 操作成功。

PCC QoS相关控制参数
------------------------
QoS Rule优先级设置原则 = 等于PCC Rule优先级
(结果个数 = 1)
--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0208342474)

参见SET PCCRULECTRL的参数说明。
