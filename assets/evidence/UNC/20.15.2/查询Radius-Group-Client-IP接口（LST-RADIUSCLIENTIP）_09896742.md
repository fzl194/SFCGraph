# 查询Radius Group Client IP接口（LST RADIUSCLIENTIP）

- [命令功能](#ZH-CN_CONCEPT_0209896742__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896742__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896742__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896742__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896742__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896742__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896742)

**适用NF：PGW-C、SMF**

LST RADIUSCLIENTIP命令用来查询Radius Group Client IP接口。

#### [注意事项](#ZH-CN_CONCEPT_0209896742)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896742)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896742)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | Radius Server Group名称 | 可选必选说明：可选参数<br>参数含义：指定Radius Server Group名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| AUTHORACCT | 鉴权或计费 | 可选必选说明：可选参数<br>参数含义：指定鉴权或计费。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ACCOUNTING：表示指定的Gi接口的IP地址是计费时的radius client ip。<br>- AUTHENTICATION：表示指定的Gi接口的IP地址是鉴权时的radius client ip。<br>- ACCT_AND_AUTH：表示指定的Gi接口的IP地址既是鉴权时的radius client ip，也是计费时的radius client ip。<br>默认值：无<br>配置原则：<br>- ACCOUNTING：表示计费。<br>- AUTHENTICATION：表示鉴权。<br>- ACCT_AND_AUTH：表示计费和鉴权。 |
| INTFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～13。用户输入形式例如：giif1/0/0。其中giif为逻辑接口类型；1/0/0中第一个数字为组号，第二个数字为实例类型；第三个数字为逻辑接口号，各逻辑接口类型有各自的配置范围。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896742)

如果想要查询Radius Group Client IP接口，应该输入合法的数据，例如：

```
LST RADIUSCLIENTIP:RDSSVRGRPNAME="aaa";
```

```

RETCODE = 0  操作成功。

Radius Server Group接口绑定
---------------------------
Radius Server Group名称  =  aaa
             鉴权或计费  =  计费
               接口名称  =  giif1/0/0
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896742)

参见ADD RADIUSCLIENTIP的参数说明。
