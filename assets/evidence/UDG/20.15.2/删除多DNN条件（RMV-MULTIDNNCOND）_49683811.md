# 删除多DNN条件（RMV MULTIDNNCOND）

- [命令功能](#ZH-CN_CONCEPT_0000206449683811__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206449683811__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206449683811__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206449683811__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206449683811__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206449683811)

**适用NF：UPF**

该命令用于删除多DNN条件。

#### [注意事项](#ZH-CN_CONCEPT_0000206449683811)

该命令执行后对新数据流生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206449683811)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206449683811)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNCONDTYPE | DNN条件类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置DNN名称的条件。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IS：如果DNN名称等于DNNCONDVAL，则匹配中该条件。<br>- STARTS_WITH：如果DNN名称以DNNCONDVAL开始，则匹配中该条件。<br>- ENDS_WITH：如果DNN名称以DNNCONDVAL结束，则匹配中该条件。<br>- CONTAINS：如果DNN名称包含DNNCONDVAL，则匹配中该条件。<br>- ALL_DNN：所有DNN名称均能匹配中该条件。<br>默认值：无<br>配置原则：无 |
| DNNCONDVAL | DNN条件值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DNNCONDTYPE”配置为“STARTS_WITH”、“ENDS_WITH”、“CONTAINS” 或 “IS”时为必选参数。<br>参数含义：该参数用于设置DNN条件值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写, 只能由“-”、数字、大小写字母和“.”组成，不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”。当DNN条件类型为STARTS_WITH或IS时，该值不能以“.”开头。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206449683811)

假如运营商需要删除以“.dnn1”结束的DNN名称：

```
RMV MULTIDNNCOND: DNNCONDTYPE=ENDS_WITH, DNNCONDVAL="dnn1";
```
