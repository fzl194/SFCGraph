---
id: UNC@20.15.2@MMLCommand@LST SGWCHARACT
type: MMLCommand
name: LST SGWCHARACT（查询S-GW特性对接配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGWCHARACT
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- S11接口管理
- S-GW属性
status: active
---

# LST SGWCHARACT（查询S-GW特性对接配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询MME与S-GW支持能力交互配置策略。

输出结果顺序：

“ALL(所有S-GW)”

“SPECIFIED(指定S-GW)”的IPv4记录

“SPECIFIED(指定S-GW)”的IPv6记录

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWCHARACT]] · S-GW特性对接配置（SGWCHARACT）

## 使用实例

查询MME与S-GW支持特性的能力交互配置策略记录：

LST SGWCHARACT:;

```
%%LST SGWCHARACT:;%%
RETCODE = 0  操作成功。

所有S-GW查询结果如下
--------------------
                              对端设备范围  =  所有S-GW
                          S-GW支持NTSR功能  =  不支持
                           S-GW支持PRN功能  =  不支持
                            S-GW支持MME ID  =  不支持
   S-GW支持Secondary RAT Usage Data Report  =  不支持
                       GTPU IP类型选择策略  =  优先使用IPv4地址
S-GW支持User Location Information For S-GW  =  不支持
              S-GW支持CSR消息携带PSCELL ID  =  不支持
                         S-GW支持PSCell ID  =  不支持
                           S-GW支持PGWRNSI  =  不支持
     S-GW支持P-CSCF Restoration Indication  =  不支持
                                      描述  =  NULL
(结果个数 = 1)

指定S-GW IPv4查询结果如下
-------------------------
对端设备范围    IP地址类型    IPv4地址           IPV4地址掩码    S-GW支持NTSR功能    S-GW支持PRN功能    S-GW支持MME ID    S-GW支持Secondary RAT Usage Data Report    GTPU IP类型选择策略    S-GW支持User Location Information For S-GW    S-GW支持CSR消息携带PSCELL ID    S-GW支持PSCell ID    S-GW支持PGWRNSI    S-GW支持P-CSCF Restoration Indication    描述

指定S-GW        IPV4         10.141.149.100     255.0.0.0      不支持              不支持             不支持           不支持                                      优先使用IPv4地址       不支持                                        不支持                         不支持               不支持              不支持                                   NULL
指定S-GW        IPV4         10.141.149.180     255.255.0.0    不支持              不支持             不支持           不支持                                      优先使用IPv4地址       不支持                                        不支持                         不支持               不支持              不支持                                   NULL
指定S-GW        IPV4         10.141.149.190     255.255.0.0    不支持              不支持             不支持           不支持                                      优先使用IPv4地址       不支持                                        不支持                         不支持               不支持              不支持                                   NULL
(结果个数 = 3)

指定S-GW IPv6查询结果如下
-------------------------
对端设备范围    IP地址类型    IPv6地址                       IPV6地址前缀长度    S-GW支持NTSR功能    S-GW支持PRN功能    S-GW支持MME ID    S-GW支持Secondary RAT Usage Data Report    GTPU IP类型选择策略    S-GW支持User Location Information For S-GW    S-GW支持CSR消息携带PSCELL ID    S-GW支持PSCell ID    S-GW支持PGWRNSI    S-GW支持P-CSCF Restoration Indication    描述

指定S-GW        IPV6         2001:db8:10:19:44:55:10:12     128                不支持              不支持             不支持           不支持                                     优先使用IPv6地址       不支持                                        不支持                          不支持                不支持             不支持                                   NULL
指定S-GW        IPV6         2001:db8:10:19:44:55:10:15     128                不支持              不支持             不支持           不支持                                     优先使用IPv6地址       不支持                                        不支持                          不支持                不支持             不支持                                   NULL
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SGWCHARACT.md`
