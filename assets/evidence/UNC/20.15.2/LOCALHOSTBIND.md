# 查询Diameter本端主机与Diameter本端主机组的关联关系（LST LOCALHOSTBIND）

- [命令功能](#ZH-CN_CONCEPT_0000201616858411__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201616858411__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201616858411__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201616858411__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201616858411__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000201616858411__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201616858411)

**适用NF：PGW-C、SMF**

此命令用于查询Diameter本端主机与Diameter本端主机组的绑定信息。

#### [注意事项](#ZH-CN_CONCEPT_0000201616858411)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201616858411)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201616858411)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCGRPNAME | Diameter本端信息组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter本端主机组名。要求在系统内唯一，数据来源为运营商规划。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000201616858411)

查询Diameter本端主机与Diameter本端主机组的关联关系，被查询的Diameter本端主机组名为“abc”：

```
LST LOCALHOSTBIND: LOCGRPNAME="abc";
```

```

RETCODE = 0 操作成功。

Diameter本端主机组内的Diameter主机信息
--------------------------------------
Diameter本端信息组名  =  abc
  Diameter本端主机名  =  aaa
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000201616858411)

参见ADD LOCALHOSTBIND的参数说明。
