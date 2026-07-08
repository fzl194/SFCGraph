# 设置全局app参数（SET GLBAPPPARA）

- [命令功能](#ZH-CN_CONCEPT_0274982443__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0274982443__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0274982443__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0274982443__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0274982443__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0274982443)

**适用NF：PGW-U、UPF**

该命令用于配置全局的app规格匹配条件。

#### [注意事项](#ZH-CN_CONCEPT_0274982443)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | APPRVALIDCOND |
| --- | --- |
| 初始值 | N4_INDICATION |

#### [操作用户权限](#ZH-CN_CONCEPT_0274982443)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0274982443)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPRVALIDCOND | App规则生效条件 | 可选必选说明：可选参数<br>参数含义：该参数用于配置app规则生效条件。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- N4_INDICATION：根据N4接口下发的Application ID作为app规则的匹配条件。<br>- N4_UNRELATED：不论N4接口是否下发Application ID，均进行app规则匹配。<br>默认值：无<br>配置原则：无 |
| GENERALAPPID | 通用应用标识 | 可选必选说明：可选参数<br>参数含义：该参数定义一个通用的应用标识，是所有app规则的一个统称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 该参数用于和SMF下发的PDR中携带的Application ID进行匹配，当SMF下发的PDR携带的Application ID匹配中当前配置的GeneralAppID的时候，当前所有的app规则都将生效。 |

#### [使用实例](#ZH-CN_CONCEPT_0274982443)

该命令用于设置全局的app规格匹配条件，APPRVALIDCOND设置为N4_INDICATION。使用命令：

```
SET GLBAPPPARA: APPRVALIDCOND=N4_INDICATION;
```
