# 查询EPRPSTA对象（LST EPRPSTA）

- [命令功能](#ZH-CN_CONCEPT_0295919473__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0295919473__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0295919473__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0295919473__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0295919473__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0295919473__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0295919473)

**适用NF：SGW-U、PGW-U**

该命令用于查询EpRpSta对象。

#### [注意事项](#ZH-CN_CONCEPT_0295919473)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0295919473)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0295919473)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACETYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：接口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SXA：接口类型为Sxa。<br>- SXB：接口类型为Sxb。<br>- SXBGSN：接口类型为Sxb，且用户角色为GGSN。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0295919473)

查询接口类型为SXA的EpRpSta对象：

```
LST EPRPSTA: INTERFACETYPE=SXA;
```

```

RETCODE = 0 操作成功。

EpRpSta 配置
---------------------
              对象名称  =  huawei
              接口类型  =  Sxa
        CP NodeID 类型  =  FQDN
 IPv4地址类型的Node Id  =  0.0.0.0
 IPv6地址类型的Node Id  =  ::
     FQDN类型的Node Id  =  new
(结果个数 = 1)
--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0295919473)

参见ADD EPRPSTA的参数说明。
