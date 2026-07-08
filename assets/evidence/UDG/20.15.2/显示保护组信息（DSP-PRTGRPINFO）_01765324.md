# 显示保护组信息（DSP PRTGRPINFO）

- [命令功能](#ZH-CN_MMLREF_0000001401765324__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001401765324__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001401765324__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001401765324__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001401765324__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001401765324)

该命令用于显示保护组信息。

外部网关路由器只与保护组内ISU/APU之间建立BFD会话，备路由也只到保护组内ISU/APU的ECMP路由。

> **说明**
> - 此命令仅在虚机场景下支持。
> - 仅ISU/APU场景支持显示保护组信息。

#### [操作用户权限](#ZH-CN_MMLREF_0000001401765324)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001401765324)

无

## [使用实例](#ZH-CN_MMLREF_0000001401765324)

假如运营商想要查看哪些VNRS RU处于保护组中，调用以下命令可以看到所有处于保护组中的VNRS RU信息。

```
%%DSP PRTGRPINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
RuId  RuName           PodName    VmId                              VmName                      

64    VNRS_IP_RU_0064  isu-pod-0  cef65e1bbe3045279fee856349d7b84b  env198_UDG_VNF_1109_ISU__1  
65    VNRS_IP_RU_0065  isu-pod-1  b04ad5c5aadc4e7a9d8f67a3d86bc906  env198_UDG_VNF_1109_ISU__0  
(结果个数 = 2)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001401765324)

| 输出项名称 | 输出项解释 |
| --- | --- |
| RuId | 该参数是Ru的唯一标识。 |
| RuName | 该参数用于表示Ru名称。 |
| PodName | 该参数用于表示Pod名称。 |
| VmId | 该参数是Vm的唯一标识。 |
| VmName | 该参数用于标识Vm名称。 |
