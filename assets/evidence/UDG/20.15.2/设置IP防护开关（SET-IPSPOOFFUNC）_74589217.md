# 设置IP防护开关（SET IPSPOOFFUNC）

- [命令功能](#ZH-CN_CONCEPT_0000201474589217__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201474589217__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201474589217__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201474589217__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201474589217__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000201474589217__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201474589217)

**适用NF：UPF**

设置IP防护开关。

#### [注意事项](#ZH-CN_CONCEPT_0000201474589217)

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ANTISPOOFINGUL | ANTISPOOFINGDL |
| --- | --- | --- |
| 初始值 | ENABLE | ENABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0000201474589217)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201474589217)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ANTISPOOFINGUL | 上行IP防攻击开关 | 可选必选说明：可选参数<br>参数含义：上行IP防攻击开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| ANTISPOOFINGDL | 下行IP防攻击开关 | 可选必选说明：可选参数<br>参数含义：下行IP防攻击开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000201474589217)

假如运营商需要关闭IP防攻击检查，可以通过此命令配置：

```
SET IPSPOOFFUNC: ANTISPOOFINGUL=DISABLE, ANTISPOOFINGDL=DISABLE;
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000201474589217)

参见SET IPSPOOFFUNC的参数说明。
