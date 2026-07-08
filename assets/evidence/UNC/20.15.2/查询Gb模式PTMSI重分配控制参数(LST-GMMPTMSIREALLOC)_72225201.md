# 查询Gb模式PTMSI重分配控制参数(LST GMMPTMSIREALLOC)

- [命令功能](#ZH-CN_MMLREF_0000001172225201__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225201__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225201__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225201__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225201__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225201__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172225201__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225201)

**适用网元：SGSN**

此命令用于查询Gb模式PTMSI重分配控制参数。

#### [注意事项](#ZH-CN_MMLREF_0000001172225201)

此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225201)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225201)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225201)

无。

#### [使用实例](#ZH-CN_MMLREF_0000001172225201)

查询Gb模式PTMSI重分配控制参数所有信息：

LST GMMPTMSIREALLOC:;

```
%%LST GMMPTMSIREALLOC:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                 伴随RAU流程分配  =  是
P-TMSI重分配流程间隔时长（小时）  =  0
        P-TMSI重分配流程发起条件  =  处于Ready状态
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172225201)

参见 [**SET GMMPTMSIREALLOC**](设置Gb模式PTMSI重分配控制参数（SET GMMPTMSIREALLOC）_26145520.md) 的参数说明。
