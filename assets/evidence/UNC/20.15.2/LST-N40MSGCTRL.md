# 查询N40接口消息的控制参数（LST N40MSGCTRL）

- [命令功能](#ZH-CN_MMLREF_0000001878553376__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001878553376__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001878553376__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001878553376__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001878553376__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001878553376)

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询N40接口消息的控制参数。

## [注意事项](#ZH-CN_MMLREF_0000001878553376)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001878553376)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001878553376)

无

## [使用实例](#ZH-CN_MMLREF_0000001878553376)

查询N40接口消息的控制参数：

```
%%LST N40MSGCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
      国际漫游场景更新流程中仅离线新业务预申请上报CHF开关  =  不使能
                             GERAN/UTRAN接入场景携带UPFID  =  使能
GERAN/UTRAN接入场景携带Presence Reporting Area Infomation  =  使能
       GERAN/UTRAN接入场景携带Network Slicing Information  =  使能
                          GERAN/UTRAN接入场景携带SSC Mode  =  使能
                GERAN/UTRAN接入场景携带DNN Selection Mode  =  使能
            GERAN/UTRAN接入场景携带Session Stop Indicator  =  使能
       GERAN/UTRAN接入场景携带Unit Count Inactivity Timer  =  使能
(结果个数 = 1)
```

## [输出结果说明](#ZH-CN_MMLREF_0000001878553376)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 国际漫游场景更新流程中仅离线新业务预申请上报CHF开关 | 该参数用于控制国际漫游场景下SMF与CHF的更新流程仅离线新业务预申请时是否上报CHF。 |
| GERAN/UTRAN接入场景携带UPFID | 该参数用于控制GERAN/UTRAN接入场景是否携带UPFID。 |
| GERAN/UTRAN接入场景携带Presence Reporting Area Information | 该参数用于控制GERAN/UTRAN接入场景是否携带Presence Reporting Area Information。 |
| GERAN/UTRAN接入场景携带Network Slicing Information | 该参数用于控制GERAN/UTRAN接入场景是否携带Network Slicing Information。 |
| GERAN/UTRAN接入场景携带SSC Mode | 该参数用于控制GERAN/UTRAN接入场景是否携带SSC Mode。 |
| GERAN/UTRAN接入场景携带DNN Selection Mode | 该参数用于控制GERAN/UTRAN接入场景是否携带DNN Selection Mode。 |
| GERAN/UTRAN接入场景携带Session Stop Indicator | 该参数用于控制GERAN/UTRAN接入场景是否携带Session Stop Indicator。 |
| GERAN/UTRAN接入场景携带Unit Count Inactivity Timer | 该参数用于控制GERAN/UTRAN接入场景是否携带Unit Count Inactivity Timer。 |
