# 查询整机Trunk Remark配置（LST GLBTRUNKREMARK）

- [命令功能](#ZH-CN_CONCEPT_0000202770522432__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202770522432__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202770522432__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202770522432__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202770522432__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000202770522432__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202770522432)

**适用NF：SGW-U、PGW-U**

该命令用于查询整机所有的Trunk Remark配置。

#### [注意事项](#ZH-CN_CONCEPT_0000202770522432)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202770522432)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202770522432)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000202770522432)

查询整机的Trunk Remark配置：

```
LST GLBTRUNKREMARK:;
```

```

RETCODE = 0  操作成功

宽带集群重标记配置信息
----------------------
QCI  ARP的优先级别  标记类型  DSCP  AF级别  AF丢弃优先级  TOS值  DSCP值  

1    1              TOS       EF    0       0             3      0       
1    2              TOS       EF    0       0             5      0       
(结果个数 = 2)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000202770522432)

参见ADD GLBTRUNKREMARK的参数说明。
