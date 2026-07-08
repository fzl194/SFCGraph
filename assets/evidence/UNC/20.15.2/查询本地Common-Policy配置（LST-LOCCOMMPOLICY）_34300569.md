# 查询本地Common Policy配置（LST LOCCOMMPOLICY）

- [命令功能](#ZH-CN_MMLREF_0000001434300569__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001434300569__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001434300569__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001434300569__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001434300569__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001434300569)

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询本地Common Policy配置。

## [注意事项](#ZH-CN_MMLREF_0000001434300569)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001434300569)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001434300569)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD USERPROFILE命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0000001434300569)

查询本地Common Policy配置，USERPROFILENAME为testuserprofilename1。

```
LST LOCCOMMPOLICY: USERPROFILENAME= testuserprofilename1;
RETCODE = 0  操作成功

结果如下
--------
用户模板名称  =  testuserprofilename1
优先级  =  3
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001434300569)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 用户模板名称 | 该参数用于指定用户模板名称。 |
| 优先级 | 该参数用于指定UserProfile的全局优先级。 |
