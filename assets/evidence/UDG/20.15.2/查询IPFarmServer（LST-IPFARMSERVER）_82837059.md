# 查询IPFarmServer（LST IPFARMSERVER）

- [命令功能](#ZH-CN_CONCEPT_0182837059__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837059__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837059__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837059__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837059__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837059__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837059)

**适用NF：PGW-U、UPF**

该命令用于显示该IP farm服务器所在的IP farm中的所有IP farm服务器信息。

#### [注意事项](#ZH-CN_CONCEPT_0182837059)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837059)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837059)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPFARMNAME | IP-Farm名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IP farm名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837059)

查询一个IP farm下的全部服务器：

```
LST IPFARMSERVER:;
```

```

RETCODE = 0  操作成功。

IPFarmServer信息
----------------
       IP-Farm名称  =  test
          地址信息  =  10.0.0.1
               URL  =  www.huawei.com
    重定向缺省动作  =  BLOCK
重定向携带信息名称  =  test
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837059)

参见ADD IPFARMSERVER的参数说明。
