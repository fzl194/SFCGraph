# 查询EIR配置(LST EIR)

- [命令功能](#ZH-CN_MMLREF_0000001126305264__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305264__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305264__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305264__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305264__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305264__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126305264__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305264)

**适用网元：MME**

此命令用于查询EIR（Equipment Identity Register）表记录。MME（Mobility Management Entity）根据EIR表记录选择EIR。

#### [注意事项](#ZH-CN_MMLREF_0000001126305264)

此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305264)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305264)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305264)

无。

#### [使用实例](#ZH-CN_MMLREF_0000001126305264)

查询系统内EIR表记录：

LST EIR:;

```
%%LST EIR:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
            EIR域名  =  example01.com
          EIR主机名  =  example01.com
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126305264)

参见 [**ADD EIR**](增加EIR配置(ADD EIR)_72345049.md) 的参数说明。
