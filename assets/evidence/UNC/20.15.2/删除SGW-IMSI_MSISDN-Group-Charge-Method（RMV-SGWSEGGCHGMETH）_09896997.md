# 删除SGW IMSI/MSISDN Group Charge Method（RMV SGWSEGGCHGMETH）

- [命令功能](#ZH-CN_CONCEPT_0209896997__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896997__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896997__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896997__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896997__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896997)

**适用NF：SGW-C**

![](删除SGW IMSI_MSISDN Group Charge Method（RMV SGWSEGGCHGMETH）_09896997.assets/notice_3.0-zh-cn_2.png)

该命令属于高危命令，如果不输入用户号段组名称，表示删除所有号段组的计费方式配置，可能对SGW的计费功能产生影响，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

该命令用于删除SGW基于号段组的计费方式。

#### [注意事项](#ZH-CN_CONCEPT_0209896997)

- 该命令执行后只对新激活用户生效。
- 该命令属于高危命令，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896997)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896997)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGGROUPNAME | IMSI/MSISDN号段组名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定用户号段组。如果配置了多个用户号段组，则根据优先级来选择。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896997)

根据需求，删除名为“huawei”的号段组的计费方式，命令为：

```
RMV SGWSEGGCHGMETH: SEGGROUPNAME="huawei";
```
