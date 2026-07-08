# 查询SA指纹识别协议（LST SUPPFINGERIDEN）

- [命令功能](#ZH-CN_CONCEPT_0000202439608925__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202439608925__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202439608925__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202439608925__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202439608925__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000202439608925__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202439608925)

**适用NF：PGW-U、UPF**

该命令用于显示系统支持的SA指纹识别功能的协议。

#### [注意事项](#ZH-CN_CONCEPT_0000202439608925)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202439608925)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202439608925)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000202439608925)

显示系统支持的所有SA指纹识别功能的协议：

```
LST SUPPFINGERIDEN:;
```

```

RETCODE = 0  操作成功。

支持SA指纹识别协议信息
----------------------
应用子协议名称            应用协议名称

a000dn_data               a000dn       
dolphintunnel             dolphintunnel
facebook_http_video       facebook     
facebook_messenger_im     facebook     
facebook_nonhttp_video    facebook     
facebook_others           facebook     
tor                       tor          
(结果个数 = 7)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000202439608925)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 应用子协议名称 | 用于显示支持SA指纹识别功能的应用子协议名称。 |
| 应用协议名称 | 用于显示支持SA指纹识别功能的应用协议名称。 |
