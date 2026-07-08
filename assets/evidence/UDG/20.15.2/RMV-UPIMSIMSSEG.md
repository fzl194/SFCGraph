# 删除IMSI和MSISDN号段（RMV UPIMSIMSSEG）

- [命令功能](#ZH-CN_CONCEPT_0000202985042561__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202985042561__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202985042561__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202985042561__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202985042561__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202985042561)

**适用NF：PGW-U、UPF**

该命令用于删除IMSI/MSISDN号码段。

#### [注意事项](#ZH-CN_CONCEPT_0000202985042561)

- 该命令执行后立即生效。
- 如果号段被绑定，则不能删除IMSI和MSISDN号段。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202985042561)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202985042561)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000202985042561)

删除IMSI和MSISDN号段,SEGMENTNAME为huawei，命令为：

```
RMV UPIMSIMSSEG:SEGMENTNAME="huawei";
```
