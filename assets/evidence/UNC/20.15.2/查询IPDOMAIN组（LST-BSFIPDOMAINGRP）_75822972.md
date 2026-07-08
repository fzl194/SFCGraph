# 查询IPDOMAIN组（LST BSFIPDOMAINGRP）

- [命令功能](#ZH-CN_MMLREF_0000001875822972__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001875822972__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001875822972__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001875822972__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001875822972__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001875822972)

该命令用于查询IPDOMAIN组。

## [注意事项](#ZH-CN_MMLREF_0000001875822972)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001875822972)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001875822972)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPNAME | IPDOMAIN组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPDOMAIN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001875822972)

查询IPDOMAIN组"ipdomaingroup1"中的IPDOMAIN信息：

```
%%LST BSFIPDOMAINGRP: GRPNAME="ipdomaingroup1";%%
RETCODE = 0  操作成功

结果如下
--------
IPDOMAIN组名  =  ipdomaingroup1
IPDOMAIN名称  =  Domain_0
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001875822972)

| 输出项名称 | 输出项解释 |
| --- | --- |
| IPDOMAIN组名 | 该参数用于指定IPDOMAIN组名。 |
| IPDOMAIN名称 | 该参数用于指定IPDOMAIN名称。 |
