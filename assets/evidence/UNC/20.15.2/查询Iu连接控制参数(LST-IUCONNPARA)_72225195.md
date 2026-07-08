# 查询Iu连接控制参数(LST IUCONNPARA)

- [命令功能](#ZH-CN_MMLREF_0000001172225195__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225195__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225195__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225195__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225195__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225195__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172225195__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225195)

**适用网元：SGSN**

该命令用于查询Iu连接控制参数。

#### [注意事项](#ZH-CN_MMLREF_0000001172225195)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225195)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225195)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225195)

无。

#### [使用实例](#ZH-CN_MMLREF_0000001172225195)

查询IUCONNPARA参数：

LST IUCONNPARA:;

```
%%LST IUCONNPARA:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------
   Follow on without PDP场景Iu连接管理 (s)  =  10
      Follow on with PDP场景Iu连接管理 (s)  =  10
No follow on without PDP场景Iu连接管理 (s)  =  0
   No follow on with PDP场景Iu连接管理 (s)  =  0
                      SMS流程Iu连接管理(s)  =  65535
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172225195)

参见 [**SET IUCONNPARA**](设置Iu连接控制参数(SET IUCONNPARA)_26145514.md) 的参数说明。
