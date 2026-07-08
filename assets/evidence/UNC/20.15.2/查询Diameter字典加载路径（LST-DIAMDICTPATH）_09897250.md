# 查询Diameter字典加载路径（LST DIAMDICTPATH）

- [命令功能](#ZH-CN_CONCEPT_0209897250__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897250__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897250__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897250__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897250__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897250__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897250)

**适用NF：PGW-C、SMF**

该命令用于查询Diameter字典加载路径。

#### [注意事项](#ZH-CN_CONCEPT_0209897250)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897250)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897250)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209897250)

当需要查询当前配置的Diameter字典加载路径时：

```
LST DIAMDICTPATH:;
```

```

RETCODE = 0  操作成功

Diameter字典加载路径
--------------------
应用  字典序号  字典加载路径     

Gy    1         EPC标准字典路径  
Gy    2         定制字典路径2    
Gx    1         定制字典路径1    
S6b   1         EPC标准字典路径  
(结果个数 = 4)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897250)

参见ADD DIAMDICTPATH的参数说明。
