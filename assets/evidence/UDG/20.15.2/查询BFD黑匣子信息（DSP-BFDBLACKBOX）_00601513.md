# 查询BFD黑匣子信息（DSP BFDBLACKBOX）

- [命令功能](#ZH-CN_CONCEPT_0000001600601513__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600601513__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600601513__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600601513__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600601513__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600601513__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600601513)

该命令行用于查询BFD的黑匣子信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600601513)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600601513)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600601513)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 黑匣子类型 | 可选必选说明：必选参数<br>参数含义：黑匣子的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SESSION：会话信息。<br>- SOCK：套接字。<br>- HA：高可靠性。<br>- SMOOTH_APP：应用平滑信息。<br>- RELIABILITY：可靠性。<br>- SMOOTH_FEI：FEI平滑。<br>- SMOOTH_FES：FES平滑。<br>- FES_TLV：FES的TLV。<br>- GFD_COMMON：GFD公共消息。<br>- GFD_NOTIFY：GFD消息通告。<br>- DISCRIMINATOR：会话标识符。<br>- DEVM_LIB：DEVM消息。<br>- VPN_LIB：VPN消息。<br>- EVENT：事件消息。<br>- IFM_LIB：IFM消息。<br>默认值：无 |
| LOCALDISCR | 本地标识符 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“DISCRIMINATOR”时为必选参数。<br>参数含义：本地描述符。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～49152。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600601513)

查询BFD高可靠性的黑匣子信息：

```
DSP BFDBLACKBOX:TYPE=HA;
```

```

RETCODE = 0  操作成功。

结果如下
----------------
   黑匣子信息  =  2016-12-23 0:38:3:55  Execute batch backup FSM.(input:0,state:0)
2016-12-23 0:38:4:950  Execute batch backup FSM.(input:1,state:1)
2016-12-23 0:38:5:955  Execute batch backup FSM.(input:3,state:2)
2016-12-23 0:38:6:950  Execute batch backup FSM.(input:4,state:3)
2016-12-23 0:38:7:955  Execute batch backup FSM.(input:5,state:4)
2016-12-23 0:38:8:959  Execute batch backup FSM.(input:7,state:6)
2016-12-23 0:38:9:965  Execute batch backup FSM.(input:8,state:7)
2016-12-23 0:38:10:964  Execute batch backup FSM.(input:10,state:8)
2016-12-23 1:30:19:798  Execute component FSM.(input:1,state:7)
(结果个数 = 1)
--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600601513)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 黑匣子信息 | 查询黑匣子返回的信息。 |
