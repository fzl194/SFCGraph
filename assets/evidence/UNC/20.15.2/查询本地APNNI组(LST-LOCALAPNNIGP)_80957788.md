# 查询本地APNNI组(LST LOCALAPNNIGP)

- [命令功能](#ZH-CN_TOPIC_0000002180957788__1.3.1.1)
- [注意事项](#ZH-CN_TOPIC_0000002180957788__1.3.2.1)
- [本地用户权限](#ZH-CN_TOPIC_0000002180957788__1.3.3.1)
- [网管用户权限](#ZH-CN_TOPIC_0000002180957788__1.3.4.1)
- [参数说明](#ZH-CN_TOPIC_0000002180957788__1.3.5.1)
- [使用实例](#ZH-CN_TOPIC_0000002180957788__1.3.6.1)
- [输出结果说明](#ZH-CN_TOPIC_0000002180957788__1.3.9.1)

#### [命令功能](#ZH-CN_TOPIC_0000002180957788)

**适用网元：SGSN**

该命令用于查询本地APNNI组信息。定制APN纠正功能会引用该配置参数APNNIGRPID，可参考 **[ADD SMACTCTRL](../激活过程管理/增加激活过程控制参数（ADD SMACTCTRL）_26305472.md)** 命令的APNNIGRPID参数说明。

#### [注意事项](#ZH-CN_TOPIC_0000002180957788)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_TOPIC_0000002180957788)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_TOPIC_0000002180957788)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_TOPIC_0000002180957788)

无。

#### [使用实例](#ZH-CN_TOPIC_0000002180957788)

查询LOCALAPNNI组信息。

LST LOCALAPNNIGP:;

```
%%LST LOCALAPNNIGP:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
本地APNNI组号  =  1
        APNNI  =  HUAWEI1.COM
  APNNI优先级  =  1
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_TOPIC_0000002180957788)

请参考 **[ADD LOCALAPNNIGP](增加本地APNNI组(ADD LOCALAPNNIGP)_16438089.md)** 命令的参数说明。
