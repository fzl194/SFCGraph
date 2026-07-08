# 修改基于ARP的DDN消息优先级配置（MOD DDNPRIORITYARP）

- [命令功能](#ZH-CN_MMLREF_0304284718__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0304284718__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0304284718__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0304284718__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0304284718)

**适用NF：SGW-C、SMF**

该命令用于修改基于ARP的DDN消息优先级。

## [注意事项](#ZH-CN_MMLREF_0304284718)

- 该命令执行后立即生效。

- 该命令用于DDN流控场景下，UNC识别DDN消息的优先级。
- DDN Throttling功能使能时高优先级业务流触发的DDN消息不流控。当用户不配置DDNPRIORITYARP时，则默认为低优先级。

#### [操作用户权限](#ZH-CN_MMLREF_0304284718)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0304284718)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ARP | ARP数值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DDN消息的优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DDN_LOW（低）<br>- DDN_HIGH（高）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0304284718)

修改ARP为1的DDN消息是高优先级：

```
MOD DDNPRIORITYARP: ARP=1, PRIORITY=DDN_HIGH;
```
