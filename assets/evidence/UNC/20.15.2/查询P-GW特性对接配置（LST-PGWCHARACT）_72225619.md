# 查询P-GW特性对接配置（LST PGWCHARACT）

- [命令功能](#ZH-CN_CONCEPT_0000001172225619__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001172225619__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001172225619__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001172225619__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001172225619__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001172225619__1.3.6.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001172225619__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001172225619)

**适用网元：SGSN、MME**

该命令用于查询需要匹配的对端P-GW的属性信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001172225619)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001172225619)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0000001172225619)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001172225619)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000001172225619)

1. 查询所有记录：
  LST PGWCHARACT:;

  ```
  %%LST PGWCHARACT:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
                           对端设备范围  =  指定IP的P-GW
                             IP地址类型  =  IPv4
                               IPv4地址  =  10.141.196.197
                           IPv4地址掩码  =  255.255.255.0
                         P-GW支持MME ID  =  不支持
      是否向P-GW转发LTE-M类型的RAT TYPE  =  不支持
  P-GW支持P-CSCF Restoration Indication  =  不支持
  仍有后续报告输出
  ---    END
  %%LST PGWCHARACT:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
                           对端设备范围  =  指定IP的P-GW
                             IP地址类型  =  IPv6
                               IPv6地址  =  2001:db8:10:19:44:55:10:12
                       IPv6地址前缀长度  =  120
                         P-GW支持MME ID  =  不支持
      是否向P-GW转发LTE-M类型的RAT TYPE  =  不支持
  P-GW支持P-CSCF Restoration Indication  =  不支持
  (结果个数 = 2)
  共有2个报告
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001172225619)

参数说明参考 [**ADD PGWCHARACT**](增加P-GW特性对接配置（ADD PGWCHARACT）_26305748.md) 命令。
