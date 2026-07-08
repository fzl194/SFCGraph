# 设置基于位置区分配地址的开关（SET IPALLOCBYLOCSW）

- [命令功能](#ZH-CN_CONCEPT_0182837160__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837160__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837160__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837160__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837160__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837160)

**适用NF：PGW-U、UPF**

该命令用于配置基于位置区分配地址开关。

#### [注意事项](#ZH-CN_CONCEPT_0182837160)

- 该命令执行后立即生效。
- 该命令最大记录数为9000。
- 开关为INHERIT时，按照基于位置区组分配地址的全局开关的配置进行地址分配，不为INHERIT时，按照基于位置区组分配地址的开关配置进行地址分配。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837160)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837160)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCATIONGRPTYPE | 位置区组类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区组类型。<br>数据来源：本端规划<br>取值范围：枚举类型。只能选取一个选项。<br>- LAC：LAC。<br>- TAC：TAC。<br>默认值：无<br>配置原则：无 |
| LOCATIONGRPNAME | 位置区组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：该位置区组名称必须通过ADD LACGROUP或ADD TACGROUP命令配置过。 |
| SWITCH | IPv4 开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于位置区分配地址的IPv4开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：无 |
| IPV6SWITCH | IPv6 开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于位置区分配地址的IPv6开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837160)

- 允许名为tac1的TAC-Group基于位置区分配地址：
  ```
  SET IPALLOCBYLOCSW: LOCATIONGRPTYPE=TAC, LOCATIONGRPNAME="tac1", SWITCH=DISABLE, IPV6SWITCH=ENABLE;
  ```
- 禁止名为lac1的LAC-Group基于位置区分配地址：
  ```
  SET IPALLOCBYLOCSW: LOCATIONGRPTYPE=LAC, LOCATIONGRPNAME="lac1", SWITCH=ENABLE, IPV6SWITCH=DISABLE;
  ```
