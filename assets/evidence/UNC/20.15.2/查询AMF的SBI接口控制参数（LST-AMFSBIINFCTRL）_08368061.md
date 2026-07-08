# 查询AMF的SBI接口控制参数（LST AMFSBIINFCTRL）

- [命令功能](#ZH-CN_MMLREF_0000002108368061__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002108368061__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002108368061__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000002108368061__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000002108368061__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000002108368061)

**适用NF：AMF**

该命令用于查询AMF的SBI接口控制参数。

## [注意事项](#ZH-CN_MMLREF_0000002108368061)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000002108368061)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000002108368061)

无

## [使用实例](#ZH-CN_MMLREF_0000002108368061)

查询AMF的SBI接口控制参数，执行如下命令：

```
%%LST AMFSBIINFCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
            Schema自适应开关  =  关闭
ModelD模式UDM Schema填充策略  =  HTTP优先
ModelD模式PCF Schema填充策略  =  HTTP优先
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000002108368061)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Schema自适应开关 | 该参数用于控制AMF是否支持Schema自适应功能。 |
| ModelD模式UDM Schema填充策略 | 该参数用于设置ModelD模式下AMF与UDM网元交互时Schema的填充策略。<br>ModelD模式下，AMF无法感知对端UDM支持的Schema类型，通过本参数可以灵活调整AMF与UDM网元交互时Schema的填充策略。<br>ModelD模式下，建议AMF与对端UDM的Schema策略均设置一致；若AMF与对端UDM的Schema策略配置不一致时，则需要SCP同时配置两种Schema策略，否则会影响后续AMF与UDM通信。 |
| ModelD模式PCF Schema填充策略 | 该参数用于设置ModelD模式下AMF与PCF网元交互时Schema的填充策略。<br>ModelD模式下，AMF无法感知对端PCF支持的Schema类型，通过本参数可以灵活调整AMF与PCF网元交互时Schema的填充策略。<br>ModelD模式下，建议AMF与对端PCF的Schema策略均设置一致；若AMF与对端PCF的Schema策略配置不一致时，则需要SCP同时配置两种Schema策略，否则会影响后续AMF与PCF通信。 |
