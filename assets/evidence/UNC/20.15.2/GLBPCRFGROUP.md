# 查询全局PCRF组绑定关系（LST GLBPCRFGROUP）

- [命令功能](#ZH-CN_CONCEPT_0209897119__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897119__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897119__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897119__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897119__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897119__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897119)

**适用NF：PGW-C、GGSN**

此命令用来显示PCRF分组和指定的号段绑定关系，以及绑定优先级。

#### [注意事项](#ZH-CN_CONCEPT_0209897119)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897119)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897119)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置绑定的IMSIMSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897119)

查询GLBPCRFGROUP信息：

```
LST GLBPCRFGROUP:;
```

```

RETCODE = 0  操作成功

全局PCRF组绑定关系
------------------
IMSI/MSISDN号段名称  =  ims
         PCRF组名称  =  pcr
             优先级  =  3026
               描述  =  NULL
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897119)

参见ADD GLBPCRFGROUP的参数说明。
