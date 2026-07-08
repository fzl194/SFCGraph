# 查询外置规则库OTT flow filter信息（LST OTTFLOWFILTERNAME）

- [命令功能](#ZH-CN_CONCEPT_0000201293531883__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201293531883__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201293531883__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201293531883__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201293531883__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000201293531883__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201293531883)

**适用NF：PGW-U、UPF**

该命令用来显示通过命令行LOD EXTERNALDB加载的外置OTT数据库中定义的Flow Filter的名称。

#### [注意事项](#ZH-CN_CONCEPT_0000201293531883)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201293531883)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201293531883)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000201293531883)

运营商查询本地配置的外置流过滤器实例信息：

```
LST OTTFLOWFILTERNAME:;
```

```

RETCODE = 0 操作成功.

外置OTT flow-filter信息：
------------------------
OTTFlowFilterName
f_im
f_voip

(结果个数 = 2)
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000201293531883)

| 输出项名称 | 输出项解释 |
| --- | --- |
| flow-filter名称 | 该参数用于输出流过滤器实例名称。 |
