# 阻塞IMSI在特定的Worker Pod上激活配置（ACT IMSIBLOCKWKPOD）

- [命令功能](#ZH-CN_CONCEPT_0000201900205642__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201900205642__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201900205642__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201900205642__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201900205642__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201900205642)

**适用NF：PGW-U、UPF**

阻塞IMSI在特定的Worker Pod上激活配置。

#### [注意事项](#ZH-CN_CONCEPT_0000201900205642)

- 激活或更新前已经配置ImsiAllowWkPod/ImsiBlockWkPod的用户，本命令是新数据流生效，否则是新激活或更新的用户生效。
- 该命令和ACT ImsiAllowWkPod总规格为64。
- 同一个IMSI，同一个WORKERTYPE且同一个PodName不允许既配置ACT ImsiAllowWkPod又配置ACT ImsiBlockWkPod。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201900205642)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201900205642)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| WORKERTYPE | Worker类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Worker类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- to：TCP优化。<br>默认值：无<br>配置原则：无 |
| PODNAME | Pod 名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：WORKERTYPE参数填写为to时，该参数需配置成TO-POD类型的POD名称。 |
| TIMEOUT | 超时时长 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置生效时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～7200，单位是分钟。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000201900205642)

当需要阻塞IMSI 1234567890与to-pod-0、类型为to的POD的绑定关系时，且超时时长为120分钟，进行如下设置：

```
ACT IMSIBLOCKWKPOD: IMSI="1234567890", PODNAME="to-pod-0", TIMEOUT=120, WORKERTYPE=to;
```
