# 删除用户模板的URR组绑定关系（RMV URRGRPBINDING）

- [命令功能](#ZH-CN_CONCEPT_0182837283__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837283__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837283__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837283__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837283__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837283)

**适用NF：PGW-U、UPF**

![](删除用户模板的URR组绑定关系（RMV URRGRPBINDING）_82837283.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除UrrGrpBinding可能会影响业务计费。 删除UrrGrpBinding可能会导致用户激活失败。

该命令用于根据指定名字删除使用量上报规则的绑定。

#### [注意事项](#ZH-CN_CONCEPT_0182837283)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837283)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837283)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及“,”、“;”、“"”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| URRGROUPTYPE | URR组绑定类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定URR组绑定类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SERVICE：业务URR组。<br>- SIGNALING：信令URR组。<br>- TCP：TCP重传URR组。<br>- REDIRECT：重定向URR组。<br>默认值：无<br>配置原则：<br>- SERVICE：设定计费属性绑定类型为业务计费属性。<br>- SIGNALING：设定计费属性绑定类型为信令计费属性。<br>- TCP：设定计费属性绑定类型为TCP重传计费属性。<br>- REDIRECT：设定计费属性绑定类型为重定向计费属性。 |

#### [使用实例](#ZH-CN_CONCEPT_0182837283)

假如运营商希望取消名称为“TestUserProfileName”的用户模板下的信令使用量上报规则：

```
RMV URRGRPBINDING: USERPROFILENAME="TestUserProfileName", URRGROUPTYPE=SIGNALING;
```
