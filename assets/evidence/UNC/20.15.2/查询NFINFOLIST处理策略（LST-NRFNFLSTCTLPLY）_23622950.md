# 查询NFINFOLIST处理策略（LST NRFNFLSTCTLPLY）

- [命令功能](#ZH-CN_MMLREF_0000001823622950__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001823622950__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001823622950__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001823622950__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001823622950__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001823622950)

**适用NF：NRF**

该命令用于查询NF携带NFINFOLIST注册、更新、发现策略。

## [注意事项](#ZH-CN_MMLREF_0000001823622950)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001823622950)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001823622950)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示携带NFINFOLIST注册、更新、发现策略对应的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- SMF（SMF）<br>- NWDAF（NWDAF）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001823622950)

运营商需查询NF携带NFINFOLIST后注册、更新、发现策略时，执行如下命令：

```
LST NRFNFLSTCTLPLY:;
            %%LST NRFNFLSTCTLPLY:;%%
            RETCODE = 0  操作成功

            结果如下
            --------
            网元类型  携带NFINFOLIST注册更新处理策略      服务发现优先匹配NFINFO开关  注册更新多NFINFO部分无TAI处理开关

            SMF       不检验NFINFO或NFINFOLIST的携带情况  打开                        打开
            NWDAF     不检验NFINFO或NFINFOLIST的携带情况  关闭                        打开
            (结果个数 = 2)

            ---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001823622950)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 网元类型 | 该参数用于表示携带NFINFOLIST注册、更新、发现策略对应的NF类型。 |
| 携带NFINFOLIST注册更新处理策略 | 该参数用于控制NF携带NFINFOLIST向NRF发起注册、更新请求时，NRF针对NF携带NFINFO和NFINFOLIST的校验策略。若NF携带情况不满足本策略，NRF返回400 Bad Request；满足则校验通过。 |
| 服务发现优先匹配NFINFO开关 | 该参数用于控制服务发现NF时，若匹配到多个NF，是否优先返回NFINFO满足服务发现条件的NF。开关设置为“FUNC_ON”，服务发现NF时，优先匹配NFINFO满足发现条件的NF；开关设置为“FUNC_OFF”时，服务发现NF时，不区分NFINFO或者NFINFOLIST，两个有一个满足发现条件均可以返回。 |
| 注册更新多NFINFO部分无TAI处理开关 | 该参数用于控制NF向NRF发起注册、更新请求，携带NFINFO和NFINFOLIST时，是否允许该NF的多个NFINFO中有部分NFINFO不携带TAI信息。开关设置为“FUNC_ON”，NRF允许部分NFINFO不携带TAI信息，注册更新请求正常返回；开关设置为“FUNC_OFF”时，NRF不允许部分NFINFO不携带Tai信息，注册更新请求返回400 Bad Request。<br>若NF向NRF发起注册，更新请求，仅携带单NFINFO或多NFINFO均无TAI时，NRF对于NF携带TAI参数的控制策略可参考SET NRFTAKEPARARULE命令中的NOTAISW参数。 |
