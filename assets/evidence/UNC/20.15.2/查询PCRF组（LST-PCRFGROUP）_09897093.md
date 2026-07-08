# 查询PCRF组（LST PCRFGROUP）

- [命令功能](#ZH-CN_CONCEPT_0209897093__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897093__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897093__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897093__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897093__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897093__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897093)

**适用NF：PGW-C、GGSN**

此命令用于查询PCRF组宕机备份功能、PCRF组的工作模式。

#### [注意事项](#ZH-CN_CONCEPT_0209897093)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897093)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897093)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCRF组的名字，要求在系统内唯一，数据来源为运营商规划。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897093)

查询PCRFGROUP记录，输入PCRFGRPNAME为“huawei”：

```
LST PCRFGROUP:PCRFGRPNAME="huawei";
```

```

RETCODE = 0  操作成功。

PCRF组信息
----------
    PCRF组名称  =  huawei
  负荷分担模式  =  主备
  宕机备份开关  =  不使能
主用PCRF主机名  =  NULL
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897093)

参见ADD PCRFGROUP、SET MASTERPCRF的参数说明。
