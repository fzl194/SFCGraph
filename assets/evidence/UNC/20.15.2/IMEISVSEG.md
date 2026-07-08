# 查询IMEISV号段（LST IMEISVSEG）

- [命令功能](#ZH-CN_CONCEPT_0209897141__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897141__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897141__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897141__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897141__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897141__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897141)

**适用NF：PGW-C、SMF**

该命令用于查询IMEISVSEG号段。

支持批量查询。

#### [注意事项](#ZH-CN_CONCEPT_0209897141)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897141)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897141)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMEISV号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMEISV号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897141)

查询IMEISV号段：

```
LST IMEISVSEG:;
```

```

RETCODE = 0  操作成功

IMEISV号段信息
--------------
    IMEISV号段名称  =  testsegmentname
    IMEISV号段类型  =  IMEI
IMEI号段起始字符串  =  22222222000000
IMEI号段结束字符串  =  22222222999999
  SV号段起始字符串  =  NULL
  SV号段结束字符串  =  NULL
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897141)

参见ADD IMEISVSEG的参数说明。
