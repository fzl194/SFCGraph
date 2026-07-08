# 设置PDN自动探测功能开关（SET PDNAUTOTSTSW）

- [命令功能](#ZH-CN_CONCEPT_0000206312635692__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206312635692__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206312635692__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206312635692__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206312635692__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206312635692)

**适用NF：PGW-U、UPF**

设置PDN自动探测功能开关。

#### [注意事项](#ZH-CN_CONCEPT_0000206312635692)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH | DNSKPIFTSW | FAULTTRACERTSW |
| --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0000206312635692)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206312635692)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | PDN侧路由自动探测开关 | 可选必选说明：必选参数<br>参数含义：PDN侧自动探测开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| DNSKPIFTSW | DNS KPI故障自动探测开关 | 可选必选说明：可选参数<br>参数含义：DNS KPI故障自动探测开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：无 |
| FAULTTRACERTSW | 路径故障Tracert开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DNSKPIFTSW”配置为“ENABLE”时为可选参数。<br>参数含义：路径故障Tracert开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206312635692)

- 打开PDN自动探测功能开关：
  ```
  SET PDNAUTOTSTSW:SWITCH="ENABLE";
  ```
- 打开KPI异常检测开关：
  ```
  SET PDNAUTOTSTSW:SWITCH="ENABLE", DNSKPIFTSW="ENABLE";
  ```
- 打开路径故障自动探测开关：
  ```
  SET PDNAUTOTSTSW:SWITCH="ENABLE", FAULTTRACERTSW="ENABLE";
  ```
