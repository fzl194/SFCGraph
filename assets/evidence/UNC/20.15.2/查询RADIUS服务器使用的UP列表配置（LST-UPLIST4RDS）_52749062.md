# 查询RADIUS服务器使用的UP列表配置（LST UPLIST4RDS）

- [命令功能](#ZH-CN_CONCEPT_0252749062__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0252749062__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0252749062__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0252749062__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0252749062__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0252749062__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0252749062)

**适用NF：PGW-C、SMF**

LST UPLIST4RDS命令用来查询UP列表配置，该UPF列表用于根据UP选择RADIUS服务器发送RADIUS消息。

#### [注意事项](#ZH-CN_CONCEPT_0252749062)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0252749062)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0252749062)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPLISTNAME | UP列表名称 | 可选必选说明：可选参数<br>参数含义：指定UP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。长度1到63的非空格字符串。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0252749062)

显示名为“uplist1”的UP列表下的UP的配置信息：

```
LST UPLIST4RDS: UPLISTNAME="uplist1";
```

```

RETCODE = 0  操作成功

UPF列表信息
-----------
UP列表名称  =  uplist1
UP实例标识  =  up1
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0252749062)

参见ADD UPLIST4RDS的参数说明。
