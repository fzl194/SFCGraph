# 查询MME IP（LST MMEIPTOMMEPOOL）

- [命令功能](#ZH-CN_MMLREF_0231453515__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0231453515__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0231453515__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0231453515__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0231453515__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0231453515)

**适用NF：SGW-C、PGW-C**

该命令用于显示MME POOL绑定的地址。

## [注意事项](#ZH-CN_MMLREF_0231453515)

无

#### [操作用户权限](#ZH-CN_MMLREF_0231453515)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0231453515)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEPOOLNAME | MME POOL名称 | 参数含义：该参数用于指定MME POOL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD MMEPOOL命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0231453515)

假设用户需要查询名为“mmepool1”的MME POOL：

```
%%LST MMEIPTOMMEPOOL:;%%
RETCODE = 0  操作成功

结果如下
--------
		     MME POOL名称  =  mmepool1
				   IP版本  =  IPV4
		    MME的IPv4地址  =  10.0.0.10
		    MME的IPv6地址  =  ::
		  是否为备份的MME  =  否
				     端口  =  2123
		   MME IP描述信息  =  NULL
备份的MME优先使用的IP版本  =  NULL

(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0231453515)

| 输出项名称 | 输出项解释 |
| --- | --- |
| MME POOL名称 | 该参数用于指定MME POOL名称。 |
| IP版本 | 该参数用于指定MME地址池的地址类型。 |
| MME的IPv4地址 | 该参数指定该地址类型为IPv4地址。 |
| MME的IPv6地址 | 该参数指定该地址类型为IPv6地址。 |
| 是否为备份的MME | 配置是否为备份MME。 |
| 端口 | 指定MME的端口号。 |
| MME IP描述信息 | 该参数用于指定MME IP描述信息。 |
| 备份的MME优先使用的IP版本 | 该参数用于当备份MME IP版本为双栈时，指定IP地址使用优先策略。 |
