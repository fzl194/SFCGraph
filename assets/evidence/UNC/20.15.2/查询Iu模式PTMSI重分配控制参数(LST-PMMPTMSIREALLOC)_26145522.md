# 查询Iu模式PTMSI重分配控制参数(LST PMMPTMSIREALLOC)

- [命令功能](#ZH-CN_MMLREF_0000001126145522__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145522__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145522__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145522__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145522__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145522__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126145522__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145522)

**适用网元：SGSN**

此命令用于查询Iu模式PTMSI重分配控制参数。

#### [注意事项](#ZH-CN_MMLREF_0000001126145522)

该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145522)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145522)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145522)

无。

#### [使用实例](#ZH-CN_MMLREF_0000001126145522)

查询Iu模式PTMSI重分配控制参数所有信息：

LST PMMPTMSIREALLOC:;

```
%%LST PMMPTMSIREALLOC:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                 伴随RAU流程分配  =  否
P-TMSI重分配流程间隔时长（小时）  =  1
        P-TMSI重分配流程发起条件  =  PTMSI分配后
(结果个数 = 1)

---    END 
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126145522)

参见 [**SET PMMPTMSIREALLOC**](设置Iu模式PTMSI重分配控制参数(SET PMMPTMSIREALLOC)_72345119.md) 的参数说明。
