# 删除RADIUS服务器的UP列表中指定UP的功能属性（RMV RDSUPFCTRL）

- [命令功能](#ZH-CN_MMLREF_0000001182242449__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001182242449__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001182242449__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001182242449__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001182242449)

**适用NF：SMF、PGW-C、GGSN**

该命令用来删除RADIUS服务器使用的UP列表中指定UPF的功能属性。

## [注意事项](#ZH-CN_MMLREF_0000001182242449)

- 该命令执行后立即生效。

- 会在下一次二次鉴权RADIUS中转UPF会话创建时生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001182242449)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001182242449)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPLISTNAME | UP列表名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。该参数需要是UPLIST4RDS配置中已添加的UPLISTNAME的值。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD UPLIST4RDS**](../../连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)<br>命令配置生成。 |
| UPINSTANCEID | UP实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UP实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数取值需要是UPLIST4RDS配置中已添加的UPINSTANCEID的值。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD UPLIST4RDS**](../../连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)<br>命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0000001182242449)

删除UP列表名为“uplist1”，UP名为“up1”的配置记录：

```
RMV UPLIST4RDS: UPLISTNAME="uplist1", UPINSTANCEID="up1";
```
