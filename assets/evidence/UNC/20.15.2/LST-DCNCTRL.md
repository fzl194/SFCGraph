# 查询DCN控制参数(LST DCNCTRL)

- [命令功能](#ZH-CN_MMLREF_0000001172345425__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345425__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345425__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345425__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345425__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345425__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172345425__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345425)

**适用网元：MME**

此命令用于查询当前专用核心网重选处理方式。

#### [注意事项](#ZH-CN_MMLREF_0000001172345425)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345425)

manage-ug；system-ug；monitor-ug；visit-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345425)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；G_4，来宾级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345425)

无。

#### [使用实例](#ZH-CN_MMLREF_0000001172345425)

查询当前配置的DCN控制参数：

LST DCNCTRL:;

```
%%LST DCNCTRL:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
                  重选策略  =  立即
         携带UE Usage Type  =  否
     UE USAGE TYPE携带策略  =  正在使用的UE USAGE TYPE
                 非广播TAI  =  0000000000
             MMEGI查询策略  =  使用本地配置查询MMEGI
              域名回退查询  =  NULL
     Backoff Timer分配开关  =  关闭
Back off timer最小值（秒）  =  300
Back off timer最大值（秒）  =  1800
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172345425)

参见 [SET DCNCTRL](设置DCN控制参数(SET DCNCTRL)_26305634.md) 的参数说明。
