# 查询IPFarm（DSP IPFARM）

- [命令功能](#ZH-CN_CONCEPT_0182837054__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837054__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837054__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837054__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837054__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837054__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837054)

**适用NF：PGW-U、UPF**

该命令用于显示对应IP farm的信息，包括IP farm的名称。如果参数为空，则显示所有IP farm的信息。

#### [注意事项](#ZH-CN_CONCEPT_0182837054)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837054)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837054)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPFARMNAME | IP-Farm名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IP farm名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837054)

查询一条IP farm记录：

```
DSP IPFARM:;
```

```

RETCODE = 0 操作成功。

IPFarm信息
----------
IP-Farm名称 = test
IP Farm可用服务器数目 = 2
IP Farm服务器数目 = 2
(结果个数 = 1)
--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837054)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 可用IP Farm服务器数目 | 用于显示IPFarm下可用的IPFarmServer数目。 |
| IP Farm服务器数目 | 用于显示IPFarm下配置的IPFarmServer数目。 |

其余输出项请参见ADD IPFARM的参数说明。
