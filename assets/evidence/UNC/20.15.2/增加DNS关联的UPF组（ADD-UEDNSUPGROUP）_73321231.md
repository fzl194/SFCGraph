# 增加DNS关联的UPF组（ADD UEDNSUPGROUP）

- [命令功能](#ZH-CN_MMLREF_0273321231__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0273321231__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0273321231__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0273321231__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0273321231)

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加DNS关联的UPF组。

## [注意事项](#ZH-CN_MMLREF_0273321231)

- 该命令执行后立即生效。

- 最多可输入3000条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0273321231)

G_1，管理员级别命令组

## [参数说明](#ZH-CN_MMLREF_0273321231)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0273321231)

增加DNS关联的UPF组，组名为upfgrp1：

```
ADD UEDNSUPGROUP: UPFGRPNAME="upfgrp1";
```
