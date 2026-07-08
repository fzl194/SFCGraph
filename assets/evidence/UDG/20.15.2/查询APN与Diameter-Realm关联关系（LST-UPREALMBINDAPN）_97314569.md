# 查询APN与Diameter Realm关联关系（LST UPREALMBINDAPN）

- [命令功能](#ZH-CN_CONCEPT_0000206297314569__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206297314569__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206297314569__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206297314569__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206297314569__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000206297314569__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206297314569)

**适用NF：UPF**

该命令用于查询Diameter域与APN的绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0000206297314569)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206297314569)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206297314569)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要与Diameter域绑定的APN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206297314569)

查询APN isp与Diameter域的绑定关系：

```
LST UPREALMBINDAPN: APN="isp";
```

```

RETCODE = 0  操作成功
APN与Diameter Realm关联关系
---------------------------
                       APN名称  =  isp
                  Diameter应用  =  SWM
   根据IMSI构造归属地Realm开关  =  使能
                       Realm名  =  NULL
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000206297314569)

参见ADD UPREALMBINDAPN的参数说明。
