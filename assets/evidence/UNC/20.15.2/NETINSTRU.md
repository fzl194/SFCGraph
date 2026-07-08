# 查询网络实例对应RU信息(DSP NETINSTRU)

- [命令功能](#ZH-CN_CONCEPT_0129626916__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0129626916__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0129626916__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0129626916__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0129626916__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0129626916__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0129626916)

该命令用于查询网络实例对应RU信息。

#### [注意事项](#ZH-CN_CONCEPT_0129626916)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0129626916)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0129626916)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NETINSTNAME | 网络实例名称 | 可选必选说明：可选参数。<br>参数含义：要查询的网络实例的名称。<br>数据来源：本端规划。<br>默认值：无。<br>取值范围：长度为1～63的字符串。<br>配置原则：不支持空格和符号'?'，区分大小写。 |

#### [使用实例](#ZH-CN_CONCEPT_0129626916)

查询网络实例NetInstanceDefault对应的RU信息。

```
DSP NETINSTRU: NETINSTNAME="NetInstanceDefault";
```

```
%%DSP NETINSTRU: NETINSTNAME="NetInstanceDefault";%%
RETCODE = 0  操作成功。

结果如下
-------------------------
网络实例名称       网络实例ID     ScaleGroup名称     ScaleGroup ID      RU ID     VNFC类型
NetInstanceDefault 0              SG0_CSLB_IPFWD     0                  64        CSLB_VNFC
NetInstanceDefault 0              SG0_CSLB_IPFWD     0                  65        CSLB_VNFC
NetInstanceDefault 0              SG0_CSLB_IPFWD     0                  65        VNRS_VNFC
NetInstanceDefault 0              SG0_CSLB_IPFWD     0                  64        VNRS_VNFC  
(结果个数 = 4)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0129626916)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 网络实例名称 | 查询的网络实例的名称。<br>取值范围：字符串类型，长度1~63。 |
| 网络实例ID | 查询的网络实例的ID。<br>取值范围：整数类型，取值范围为0～4。 |
| ScaleGroup名称 | 查询的网络实例的ScaleGroup名称。<br>取值范围：字符串类型，长度1~63。 |
| ScaleGroup ID | 查询的网络实例的ScaleGroupID。<br>取值范围：整数类型，取值范围为0～4294967294。 |
| RU ID | 查询的网络实例对应RU的ID。<br>取值范围：整数类型，取值范围为0～4294967294。 |
| VNFC类型 | 查询的网络实例对应RU的VNFC类型。<br>取值范围：字符串类型，长度1~63。 |
