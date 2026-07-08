# 查询AMF N26消息抄送路径（LST AMFN26CPPATH）

- [命令功能](#ZH-CN_CONCEPT_0000001629829116__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001629829116__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001629829116__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001629829116__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001629829116__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001629829116__1.3.6.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001629829116__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001629829116)

**适用网元：MME、AMF**

该命令用于查询AMF N26消息抄送路径相关的参数。

#### [注意事项](#ZH-CN_CONCEPT_0000001629829116)

无。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001629829116)

manage-ug；system-ug；monitor-ug。

#### [网管用户权限](#ZH-CN_CONCEPT_0000001629829116)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组。

#### [参数说明](#ZH-CN_CONCEPT_0000001629829116)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000001629829116)

查询AMF N26消息抄送路径：

LST AMFN26CPPATH:;

```
%%LST AMFN26CPPATH:;%%
RETCODE = 0  操作成功

输出结果如下
------------------------
        抄送路径开关  =  打开
          IP地址类型  =  IPV4类型
       MME侧IPv4地址  =  192.168.1.1
       MME侧IPv6地址  =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
       AMF侧IPv4地址  =  192.168.2.2
       AMF侧IPv6地址  =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
             VPN名称  =  _abc_
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001629829116)

参见 [SET AMFN26CPPATH](设置AMF N26消息抄送路径（SET AMFN26CPPATH）_30308792.md) 的参数说明。
