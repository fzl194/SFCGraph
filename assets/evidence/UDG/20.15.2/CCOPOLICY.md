# 设置CCO策略（SET CCOPOLICY）

- [命令功能](#ZH-CN_CONCEPT_0000205344536221__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000205344536221__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000205344536221__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000205344536221__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000205344536221__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000205344536221)

**适用NF：UPF**

本条命令用于设置CCO拥塞控制策略开关。

#### [注意事项](#ZH-CN_CONCEPT_0000205344536221)

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | BWMCAR | BWMSHAPING | EFLOWTHROTTLE | TOPLY |
| --- | --- | --- | --- | --- |
| 初始值 | ENABLE | ENABLE | DISABLE | ENABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0000205344536221)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000205344536221)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BWMCAR | BWMCAR策略开关 | 可选必选说明：可选参数<br>参数含义：BWMCAR策略开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：ENABLE<br>配置原则：无 |
| BWMSHAPING | BWMSHAPING策略开关 | 可选必选说明：可选参数<br>参数含义：BWMSHAPING策略开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：ENABLE<br>配置原则：无 |
| EFLOWTHROTTLE | 大象流抑制策略开关 | 可选必选说明：可选参数<br>参数含义：大象流抑制策略开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：无 |
| TOPLY | TO分流策略开关 | 可选必选说明：可选参数<br>参数含义：TO分流策略开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：ENABLE<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000205344536221)

用户可以设置某种CCO拥塞控制策略是否生效; 例如：设置BWMCAR策略为可用，BWMSHAPING策略为可用，EFLOWTHROTTLE策略为不可用，TO策略为可用。

```
SET CCOPOLICY: BWMCAR=ENABLE, BWMSHAPING=ENABLE, EFLOWTHROTTLE=DISABLE, TOPLY=ENABLE;
```
