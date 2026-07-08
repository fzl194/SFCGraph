# 查询N2TAC组内N2TAC号段（LST ADDRN2TACID）

- [命令功能](#ZH-CN_MMLREF_0249644914__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0249644914__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0249644914__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0249644914__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0249644914__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0249644914)

**适用NF：GGSN、SMF、PGW-C**

该命令用来查询指定N2TAC号段与N2TAC组的绑定关系或者配置的所有N2TAC号段和N2TAC组的绑定关系。

## [注意事项](#ZH-CN_MMLREF_0249644914)

无

#### [操作用户权限](#ZH-CN_MMLREF_0249644914)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0249644914)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | N2TAC组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N2TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRTACGROUP命令配置生成。 |
| TACSECNUM | N2TAC段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N2TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15999。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0249644914)

查询指定N2TAC号段与N2TAC组的绑定关系：“N2TAC组”为“wz-sq”，“N2TAC号段”为“2”：

```
LST ADDRN2TACID:TACGROUPNAME="wz-sq",TACSECNUM=2;
RETCODE = 0  操作成功。

结果如下
------------------------
   N2TAC组名  =  wz-sq
 N2TAC段编号  =  2
 N2TAC起始ID  =  0x1
 N2TAC终止ID  =  0x1F
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0249644914)

| 输出项名称 | 输出项解释 |
| --- | --- |
| N2TAC组名 | 该参数用于指定N2TAC组名。 |
| N2TAC段编号 | 该参数用于指定N2TAC段编号。 |
| N2TAC起始ID | 该参数用于指定N2TAC起始ID。 |
| N2TAC终止ID | 该参数用于指定N2TAC终止ID。 |
