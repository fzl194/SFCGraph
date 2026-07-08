# 查询用户模板组和用户模板的绑定关系（LST UPBINDUPG）

- [命令功能](#ZH-CN_CONCEPT_0209897232__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897232__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897232__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897232__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897232__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897232__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897232)

**适用NF：PGW-C、SMF**

本命令用于查询UsrProfGroup下绑定的UserProfile。

#### [注意事项](#ZH-CN_CONCEPT_0209897232)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897232)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897232)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的USERPROFGNAME必须是系统已经存在的UsrProfGroup对象名称。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897232)

查询UserProfGName为userprofg1的UPBindUPG配置：

```
LST UPBINDUPG:USERPROFGNAME="userprofg1";
```

```

RETCODE = 0  操作成功。

用户模板组与用户模板绑定信息
----------------------------
     用户模板组名称  =  userprofg1
       用户模板名称  =  userprofile
                RAT  =  UTRAN
           漫游属性  =  本地
   计费属性配置模式  =  NULL
           计费属性  =  NULL
       计费属性掩码  =  0xFFFF
IMSI/MSISDN号段名称  =  NULL
     IMEISV号段名称  =  NULL
         位置组名称  =  NULL
             优先级  =  10
           缺省标记  =  0
         位置组名称  =  NULL
   用户模板绑定类型  =  SPECIFIC
 本地PCC策略选择模式 = 继承全局配置
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897232)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 缺省标记 | 用于指定该User Profile是否为默认User Profile。 |

其余输出项请参见ADD UPBINDUPG的参数说明。
