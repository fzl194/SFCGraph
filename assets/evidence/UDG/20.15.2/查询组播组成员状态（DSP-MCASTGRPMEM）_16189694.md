# 查询组播组成员状态（DSP MCASTGRPMEM）

- [命令功能](#ZH-CN_CONCEPT_0000202616189694__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202616189694__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202616189694__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202616189694__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202616189694__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000202616189694__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202616189694)

**适用NF：UPF**

该命令用于查询静态组播组内成员激活状态。

#### [注意事项](#ZH-CN_CONCEPT_0000202616189694)

- 该命令执行后立即生效。
- 状态激活显示为Active，状态未激活显示为Inactive。
- IMSI类型的组播组成员，只有当该IMSI对应的用户激活在该静态组播组绑定的5G LAN组会话下，状态才是Active。
- VTEP类型的组播组成员，链路状态UP时，状态为Active。
- DFSR PAIR类型的组播组成员，结对中有一个用户激活，状态就显示为Active。
- ETHERNETPDN类型的组播组成员，状态只显示为Active。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202616189694)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202616189694)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCASTGRPNAME | 组播组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置组播组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63，区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000202616189694)

查询静态组播组成员状态：

```
DSP MCASTGRPMEM: MCASTGRPNAME="group";
```

```

RETCODE = 0  操作成功

组播组成员状态
--------------
组播组名称  成员类型  成员标识    状态

group       IMSI                               1234567748  Inactive
group       IMSI                               123456778   Inactive
group       VTEP                               vtep1       Inactive
group       Ethernet PDN                       1           Active
group       Dual Fed Selective Receiving Pair  1           Inactive
(结果个数 = 5)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000202616189694)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 组播组名称 | 命令查询的组播组的名称。 |
| 成员类型 | 组播组中成员的类型，包括IMSI、VTEP、Dual Fed Selective Receiving Pair、Ethernet PDN四种。 |
| 成员标识 | 组播组中成员的标识，IMSI类型成员标识为IMSI号码，VTEP类型成员标识为VTEP名称，Dual Fed Selective Receiving Pair类型成员标识为结对ID，Ethernet PDN类型成员标识固定为1。 |
| 状态 | 组播组下成员的激活状态，Active为激活状态，Inactive为未激活状态。 |
