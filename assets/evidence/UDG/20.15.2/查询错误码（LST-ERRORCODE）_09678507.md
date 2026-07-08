# 查询错误码（LST ERRORCODE）

- [命令功能](#ZH-CN_CONCEPT_0209678507__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209678507__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209678507__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209678507__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209678507__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209678507__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209678507)

**适用NF：PGW-U、UPF**

此命令用于显示配置错误码信息。

#### [注意事项](#ZH-CN_CONCEPT_0209678507)

- 该命令执行后立即生效。
- 输入ERRORCODENAME查询指定记录，如果不输入ERRORCODENAME表示查询所有记录。

#### [操作用户权限](#ZH-CN_CONCEPT_0209678507)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209678507)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ERRORCODENAME | 错误码名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置错误码配置名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209678507)

查询所有错误码：

```
LST ERRORCODE:;
```

```

%%LST ERRORCODE:;%%
RETCODE = 0  Operation succeeded

Error Code
----------
Error Code Name  Error Code Range Operation  Error Code Start Value  Error Code End Value  

e1               Less Than or Equal To       0                       10                    
testerrorcode    Less Than or Equal To       0                       5                     
(Number of results = 2)
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209678507)

参见ADD ERRORCODE的参数说明。
