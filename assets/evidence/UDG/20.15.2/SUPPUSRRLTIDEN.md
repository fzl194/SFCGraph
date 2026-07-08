# 查询支持用户关联识别协议（LST SUPPUSRRLTIDEN）

- [命令功能](#ZH-CN_CONCEPT_0182837438__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837438__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837438__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837438__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837438__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837438__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837438)

**适用NF：PGW-U、UPF**

该命令用于查询支持用户关联识别功能的协议列表。在配置用户关联识别功能时，运营商需要查询支持该功能的协议时执行该命令。

#### [注意事项](#ZH-CN_CONCEPT_0182837438)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837438)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837438)

无。

#### [使用实例](#ZH-CN_CONCEPT_0182837438)

显示所有支持用户关联识别的协议：

```
LST SUPPUSRRLTIDEN:;
```

```

RETCODE = 0  操作成功。

支持用户关联识别协议信息
------------------------
子协议名称                 应用协议名称           

facebook_messenger_voip    facebook_messenger_voip
facebook_others            facebook               
niantic_data               niantic                
pokemongo_data             pokemongo              
(结果个数 = 4)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837438)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 子协议名称 | 用于设置对应的子协议名称。 |
| 应用协议名称 | 用于设置对应的应用协议名称。 |
