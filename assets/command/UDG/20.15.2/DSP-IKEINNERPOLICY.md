---
id: UDG@20.15.2@MMLCommand@DSP IKEINNERPOLICY
type: MMLCommand
name: DSP IKEINNERPOLICY（显示IKE内部负载分担策略信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IKEINNERPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- 操作维护
- 系统调测
- IPsec调测
- IKE内部策略信息
status: active
---

# DSP IKEINNERPOLICY（显示IKE内部负载分担策略信息）

## 功能

该命令用于显示IKE内部负载分担策略信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TULNAME | 隧道名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询内部策略关联的隧道名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IKEINNERPOLICY]] · IKE内部负载分担策略信息（IKEINNERPOLICY）

## 使用实例

显示与隧道名称为“Tunnel27”的隧道接口相关的IKE内部负载分担策略信息

```
DSP IKEINNERPOLICY: TULNAME="Tunnel27";
RETCODE = 0  操作成功

结果如下
------------------------
           隧道名  =  Tunnel27
         隧道标识  =  1
            VPN名  =  NULL
          VPN标识  =  0
         Policy名  =  ipsecply27
     Policy序列号  =  1
       Proposal名  =  ipsecpsl27
     Proposal标识  =  27
           Peer名  =  env27
       Peer优先级  =  1
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-IKEINNERPOLICY.md`
