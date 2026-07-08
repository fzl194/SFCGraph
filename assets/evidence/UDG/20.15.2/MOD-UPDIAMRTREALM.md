# 修改Diameter路由域名信息（MOD UPDIAMRTREALM）

- [命令功能](#ZH-CN_CONCEPT_0000206297314573__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206297314573__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206297314573__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206297314573__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206297314573__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206297314573)

**适用NF：UPF**

![](修改Diameter路由域名信息（MOD UPDIAMRTREALM）_97314573.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会修改Diameter路由域名信息，可能会影响DRA的选择。

该命令用于修改Diameter路由的配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0000206297314573)

- 该命令执行后立即生效。
- 该命令Failover和自动倒回相关的功能20.14版本暂不支持。
- 应用和realm对应的Diameter路由需已经通过ADD UPDIAMRTREALM添加成功才可修改。
- 基于会话轮循的路由选择模式下，根据Session-id选择的DRA状态异常时，会选择Diameter路由中下一个链路正常的DRA进行消息交互。当根据Session-id选择的DRA状态恢复正常后，会重新选择该DRA进行消息交互。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206297314573)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206297314573)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMNAME | Diameter域名名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的realm名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 2670控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：无 |
| SELECTMODE | 路由选择模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定到同一realm的多条路由的路由选择模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER_SLAVE：主备模式。<br>- SESSION_ID：基于会话的轮循模式。<br>- ROUND_ROBIN：基于消息的轮循模式。<br>默认值：无<br>配置原则：无 |
| FAILOVERSW | Failover开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的Failover开关是否开启。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| AUTOFAILBACKSW | 自动倒回开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的自动倒回开关是否开启。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206297314573)

修改Swm应用且realm名为example.com的Diameter路由选择模式为基于会话的轮循(session-id)：

```
MOD UPDIAMRTREALM: REALMNAME="example.com", APPLICATION=SWM, SELECTMODE=SESSION_ID, FAILOVERSW=ENABLE, AUTOFAILBACKSW=ENABLE;
```
