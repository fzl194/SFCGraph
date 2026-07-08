# 查询IPFarm服务器状态（DSP IPFARMSERVER）

- [命令功能](#ZH-CN_CONCEPT_0186526404__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186526404__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186526404__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186526404__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186526404__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0186526404__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0186526404)

**适用NF：PGW-U、UPF**

该命令用于显示该IP farm服务器所在的IP farm中的所有IP farm服务器信息。

#### [注意事项](#ZH-CN_CONCEPT_0186526404)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0186526404)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186526404)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPFARMNAME | IP-Farm名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IP farm名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0186526404)

查询一个IP farm下的全部服务器：

```
DSP IPFARMSERVER:IPFARMNAME="test";
```

```

RETCODE = 0 操作成功。

IPFarmServer信息
----------------
IP-Farm名称 = f2
   地址信息 = fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 服务器状态 = 正常
(结果个数 = 1)
--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0186526404)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 服务器状态 | 用于显示IP farm服务器状态。 |

其余输出项请参见ADD IPFARMSERVER的参数说明。
