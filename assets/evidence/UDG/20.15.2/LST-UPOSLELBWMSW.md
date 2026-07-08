# 查询User Profile操作系统级带宽管理开关（LST UPOSLELBWMSW）

- [命令功能](#ZH-CN_CONCEPT_0182837496__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837496__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837496__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837496__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837496__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837496__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837496)

**适用NF：PGW-U、UPF**

该命令用来查询User Profile操作系统级带宽管理开关。

#### [注意事项](#ZH-CN_CONCEPT_0182837496)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837496)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837496)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | User Profile名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定User Profile名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的USERPROFILENAME必须是系统已经存在的UserProfile对象名称。 |

#### [使用实例](#ZH-CN_CONCEPT_0182837496)

查询名称为“testuserprofile”的User Profile操作系统级带宽管理开关信息：

```
LST UPOSLELBWMSW: USERPROFILENAME="testuserprofile";
```

```

RETCODE = 0 Operation Success.

User Profile OS Level Bandwidth Managament Switch Information
------------------------------------------------------------------------------------------
                                      User Profile = testuserprofile
 User Profile OS Level Bandwidth Managament Switch = INHERIT
(Number of results = 1)
--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837496)

参见SET UPOSLELBWMSW的参数说明。
