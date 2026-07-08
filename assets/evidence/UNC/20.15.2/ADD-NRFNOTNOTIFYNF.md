# 增加不通知NF实例（ADD NRFNOTNOTIFYNF）

- [命令功能](#ZH-CN_MMLREF_0000001360329621__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001360329621__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001360329621__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001360329621__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001360329621)

![](增加不通知NF实例（ADD NRFNOTNOTIFYNF）_60329621.assets/notice_3.0-zh-cn_2.png)

该命令与NRF通知策略SET NRFNOTIFYPLY配合使用，当SET NRFNOTIFYPLY的NRFNOTIFYPLY设置为NFINSTANCEIDNOT时，请谨慎添加NF实例信息，否则对于添加到列表中的NF，NRF将不会通知其注册变更信息。

**适用NF：NRF**

该命令用于增加不通知的NF实例，当列表中的NF注册信息发生变更时，NRF将不会发送对应的订阅通知消息。

## [注意事项](#ZH-CN_MMLREF_0000001360329621)

- 该命令执行后立即生效。

- 最多可输入1024条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001360329621)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001360329621)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：<br>该命令与SET NRFNOTIFYPLY配合使用，当SET NRFNOTIFYPLY中的NOTIFYNPLY参数设置为“NFINSTANCEIDNOT”时生效。 |

## [使用实例](#ZH-CN_MMLREF_0000001360329621)

当运营商希望NF实例标识为“88888888-4444-1234-5678-123456789abc”的NF注册信息发生变更时，NRF不发送通知消息，执行如下命令。

```
ADD NRFNOTNOTIFYNF: NFINSTANCEID="88888888-4444-1234-5678-123456789abc";
SET NRFNOTIFYPLY: NOTIFYPLY=NFINSTANCEIDNOT;
```
