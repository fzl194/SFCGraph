# 查询LAC组内LAC号段（LST ADDRLACID）

- [命令功能](#ZH-CN_MMLREF_0249644913__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0249644913__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0249644913__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0249644913__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0249644913__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0249644913)

**适用NF：PGW-C、SMF、GGSN**

该命令用来查询指定LAC号段与LAC组的绑定关系或者配置的所有LAC号段和LAC组的绑定关系。

## [注意事项](#ZH-CN_MMLREF_0249644913)

无

#### [操作用户权限](#ZH-CN_MMLREF_0249644913)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0249644913)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACGROUPNAME | LAC组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRLACGROUP命令配置生成。 |
| LACSECNUM | LAC段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~23999。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0249644913)

查询指定LAC号段与LAC组的绑定关系：LAC组为“beijing”，LAC号段为“2”：

```
LST ADDRLACID: LACGROUPNAME="beijing", LACSECNUM=2;
RETCODE = 0  操作成功。

结果如下
--------
      LAC组名  =  beijing
    LAC段编号  =  2
    LAC起始ID  =  0x1
    LAC截止ID  =  0x10
(结果个数 = 1)
---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0249644913)

| 输出项名称 | 输出项解释 |
| --- | --- |
| LAC组名 | 该参数用于指定LAC组名。 |
| LAC段编号 | 该参数用于指定LAC段编号。 |
| LAC起始ID | 该参数用于指定LAC起始ID。 |
| LAC终止ID | 该参数用于指定LAC终止ID。 |
