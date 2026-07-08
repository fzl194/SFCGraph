# 查询激活抑制规则（LST SMARTACT）

- [命令功能](#ZH-CN_MMLREF_0000001126145744__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145744__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145744__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145744__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145744__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145744__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126145744__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145744)

**适用网元：SGSN**

此命令用于查询基于用户终端类型的激活抑制规则。用户激活异常时，按照配置的激活抑制规则对其进行抑制。

#### [注意事项](#ZH-CN_MMLREF_0000001126145744)

此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145744)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145744)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145744)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UETYPE | 终端类型 | 可选必选说明：可选参数<br>参数含义：待查询的终端类型。<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>- “UNKNOWN_TYPE(未知类型)”<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145744)

查询所有激活抑制规则：

LST SMARTACT:;

```
%%LST SMARTACT:;%%
RETCODE = 0  操作成功。

查询结果如下
------------
终端类型       特定原因值拒绝激活功能开关    Backoff Timer分配开关    Back off timer最小值（秒）    Back off timer最大值（秒）    Parking APN假激活功能开关    主动分离用户功能开关    激活拒绝原因值                                分离原因值                 

Black Berry    关闭                          开启                     660                           3000                          关闭                         关闭                    Requested service option not subscribed 33    GPRS services not allowed 7
iOS            关闭                          开启                     660                           3000                          开启                         开启                    Requested service option not subscribed 33    PLMN not allowed 11        
(结果个数 = 2)
---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126145744)

参见 [**ADD SMARTACT**](增加激活抑制规则（ADD SMARTACT）_72225421.md) 的参数说明。
