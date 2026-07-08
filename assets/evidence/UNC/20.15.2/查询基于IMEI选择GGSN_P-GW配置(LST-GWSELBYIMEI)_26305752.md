# 查询基于IMEI选择GGSN/P-GW配置(LST GWSELBYIMEI)

- [命令功能](#ZH-CN_MMLREF_0000001126305752__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305752__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305752__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305752__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305752__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305752__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126305752__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305752)

**适用网元：SGSN、MME**

该命令用于查询基于IMEI选择GGSN/P-GW配置记录。

#### [注意事项](#ZH-CN_MMLREF_0000001126305752)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305752)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305752)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305752)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指示IMEI群组标识，<br>UNC<br>需要为这些类型终端选择特定GGSN/P-GW。<br>数据来源：本端规划<br>取值范围：1~50<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305752)

查询IMEI群组标识为1的基于IMEI选择P-GW/GGSN配置：

LST GWSELBYIMEI: IMEIGPID=1;

```
%%LST GWSELBYIMEI:IMEIGPID=1;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
IMEI群组标识  =  1
    定制标识  =  CAT6
(结果个数 = 1)

---    END
```

查询所有基于IMEI选择P-GW/GGSN配置：

LST GWSELBYIMEI:;

```
%%LST GWSELBYIMEI:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
IMEI群组标识  =  1
    定制标识  =  CAT6
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126305752)

参见 [**ADD GWSELBYIMEI**](增加基于IMEI选择GGSN_P-GW配置(ADD GWSELBYIMEI)_72345541.md) 的参数说明。
