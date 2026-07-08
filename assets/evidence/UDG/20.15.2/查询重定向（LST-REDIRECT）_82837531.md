# 查询重定向（LST REDIRECT）

- [命令功能](#ZH-CN_CONCEPT_0182837531__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837531__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837531__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837531__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837531__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837531__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837531)

**适用NF：PGW-U、UPF**

此命令用于运营商查询已经配置的URL重定向策略，可以查询重定向携带信息名称等。

#### [注意事项](#ZH-CN_CONCEPT_0182837531)

输入REDIRECTNAME查询指定记录，如果不输入REDIRECTNAME表示查询所有记录。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837531)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837531)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REDIRECTNAME | 重定向名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置重定向配置名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837531)

查询名为testredirect2的URL重定向策略：

```
LST REDIRECT:REDIRECTNAME="testredirect2";
```

```

RETCODE = 0  操作成功。

重定向信息
----------
        重定向名称  =  testredirect2
               URL  =  www.huawei.com
          流控标识  =  不使能
流控时间间隔（秒）  =  5
    重定向缺省动作  =  BLOCK
重定向携带信息名称  =  test
        配置域名称  =  NULL
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837531)

参见ADD REDIRECT的参数说明。
