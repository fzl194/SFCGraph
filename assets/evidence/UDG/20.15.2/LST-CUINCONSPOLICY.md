# 查询CP和UP关键配置不一致的处理策略（LST CUINCONSPOLICY）

- [命令功能](#ZH-CN_CONCEPT_0264015289__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0264015289__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0264015289__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0264015289__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0264015289__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0264015289__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0264015289)

**适用NF：PGW-U、UPF**

查询SMF/PGW-C和UPF/PGW-U关键配置不一致的处理策略。

#### [注意事项](#ZH-CN_CONCEPT_0264015289)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0264015289)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0264015289)

无。

#### [使用实例](#ZH-CN_CONCEPT_0264015289)

查询SMF/PGW-C和UPF/PGW-U关键配置不一致处理策略：

```
LST CUINCONSPOLICY:;
```

```

RETCODE = 0 操作成功。

CP和UP关键配置不一致策略
------------------------
旁路处理开关 = 使能
(结果个数 = 1)
--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0264015289)

参见SET CUINCONSPOLICY的参数说明。
