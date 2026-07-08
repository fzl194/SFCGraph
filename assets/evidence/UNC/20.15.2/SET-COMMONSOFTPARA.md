# 设置公共软参（SET COMMONSOFTPARA）

- [命令功能](#ZH-CN_MMLREF_0000001426254845__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001426254845__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001426254845__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001426254845__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001426254845)

该命令用于设置公共软件参数信息。

## [注意事项](#ZH-CN_MMLREF_0000001426254845)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

> **说明**
> 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| DATATYPE | DWORDCOMNUM | DWORDCOMVALUE |
| --- | --- | --- |
| DwCom | 1 | 4 |
| DwCom | 2 | 0 |
| DwCom | 3 | 4100 |
| DwCom | 4 | 256 |
| DwCom | 5 | 0 |
| DwCom | 6 | 0 |
| DwCom | 7 | 0 |
| DwCom | 8 | 0 |
| DwCom | 9 | 0 |
| DwCom | 10 | 0 |
| DwCom | 11 | 0 |
| DwCom | 12 | 0 |
| DwCom | 13 | 0 |
| DwCom | 14 | 0 |
| DwCom | 15 | 0 |
| DwCom | 16 | 0 |
| DwCom | 17 | 0 |
| DwCom | 18 | 0 |
| DwCom | 19 | 0 |
| DwCom | 20 | 0 |

#### [操作用户权限](#ZH-CN_MMLREF_0000001426254845)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001426254845)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DATATYPE | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- “DwCom（公共双字）”：公共双字<br>默认值：无。<br>配置原则：无 |
| DWORDCOMNUM | Common Dword索引 | 可选必选说明：该参数在"DATATYPE"配置为"DwCom"时为条件必选参数。<br>参数含义：该参数表示Common Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1500。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST COMMONSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| DWORDCOMVALUE | Common Dword值 | 可选必选说明：该参数在"DATATYPE"配置为"DwCom"时为条件必选参数。<br>参数含义：该参数表示Common Dword类型软件参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST COMMONSOFTPARA查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001426254845)

设置公共软件参数，数据类型是“DwCom”，Common Dword索引是“1”，Common Dword值是“3”

```
SET COMMONSOFTPARA: DATATYPE=DwCom, DWORDCOMNUM=1, DWORDCOMVALUE=3;
```
