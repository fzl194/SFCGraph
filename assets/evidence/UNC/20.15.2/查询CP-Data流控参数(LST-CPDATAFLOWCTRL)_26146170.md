# 查询CP Data流控参数(LST CPDATAFLOWCTRL)

- [命令功能](#ZH-CN_CONCEPT_0000001126146170__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001126146170__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001126146170__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001126146170__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001126146170__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001126146170__1.3.6.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001126146170__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001126146170)

**适用网元：MME**

此命令用于查询当前配置的CP Data流控参数。

#### [注意事项](#ZH-CN_CONCEPT_0000001126146170)

无。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001126146170)

manage-ug；system-ug；monitor-ug。

#### [网管用户权限](#ZH-CN_CONCEPT_0000001126146170)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组。

#### [参数说明](#ZH-CN_CONCEPT_0000001126146170)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000001126146170)

查询CP Data流控参数：

LST CPDATAFLOWCTRL:;

```
%%LST CPDATAFLOWCTRL:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------

CP Data CPU 过载流控功能开关 = 打开
           T3448最小值（秒） = 500
           T3448最大值（秒） = 800
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001126146170)

参见 [**SET CPDATAFLOWCTRL**](设置CP Data流控参数(SET CPDATAFLOWCTRL)_72345769.md) 的参数说明。
