# 配置MOS分类的区间值（SET VONRMOSCLASS）

- [命令功能](#ZH-CN_CONCEPT_0000203091535712__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203091535712__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203091535712__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203091535712__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203091535712__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203091535712)

**适用NF：UPF**

该命令用于设置MOS分类区间边界值。

#### [注意事项](#ZH-CN_CONCEPT_0000203091535712)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 配置的四个参数的值必须满足MOS值为excellent和good之间的边界值大于MOS值为good和accept之间的边界值，MOS值为good和accept之间的边界值大于MOS值为accept和poor之间的边界值，MOS值为accept和poor之间的边界值大于MOS值为poor和bad之间的边界值。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | MOSEXECGOOD | MOSGOODACCP | MOSACCPPOOR | MOSPOORBAD |
| --- | --- | --- | --- | --- |
| 初始值 | 40 | 36 | 31 | 26 |

#### [操作用户权限](#ZH-CN_CONCEPT_0000203091535712)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203091535712)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOSEXECGOOD | MOS值为excellent和good之间的边界值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MOS值为excellent和good之间的边界值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～49，粒度为100。<br>默认值：无<br>配置原则：无 |
| MOSGOODACCP | MOS值为good和accept之间的边界值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MOS值为good和accept之间的边界值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～48，粒度为100。<br>默认值：无<br>配置原则：无 |
| MOSACCPPOOR | MOS值为accept和poor之间的边界值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MOS值为accept和poor之间的边界值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～47，粒度为100。<br>默认值：无<br>配置原则：无 |
| MOSPOORBAD | MOS值为poor和bad之间的边界值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MOS值为poor和bad之间的边界值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～46，粒度为100。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000203091535712)

设置MOS值为excellent和good之间的边界值为41：

```
SET VONRMOSCLASS: MOSEXECGOOD=41;
```
