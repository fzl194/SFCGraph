# 查询Diameter本端信息（LST DIAMLOCINFO）

- [命令功能](#ZH-CN_CONCEPT_0209897274__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897274__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897274__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897274__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897274__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897274__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897274)

**适用NF：PGW-C、SMF**

此命令用来查询Diameter本端信息。

#### [注意事项](#ZH-CN_CONCEPT_0209897274)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897274)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897274)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 本端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897274)

查询HOSTNAME为“test”的Diameter本端信息：

```
LST DIAMLOCINFO: HOSTNAME="test";
```

```

RETCODE = 0  操作成功

Diameter本端主机信息
--------------------
             本端主机名  =  test
               本端域名  =  test
               产品名称  =  product
        Vendor-Id AVP值  =  0
 Firmware-RevisionAVP值  =  1
    Origin-State-Id AVP  =  不使能
Supported-Vendor-Id AVP  =  不使能
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897274)

参见ADD DIAMLOCINFO的参数说明。
