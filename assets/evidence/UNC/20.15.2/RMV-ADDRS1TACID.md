# 删除S1TAC组内S1TAC号段（RMV ADDRS1TACID）

- [命令功能](#ZH-CN_MMLREF_0249644928__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0249644928__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0249644928__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0249644928__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0249644928)

**适用NF：PGW-C、GGSN、SMF**

该命令用来删除S1TAC组内绑定的S1TAC号段。

## [注意事项](#ZH-CN_MMLREF_0249644928)

该命令执行后只对新激活用户生效。

#### [操作用户权限](#ZH-CN_MMLREF_0249644928)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0249644928)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | S1TAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定S1TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRTACGROUP命令配置生成。 |
| TACSECNUM | S1TAC段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S1TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15999。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0249644928)

在一个本地已经配置的S1TAC组删除一个S1TAC号段：

```
RMV ADDRS1TACID:TACGROUPNAME="wz-xs",TACSECNUM=2;
```
