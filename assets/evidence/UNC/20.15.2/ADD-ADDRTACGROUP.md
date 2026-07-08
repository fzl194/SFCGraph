# 增加TAC组（ADD ADDRTACGROUP）

- [命令功能](#ZH-CN_MMLREF_0249644910__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0249644910__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0249644910__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0249644910__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0249644910)

**适用NF：PGW-C、SMF、GGSN**

该命令用来增加TAC组。

## [注意事项](#ZH-CN_MMLREF_0249644910)

- 该命令执行后立即生效。

- 每种类型的TAC组最大记录数为3000。

- 最多可输入6000条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0249644910)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0249644910)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | TAC组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| TACTYPE | TAC类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC类型。<br>数据来源：本端规划<br>取值范围：<br>- S1TAC（S1TAC）<br>- N2TAC（N2TAC）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0249644910)

增加TAC组，名称是“wz-sq”，类型是“S1TAC”：

```
ADD ADDRTACGROUP: TACGROUPNAME="wz-sq", TACTYPE=S1TAC;
```
