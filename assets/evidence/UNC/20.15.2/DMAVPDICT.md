# 查询Diameter AVP表(LST DMAVPDICT)

- [命令功能](#ZH-CN_MMLREF_0000001126145860__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145860__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145860__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145860__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145860__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145860__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126145860__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145860)

**适用网元：SGSN、MME**

该命令用于查询Diameter数据字典。

#### [注意事项](#ZH-CN_MMLREF_0000001126145860)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145860)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145860)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145860)

无。

#### [使用实例](#ZH-CN_MMLREF_0000001126145860)

查询Diameter数据字典：

LST DMAVPDICT:;

```
%%LST DMAVPDICT:;%%
RETCODE = 0  执行成功。

操作结果如下
-------------------------
        字典名称  =  6
        信元名称  =  129
        信元编码  =  1032
      Vendor标识  =  10415
        信元类型  =  DIAM_AVP_TYPE_UINT32
        信元标记  =  DIAM_AVP_FLAG_V_PRESENT
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126145860)

参见 [**MOD DMAVPDICT**](修改Diameter数据字典中的AVP参数(MOD DMAVPDICT)_26305668.md) 的参数标识。
