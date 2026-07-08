# 查询知名端口（LST WELLKNOWNPORT）

- [命令功能](#ZH-CN_CONCEPT_0182837335__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837335__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837335__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837335__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837335__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837335__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837335)

**适用NF：PGW-U、UPF**

LST WELLKNOWNPORT此命令用来查询指定知名端口或所有知名端口。

#### [注意事项](#ZH-CN_CONCEPT_0182837335)

输入IdenProtName查询匹配记录，不输入IdenProtName查询所有记录。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837335)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837335)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDENPROTNAME | 知名端口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定指知名端口名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837335)

查询WELLKNOWNPORT记录，IDENPROTNAME为huawei：

```
LST WELLKNOWNPORT:IDENPROTNAME="huawei";
```

```

RETCODE = 0  操作成功

知名端口信息
------------
  知名端口名称  =  huawei
      协议名称  =  http
端口范围操作码  =  范围
    起始端口号  =  1000
    结束端口号  =  3000
        优先级  =  100
    配置域名称  =  NULL
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837335)

参见ADD WELLKNOWNPORT的参数说明。
