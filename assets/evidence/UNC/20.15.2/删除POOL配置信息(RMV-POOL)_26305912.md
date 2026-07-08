# 删除POOL配置信息(RMV POOL)

- [命令功能](#ZH-CN_MMLREF_0000001126305912__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305912__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305912__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305912__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305912__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305912__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305912)

![](删除POOL配置信息(RMV POOL)_26305912.assets/notice_3.0-zh-cn_2.png)

[**RMV POOL**](删除POOL配置信息(RMV POOL)_26305912.md) 命令执行后需要复位整系统才能生效。

**适用网元：SGSN**

该命令用于删除POOL配置信息。

#### [注意事项](#ZH-CN_MMLREF_0000001126305912)

- 该命令执行后需要复位整系统才能生效，复位整系统请参考**RST VNFC**命令。
- POOLID必须是在POOL表中存在记录。
- 必须保证所删除的POOL区未配置LOCALNRI(RMV LOCALNRI)和POOLNRI(RMV POOLNRI)；否则，不允许删除。
- 删除POOL记录会同时清除OFFLOADINF中的POOLID和NULLNRI记录。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305912)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305912)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305912)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定POOL标识。<br>取值范围：0~4095<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305912)

删除一个POOL配置信息，POOLID为1：

RMV POOL: POOLID=1;
