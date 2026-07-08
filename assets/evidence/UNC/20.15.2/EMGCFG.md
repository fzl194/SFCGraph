# 查询运营商紧急呼叫功能配置（LST EMGCFG）

- [命令功能](#ZH-CN_MMLREF_0000001172225187__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225187__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225187__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225187__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225187__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225187__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172225187__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225187)

**适用网元：MME**

该命令用于查询指定MNO/MVNO对应的紧急呼叫配置数据。

#### [注意事项](#ZH-CN_MMLREF_0000001172225187)

- 该命令执行后立即生效。
- 当不输入查询条件时，显示所有记录信息。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225187)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225187)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225187)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：运营商规划<br>取值范围： 0～64，128～254<br>默认值： 无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225187)

不输入查询条件，查询表中全部紧急呼叫配置的数据：

LST EMGCFG:;

```
%%LST EMGCFG:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
                        运营商标识  =  0
                  紧急承载创建模式  =  Only UEs that are authenticated are allowed
                           紧急APN  =  1231
 紧急APN的上行APN AMBR速率(kbit/s)  =  500
 紧急APN的下行APN AMBR速率(kbit/s)  =  500
                     紧急承载的QCI  =  5
                 紧急ARP优先级级别  =  1
   紧急ARP的Pre-emption Capability  =  否
紧急ARP的Pre-emption Vulnerability  =  是
                  紧急P-GW标识类型  =  FQDN
                              FQDN  =  HUAWEI
                        IP地址类型  =  NULL
                          IPV4地址  =  NULL
                          IPV6地址  =  NULL
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172225187)

请参考 [**ADD EMGCFG**](增加运营商紧急呼叫功能配置（ADD EMGCFG）_26305316.md) 命令参数说明。
