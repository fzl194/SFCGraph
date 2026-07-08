# 清除动态PCRF（CLR DYNAMICPCRF）

- [命令功能](#ZH-CN_CONCEPT_0209897123__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897123__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897123__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897123__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897123__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897123)

**适用NF：PGW-C、GGSN**

![](清除动态PCRF（CLR DYNAMICPCRF）_09897123.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除对端信息可能导致已在线用户发送CCR消息失败。

此命令用于删除动态PCRF主机列表表项。

#### [注意事项](#ZH-CN_CONCEPT_0209897123)

- 该命令执行后立即生效。
- 动态PCRF主机列表最多支持2000个表项。
- 删除动态PCRF会导致已在线用户无法按照之前的Destination-Host和Destination-Realm封装发送CCR消息。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897123)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897123)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | PCRF主机名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示动态PCRF主机的主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897123)

删除所有动态PCRF主机列表：

```
CLR DYNAMICPCRF:;
```
