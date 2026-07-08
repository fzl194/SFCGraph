# 查询全局计费属性（LST GLBURRGROUP）

- [命令功能](#ZH-CN_CONCEPT_0182837641__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837641__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837641__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837641__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837641__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837641__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837641)

**适用NF：PGW-U、UPF**

本条命令用于查询全局计费属性。

#### [注意事项](#ZH-CN_CONCEPT_0182837641)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837641)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837641)

无。

#### [使用实例](#ZH-CN_CONCEPT_0182837641)

查询显示全局计费属性：

```
LST GLBURRGROUP:;
```

```

RETCODE = 0  操作成功

全局使用量上报规则组信息
------------------------
上行发起URR名称1  =  uponurr
上行发起URR名称2  =  NULL
上行发起URR名称3  =  NULL
下行发起URR名称1  =  dnonurr
下行发起URR名称2  =  NULL
下行发起URR名称3  =  NULL
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837641)

参见SET GLBURRGROUP的参数说明。
