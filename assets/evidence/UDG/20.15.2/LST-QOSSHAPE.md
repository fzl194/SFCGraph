# 查询QosShape配置（LST QOSSHAPE）

- [命令功能](#ZH-CN_CONCEPT_0182837672__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837672__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837672__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837672__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837672__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837672__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837672)

**适用NF：UPF**

该命令用于查询用户上下行shaping功能的全局开关。

#### [注意事项](#ZH-CN_CONCEPT_0182837672)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837672)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837672)

无。

#### [使用实例](#ZH-CN_CONCEPT_0182837672)

查询全局的QosShape功能开关：

```
LST QOSSHAPE:;
```

```

RETCODE = 0  操作成功。

QosShape配置信息
----------------
用户漫游类型    上行RAT类型    下行RAT类型

本地            NULL           NULL       
漫游            NULL           NULL       
拜访            NULL           NULL       
(结果个数 = 3)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837672)

参见SET QOSSHAPE的参数说明。
