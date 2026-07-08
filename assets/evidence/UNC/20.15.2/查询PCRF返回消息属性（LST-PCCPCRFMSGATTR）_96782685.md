# 查询PCRF返回消息属性（LST PCCPCRFMSGATTR）

- [命令功能](#ZH-CN_CONCEPT_0296782685__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0296782685__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0296782685__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0296782685__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0296782685__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0296782685__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0296782685)

**适用NF：PGW-C、SMF**

该命令用于查询PCRF返回消息属性的配置。

#### [注意事项](#ZH-CN_CONCEPT_0296782685)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0296782685)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0296782685)

无。

#### [使用实例](#ZH-CN_CONCEPT_0296782685)

查询PCRF返回消息属性的配置：

```
LST PCCPCRFMSGATTR:;
```

```

RETCODE = 0  操作成功

PCRF消息属性信息
----------------
基于CCA-U Origin-Host AVP触发PCRF重选  =  禁止
  基于RAR Origin-Host AVP触发PCRF重选  =  禁止
基于CCA-I Origin-Host AVP触发PCRF重选  =  禁止
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0296782685)

参见SET PCCPCRFMSGATTR的参数说明。
