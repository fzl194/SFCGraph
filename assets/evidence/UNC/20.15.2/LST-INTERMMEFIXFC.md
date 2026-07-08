# 查询Inter-MME接入固定速率流控功能相关参数(LST INTERMMEFIXFC)

- [命令功能](#ZH-CN_CONCEPT_0000001357365241__1.4.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001357365241__1.4.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001357365241__1.4.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001357365241__1.4.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001357365241__1.4.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001357365241__1.4.6.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001357365241__1.4.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001357365241)

**适用网元：MME**

该命令用于查询Inter-MME接入固定速率流控功能的相关参数。

#### [注意事项](#ZH-CN_CONCEPT_0000001357365241)

无。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001357365241)

manage-ug;system-ug;monitor-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0000001357365241)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001357365241)

无

#### [使用实例](#ZH-CN_CONCEPT_0000001357365241)

查询Inter-MME接入固定速率流控功能的相关参数：

```
LST INTERMMEFIXFC:;
```

```
查询结果如下
-------------------------
                      流控粒度   =  单进程
         Attach接入流控功能开关  =  关闭
 Attach Request流控阈值作用范围  =  单进程
  Attach Request速率门限(个/秒)  =  4080
             SR接入流控功能开关  =  关闭
Service Request流控阈值作用范围  =  单进程
 Service Request速率门限(个/秒)  =  4080
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001357365241)

参见 [SET INTERMMEFIXFC](设置Inter-MME接入固定速率流控功能相关参数(SET INTERMMEFIXFC)_04085540.md) 的参数说明。
