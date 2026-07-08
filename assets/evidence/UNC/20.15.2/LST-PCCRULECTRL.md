# 查询PCC规则相关控制（LST PCCRULECTRL）

- [命令功能](#ZH-CN_MMLREF_0209652541__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652541__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652541__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652541__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209652541__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209652541)

**适用NF：SMF**

该命令用于查询PCC规则相关控制参数。

## [注意事项](#ZH-CN_MMLREF_0209652541)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209652541)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652541)

无

## [使用实例](#ZH-CN_MMLREF_0209652541)

查询PCC规则相关控制参数。

```
LST PCCRULECTRL:;
```

## [输出结果说明](#ZH-CN_MMLREF_0209652541)

| 输出项名称 | 输出项解释 |
| --- | --- |
| QoS Rule设置原则 | QOSRULEPRIO_SWITCH的值设置为INTERNAL_ALLOCATION，QosRule的优先级内部分配。QOSRULEPRIO_SWITCH的值设置为INHERIT_PCCRULE_PRECEDENCE，QosRule的优先级继承PCF下发PccRule优先级，并且SMF会限制PCF下发PccRule优先级范围是0~255。 |
