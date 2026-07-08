# 查询VNF部署模式（DSP VNFMODE）

- [命令功能](#ZH-CN_MMLREF_0000001449306990__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001449306990__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001449306990__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001449306990__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001449306990__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001449306990)

该命令用于查询VNF部署模式。

> **说明**
> 无

#### [操作用户权限](#ZH-CN_MMLREF_0000001449306990)

G_1，管理员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001449306990)

无

## [使用实例](#ZH-CN_MMLREF_0000001449306990)

查询VNF部署模式。

```
%%DSP VNFMODE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
VNF容器模式  =  VM_CONTAINER
裸机部署模式  =  DomainHost
Vnfm接口模式 =  stack
附加模式     =  0
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001449306990)

| 输出项名称 | 输出项解释 |
| --- | --- |
| VNF容器模式 | 该参数表示VNF的容器模式。<br>取值说明：<br>- "VM_CONTAINER"：虚机容器。<br>- "BARE_CONTAINER"：裸机容器。 |
| 裸机部署模式 | 该参数表示VNF的裸机部署模式。<br>取值说明：<br>- "ResourceBoxHost"：ResourceBoxHost部署模式。<br>- "DomainHost"：历史裸机部署模式。 |
| Vnfm接口模式 | 该参数表示Vnfm接口模式。<br>取值说明：<br>- "stack"：历史stack接口模式。<br>- "release"：release接口模式。 |
| 附加模式 | 该参数表示附加模式。 |
