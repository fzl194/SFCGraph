# 删除LAC组内LAC号段（RMV ADDRLACID）

- [命令功能](#ZH-CN_MMLREF_0249644926__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0249644926__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0249644926__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0249644926__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0249644926)

**适用NF：PGW-C、SMF、GGSN**

该命令用来删除LAC组内绑定的LAC号段。

## [注意事项](#ZH-CN_MMLREF_0249644926)

该命令执行后只对新激活用户生效。

#### [操作用户权限](#ZH-CN_MMLREF_0249644926)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0249644926)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACGROUPNAME | LAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRLACGROUP命令配置生成。 |
| LACSECNUM | LAC段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~23999。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0249644926)

删除指定LAC组绑定的某个LAC号段，LAC组为“beijing”，LAC号段为“2”时，执行该命令：

```
RMV ADDRLACID:LACGROUPNAME="beijing",LACSECNUM=2;
```
