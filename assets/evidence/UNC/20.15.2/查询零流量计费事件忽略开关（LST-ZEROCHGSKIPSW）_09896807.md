# 查询零流量计费事件忽略开关（LST ZEROCHGSKIPSW）

- [命令功能](#ZH-CN_CONCEPT_0209896807__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896807__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896807__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896807__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896807__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896807__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896807)

**适用NF：GGSN、SGW-C、PGW-C、SMF**

该命令用于显示零流量计费事件忽略开关。

#### [注意事项](#ZH-CN_CONCEPT_0209896807)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896807)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896807)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209896807)

要显示零流量计费事件忽略开关：

```
LST ZEROCHGSKIPSW:;
```

```

RETCODE = 0  操作成功。

零流量计费事件忽略配置
----------------
                       零流量计费事件忽略总开关  =  ENABLE
                                    忽略RAT更新  =  DISABLE
                       忽略Serving Node地址改变  =  DISABLE
                                 忽略MS时区改变  =  DISABLE
                  忽略Serving Node PLMN标识改变  =  DISABLE
                                   忽略时间阈值  =  DISABLE
                                       忽略CCFH  =  DISABLE
                                 忽略去激活话单  =  ENABLE
        忽略PS-Furnish-Charging-Information改变  =  DISABLE
                               忽略强制生成话单  =  ENABLE
                   忽略基于位置的计费订阅和取消  =  DISABLE
                                    忽略QoS改变  =  DISABLE
                                    忽略ULI改变  =  DISABLE
                                   忽略费率切换  =  DISABLE
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896807)

参见SET ZEROCHGSKIPSW的参数说明。
