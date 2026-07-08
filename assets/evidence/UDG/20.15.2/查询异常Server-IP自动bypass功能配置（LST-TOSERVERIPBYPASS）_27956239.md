# 查询异常Server IP自动bypass功能配置（LST TOSERVERIPBYPASS）

- [命令功能](#ZH-CN_CONCEPT_0000207127956239__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000207127956239__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000207127956239__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000207127956239__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000207127956239__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000207127956239__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000207127956239)

**适用NF：UPF**

该命令用于查询异常Server IP自动bypass功能配置。

#### [注意事项](#ZH-CN_CONCEPT_0000207127956239)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000207127956239)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000207127956239)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000207127956239)

查询异常Server IP自动bypass功能配置：

```
LST TOSERVERIPBYPASS:;
```

```

RETCODE = 0  操作成功
 
异常Server IP自动bypass配置
-------------
异常Server IP自动bypass功能开关  =  ENABLE
老化时间（秒） =  86400
异常状态重置为初始状态时间（秒） =  21600
 
(结果个数 = 1)
 
--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000207127956239)

参见SET TOSERVERIPBYPASS的参数说明。
