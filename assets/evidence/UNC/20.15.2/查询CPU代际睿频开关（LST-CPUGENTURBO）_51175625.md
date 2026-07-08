# 查询CPU代际睿频开关（LST CPUGENTURBO）

- [命令功能](#ZH-CN_MMLREF_0000001951175625__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001951175625__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001951175625__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001951175625__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001951175625__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001951175625)

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询不同CPU代际睿频的开关状态。

## [注意事项](#ZH-CN_MMLREF_0000001951175625)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001951175625)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001951175625)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPUGENERATION | CPU代际类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CPU代际类型。<br>数据来源：本端规划<br>取值范围：<br>- Icelake（Icelake代际）<br>- Skylake（kylake代际）<br>- Broadwell（Broadwell代际）<br>- Haswell（Haswell代际）<br>- CascadeLake（CascadeLake代际）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001951175625)

查询CPU代际类型为Icelake的代际开关：

```
LST CPUGENTURBO:CPUGENERATION=Icelake;
```

## [输出结果说明](#ZH-CN_MMLREF_0000001951175625)

| 输出项名称 | 输出项解释 |
| --- | --- |
| CPU代际类型 | 该参数用于指定CPU代际类型。 |
| 睿频开关 | 该参数用于设置睿频的开关。 |
