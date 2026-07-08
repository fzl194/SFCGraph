# 删除SMF的NodeID（RMV CPNODEID）

- [命令功能](#ZH-CN_CONCEPT_0216780317__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0216780317__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0216780317__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0216780317__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0216780317__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0216780317)

**适用NF：PGW-U、UPF**

![](删除SMF的NodeID（RMV CPNODEID）_16780317.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果当前CPNODEID与相应的地址池组存在绑定关系，即通过PoolGrpMap命令与相应地址池组绑定，删除CPNODEID时对应关联的PoolGrpMap会被连带删除。

该命令用于删除指定SMF实例信息。

#### [注意事项](#ZH-CN_CONCEPT_0216780317)

- 该命令执行后只对新激活用户生效。
- 删除指定SMF实例时会同时删除关联的PoolGrpMap实例。

#### [操作用户权限](#ZH-CN_CONCEPT_0216780317)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0216780317)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPNAME | SMF名称 | 可选必选说明：必选参数<br>参数含义：SMF的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0216780317)

删除名为smfnode1的SMF实例：

```
RMV CPNODEID: CPNAME="smfnode1";
```
