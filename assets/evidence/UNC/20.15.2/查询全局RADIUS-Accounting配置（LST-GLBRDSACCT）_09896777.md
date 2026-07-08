# 查询全局RADIUS Accounting配置（LST GLBRDSACCT）

- [命令功能](#ZH-CN_CONCEPT_0209896777__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896777__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896777__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896777__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896777__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896777__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896777)

**适用NF：PGW-C、SMF**

LST GLBRDSACCT命令用来显示全局Radius计费配置的信息。

#### [注意事项](#ZH-CN_CONCEPT_0209896777)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896777)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896777)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209896777)

查询全局RADIUS Accounting配置：

```
LST GLBRDSACCT:;
```

```

RETCODE = 0  操作成功。

全局AAA计费配置
---------------
  发送RADIUS Accounting On/Off消息附加次数  =  1
每秒钟尝试发送Accounting Start消息的用户数  =  10
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896777)

参见SET GLBRDSACCT的参数说明。
