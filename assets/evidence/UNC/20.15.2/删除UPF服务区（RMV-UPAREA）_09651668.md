# 删除UPF服务区（RMV UPAREA）

- [命令功能](#ZH-CN_MMLREF_0209651668__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651668__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651668__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651668__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209651668)

**适用NF：SMF、GGSN、SGW-C、PGW-C**

该命令用于删除UPF服务区域。

## [注意事项](#ZH-CN_MMLREF_0209651668)

- 该命令执行后立即生效。

- 使用该命令删除UPF服务区之前，必须先使用命令RMV UPAREABINDS1TAI、RMV UPAREABINDN2TAI、RMV UPAREABINDLAI、RMV SUFFIXS1TAIAREA、RMV SUFFIXLAIAREA删除对应与该服务区名称相同的记录。

#### [操作用户权限](#ZH-CN_MMLREF_0209651668)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651668)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | UPF服务区名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置UPF服务区的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与LST PNFSMFSERAREA查询结果中的SMFSERVINGAREA保持一致。 |

## [使用实例](#ZH-CN_MMLREF_0209651668)

删除区域名称为"UPAREA1"的UPF服务区域：

```
RMV UPAREA: AREANAME="UPAREA1";
```
