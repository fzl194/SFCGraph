# 查询缺省Acl绑定（LST ACLDEFAULT）

- [命令功能](#ZH-CN_CONCEPT_0182837742__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837742__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837742__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837742__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837742__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837742__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837742)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询默认的ACL。默认ACL是在APN下没有配置任何ACL时，如果APN需要使用ACL，则会使用默认ACL。

#### [注意事项](#ZH-CN_CONCEPT_0182837742)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837742)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837742)

无。

#### [使用实例](#ZH-CN_CONCEPT_0182837742)

假如运营商需要查询系统当前所有的默认ACL：

```
LST ACLDEFAULT:;
```

```

RETCODE = 0  操作成功。

缺省ACL绑定信息
---------------
   方向  =  上行入
ACL名称  =  testacl1
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837742)

参见ADD ACLDEFAULT的参数说明。
