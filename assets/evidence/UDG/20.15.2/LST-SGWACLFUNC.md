# 查询SGW ACL功能（LST SGWACLFUNC）

- [命令功能](#ZH-CN_CONCEPT_0182837745__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837745__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837745__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837745__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837745__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837745__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837745)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询SGW\I-UPF\ULCL\BP上ACL功能是否使能。

#### [注意事项](#ZH-CN_CONCEPT_0182837745)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837745)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837745)

无。

#### [使用实例](#ZH-CN_CONCEPT_0182837745)

查询是否使能SGW\I-UPF\ULCL\BP上ACL功能：

```
LST SGWACLFUNC:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
S-GW ACL功能  =  使能
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837745)

参见SET SGWACLFUNC的参数说明。
