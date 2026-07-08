# 查询IP Spoofing攻击告警阈值（LST IPSPOOFALMTHD）

- [命令功能](#ZH-CN_CONCEPT_0182837780__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837780__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837780__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837780__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837780__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837780__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837780)

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询ip spoofing告警产生的条件。

#### [注意事项](#ZH-CN_CONCEPT_0182837780)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837780)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837780)

无。

#### [使用实例](#ZH-CN_CONCEPT_0182837780)

假设运营商需要查看产生ip spoofing告警时：

```
LST IPSPOOFALMTHD:;
```

```

RETCODE = 0  操作成功。

IP Spoofing占用率告警阈值
-------------------------
anti spoofing告警开关  =  使能
             初始阈值  =  1500
             增量阈值  =  1500
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837780)

参见SET IPSPOOFALMTHD的参数说明。
