# 查询SGW IP（LST SGWIPTOSGWPOOL）

- [命令功能](#ZH-CN_MMLREF_0231453517__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0231453517__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0231453517__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0231453517__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0231453517__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0231453517)

**适用NF：PGW-C、SGW-C**

该命令用于显示SGW POOL下绑定的SGW IP。

## [注意事项](#ZH-CN_MMLREF_0231453517)

无

#### [操作用户权限](#ZH-CN_MMLREF_0231453517)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0231453517)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SGWPOOLNAME | SGW POOL名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGW POOL名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>该参数使用ADD SGWPOOL命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0231453517)

假设用户需要查询所有SGW POOL下绑定的SGW IP：

```
%%LST SGWIPTOSGWPOOL:;%%
RETCODE = 0  操作成功

结果如下
--------
 SGW POOL名称  =  sgwpool1
       IP版本  =  IPV4
SGW的IPv4地址  =  10.100.100.100
SGW的IPv6地址  =  ::
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0231453517)

| 输出项名称 | 输出项解释 |
| --- | --- |
| SGW POOL名称 | 该参数用于指定SGW POOL名。 |
| IP版本 | 该参数用于指定SGW POOL的地址类型。 |
| SGW的IPv4地址 | 该参数在“IPVERSION”配置为“IPv4”时为必选参数。 |
| SGW的IPv6地址 | 该参数在“IPVERSION”配置为“IPv6”时为必选参数。 |
