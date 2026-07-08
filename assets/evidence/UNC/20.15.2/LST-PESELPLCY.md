# 查询SGSN/MME选择策略(LST PESELPLCY)

- [命令功能](#ZH-CN_MMLREF_0000001126305774__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305774__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305774__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305774__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305774__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305774__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126305774__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305774)

**适用网元：SGSN、MME**

该命令用于查询SGSN/MME选择策略。

#### [注意事项](#ZH-CN_MMLREF_0000001126305774)

该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305774)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305774)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305774)

无。

#### [使用实例](#ZH-CN_MMLREF_0000001126305774)

查询SGSN/MME选择策略。

**LST PESELPLCY:;**

```
%%LST PESELPLCY:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
对等网元识别模式  =  掩码模式
        比特掩码  =  0x8000
    MME Group ID  =  0x0
MME Group ID范围  =  0x0
  使用RNC ID域名  =  YES
     使用ID TYPE  =  YES
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126305774)

参见 [**SET PESELPLCY**](设置SGSN_MME选择策略（SET PESELPLCY）_72225643.md) 的参数说明。
