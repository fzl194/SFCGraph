# 查询基于SA的Intelligence训练参数（LST SAAITRAINPARA）

- [命令功能](#ZH-CN_CONCEPT_0000201969640518__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201969640518__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201969640518__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201969640518__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201969640518__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000201969640518__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201969640518)

**适用NF：UPF**

该命令用于查询基于SA的intelligence训练参数。

#### [注意事项](#ZH-CN_CONCEPT_0000201969640518)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201969640518)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201969640518)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000201969640518)

如果想查询基于SA的intelligence训练参数，执行以下命令：

```
LST SAAITRAINPARA:;
```

```

RETCODE = 0  操作成功

基于SA的intelligence训练参数
----------------------------
        Intelligence训练阈值  =  9900
        Intelligence训练开关  =  不使能
Intelligence训练周期（分钟）  =  30
      Intelligence训练抽样率  =  0
        SA性能优化库有效时间  =  300
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000201969640518)

参见SET SAAITRAINPARA的参数说明。
