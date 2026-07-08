# 设置COS TOS映射策略（SET COSTOS）

- [命令功能](#ZH-CN_CONCEPT_0182837705__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837705__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837705__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837705__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837705__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837705)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置Cos Tos映射策略。

#### [注意事项](#ZH-CN_CONCEPT_0182837705)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：
- 使用该命令配置参数TOSPOLICY的值为ENABLE时，需要同时配置TunnelMarking功能，参考SET SRVCOMMONPARA命令。

| 参数标识 | TOSPOLICY |
| --- | --- |
| 初始值 | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0182837705)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837705)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TOSPOLICY | TOS策略 | 可选必选说明：必选参数<br>参数含义：该参数用于控制Cos Tos处理策略是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：表示在CoS to ToS映射功能中，接口untrust时的入口报文DSCP处理方式选择，继承报文中DSCP。<br>- ENABLE：表示在CoS to ToS映射功能中，接口untrust时的入口报文DSCP处理方式选择，将报文中的DSCP清为0。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837705)

- 当需要在CoS to ToS映射功能中，接口untrust时的入口报文DSCP处理方式选择，将报文中的DSCP清为0时，使能Cos Tos处理策略：
  ```
  SET COSTOS:TOSPOLICY=ENABLE;
  ```
- 当需要在CoS to ToS映射功能中，接口untrust时的入口报文DSCP处理方式选择，继承报文中DSCP时，不使能Cos Tos处理策略：
  ```
  SET COSTOS:TOSPOLICY=DISABLE;
  ```
