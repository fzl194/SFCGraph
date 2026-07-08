# 设置获取UPF服务区绑定TAI/LAI的方式（SET UPAREABINDFUNC）

- [命令功能](#ZH-CN_MMLREF_0000001870462629__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001870462629__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001870462629__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001870462629__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001870462629)

**适用NF：PGW-C、GGSN、SGW-C**

该命令用于设置获取UPF服务区绑定TAI/LAI的方式。

## [注意事项](#ZH-CN_MMLREF_0000001870462629)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| EFFECTIVEMODE |
| --- |
| PREFIX |

#### [操作用户权限](#ZH-CN_MMLREF_0000001870462629)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001870462629)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EFFECTIVEMODE | 生效方式 | 可选必选说明：必选参数<br>参数含义：该参数用于标识获取UPF服务区绑定TAI/LAI的方式。<br>数据来源：全网规划<br>取值范围：<br>- “PREFIX（采用前缀的方式）”：如果配置为采用前缀的方式读取，仅会读取UPAREABINDS1TAI/UPAREABINDLAI配置<br>- “SUFFIX（采用后缀的方式）”：如果配置为采用后缀的方式读取，仅会读取SUFFIXS1TAIAREA/SUFFIXLAIAREA配置<br>- “BOTH（前缀方式和后缀方式同时生效）”：如果配置为采用前缀方式和后缀方式同时生效的方式读取，会读取UPAREABINDS1TAI/UPAREABINDLAI/SUFFIXS1TAIAREA/SUFFIXLAIAREA配置<br>默认值：无。<br>配置原则：<br>默认采用前缀的方式读取。 |

## [使用实例](#ZH-CN_MMLREF_0000001870462629)

以下命令用于设置获取UPF服务区绑定TAI/LAI的方式，将生效方式设置为采用前缀的方式：

```
SET UPAREABINDFUNC: EFFECTIVEMODE=PREFIX;
```
