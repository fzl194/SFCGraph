# 查询UE USAGE TYPE群组(LST UEUSGTYPEGP)

- [命令功能](#ZH-CN_MMLREF_0000001126145822__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145822__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145822__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145822__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145822__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145822__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126145822__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145822)

**适用网元：MME**

该命令用于查询UE USAGE TYPE群组记录。

#### [注意事项](#ZH-CN_MMLREF_0000001126145822)

此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145822)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145822)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145822)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组标识。<br>数据来源：本端规划<br>取值范围：0～1023<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145822)

1. 不输入参数，查询UE USAGE TYPE群组：
  LST UEUSGTYPEGP:;
  ```
  %%LST UEUSGTYPEGP: UEUSGTYPEGPID=0;%%
  RETCODE = 0  操作成功

  操作结果如下：
  --------------
  UE USAGE TYPE群组标识  =  0
                   描述  =  eMtc
  (结果个数 = 1)

  ---    END
  ```
2. 查询“UEUSGTYPEGPID”为“0”的配置：
  LST UEUSGTYPEGP: UEUSGTYPEGPID=0;
  ```
  %%LST UEUSGTYPEGP: UEUSGTYPEGPID=0;%%
  RETCODE = 0  操作成功

  操作结果如下：
  --------------
  UE USAGE TYPE群组标识  =  0
                   描述  =  eMtc
  (结果个数 = 1)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126145822)

参见 [**ADD UEUSGTYPEGP**](增加UE USAGE TYPE群组(ADD UEUSGTYPEGP)_72225499.md) 的参数标识。
