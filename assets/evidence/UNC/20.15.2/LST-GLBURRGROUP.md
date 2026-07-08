# 查询全局使用量上报规则组（LST GLBURRGROUP）

- [命令功能](#ZH-CN_CONCEPT_0209897189__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897189__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897189__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897189__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897189__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897189__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897189)

**适用NF：PGW-C、SMF**

本条命令用于PDP用户查询全局使用量上报规则组。

#### [注意事项](#ZH-CN_CONCEPT_0209897189)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897189)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897189)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209897189)

查询显示全局使用量上报规则组：

```
LST GLBURRGROUP:;
```

```

RETCODE = 0  操作成功

全局计费属性信息
----------------
上行发起离线URR名称  =  offupurr
下行发起离线URR名称  =  offdnurr
上行发起在线URR名称  =  onupurr
下行发起在线URR名称  =  ondnurr
         不计费标记  =  无
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897189)

参见SET GLBURRGROUP的参数说明。
