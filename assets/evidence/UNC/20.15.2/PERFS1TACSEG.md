# 查询S1TAC段（LST PERFS1TACSEG）

- [命令功能](#ZH-CN_MMLREF_0244529807__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0244529807__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0244529807__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0244529807__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0244529807__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0244529807)

**适用NF：SGW-C、PGW-C**

该命令用来查询S1TAC号段。

## [注意事项](#ZH-CN_MMLREF_0244529807)

无

#### [操作用户权限](#ZH-CN_MMLREF_0244529807)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0244529807)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACSEGNAME | TAC段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TAC段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0244529807)

当运营商需要查看指定TAC号段时，执行如下命令：

```
LST PERFS1TACSEG: TACSEGNAME="changping";
%%LST PERFS1TACSEG: TACSEGNAME="changping";%%
RETCODE = 0  操作成功

结果如下
--------
  TAC段名称  =  changping
TAC段起始值  =  0x0001
TAC段结束值  =  0x0002
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0244529807)

| 输出项名称 | 输出项解释 |
| --- | --- |
| TAC段名称 | 该参数用于指定TAC段名称。 |
| TAC段起始值 | 该参数用于指定TAC段的起始值。 |
| TAC段结束值 | 该参数用于指定TAC段的结束值。 |
