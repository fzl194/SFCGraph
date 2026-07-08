# 复位CSDB子实例（RST DBINSTANCE）

- [命令功能](#ZH-CN_CONCEPT_0129626988__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0129626988__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0129626988__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0129626988__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0129626988__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0129626988)

![](复位CSDB子实例（RST DBINSTANCE）_29626988.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当，子实例所属的集群的数据会被清空，请谨慎使用并联系华为技术支持协助操作。

该命令用于复位指定的子实例。

#### [注意事项](#ZH-CN_CONCEPT_0129626988)

无

#### [操作用户权限](#ZH-CN_CONCEPT_0129626988)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0129626988)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | 子实例标识 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定唯一一个子实例，可以通过<br>**[DSP DBINSTANCE](查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)**<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：1～100。<br>默认值：无。 |

#### [使用实例](#ZH-CN_CONCEPT_0129626988)

复位标识为 “1” 的子实例：

RST DBINSTANCE: INSTANCEID=1;

```
%%
RST DBINSTANCE: INSTANCEID=1
;%%
RETCODE = 0  Operation succeeded

---    END
```
