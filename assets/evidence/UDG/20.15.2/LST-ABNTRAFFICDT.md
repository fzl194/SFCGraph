# 查询异常流量功能开关（LST ABNTRAFFICDT）

- [命令功能](#ZH-CN_CONCEPT_0186526441__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186526441__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186526441__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186526441__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186526441__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0186526441__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0186526441)

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询APN下终端异常下行流量检测开关信息。

#### [注意事项](#ZH-CN_CONCEPT_0186526441)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0186526441)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186526441)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该APN必须是系统已经配置的APN，此功能不支持别名APN的配置使能。 |

#### [使用实例](#ZH-CN_CONCEPT_0186526441)

查询名称为“apn1.com”的APN的终端异常下行流量检测功能的开关信息：

```
LST ABNTRAFFICDT: APN="apn1.com";
```

```

RETCODE = 0  Operation succeeded

Abnormal Traffic Detect Switch
------------------------------
                          APN  =  apn1.com
                       Switch  =  ENABLE
Traffic Behavior Based Switch  =  ENABLE
(Number of results = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0186526441)

参见ADD ABNTRAFFICDT的参数说明。
