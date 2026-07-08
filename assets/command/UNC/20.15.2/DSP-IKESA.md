---
id: UNC@20.15.2@MMLCommand@DSP IKESA
type: MMLCommand
name: DSP IKESA（显示IKE安全联盟）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IKESA
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IKE安全联盟
status: active
---

# DSP IKESA（显示IKE安全联盟）

## 功能

该命令用于显示IKE安全联盟。

## 注意事项

- 该命令执行后立即生效。
- 该命令在有大量智家随行业务的家庭网关在线时，如果查询全量的IKE安全联盟，可能存在链路过多查询失败的风险。
- 由于用户级IPSEC链路只支持被动响应协商，查询结果中用户级链路的“剩余SA长度”字段为0。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REMOTEADDRESS | 远端地址 | 可选必选说明：可选参数<br>参数含义：IPsec策略远端地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| REMOTEADDRESS6 | 远端地址IPV6 | 可选必选说明：可选参数<br>参数含义：IPsec策略IPV6远端地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IKE安全联盟（IKESA）](configobject/UNC/20.15.2/IKESA.md)

## 使用实例

显示IKE安全联盟：

```
DSP IKESA:;
RETCODE = 0  操作成功

结果如下
--------
         地址类型  =  IPv4地址
         远端地址  =  10.1.1.2
     远端地址IPV6  =  ::
          POD名称  =  ipsecexec-pod-0192-168-1-1
           连接ID  =  46
           SA标记  =  RD|ST
           实例ID  =  46
             阶段  =  1
         本端地址  =  10.1.1.1
     本端地址IPV6  =  ::
     触发端Cookie  =  e3a8e1bb615e3e8c
     回应端Cookie  =  ba946bbfc7e3af8c
         接口名称  =  Tunnel37
         认证方法  =  预共享
         认证算法  =  sha2-256算法
         加密算法  =  256位AES算法
       完整性算法  =  sha2-256算法
             DH组  =  DH组14
       剩余SA长度  =  48267
       是否已备份  =  否
       SA建立时间  =  2021-12-22 09:08:45
    IKE对等体名称  =  env37_peer
          IKE版本  =  版本2
    流VPN实例名称  =  _public_
对等体VPN实例名称  =  _public_
              Ext  =  NULL
     发送消息计数  =  0
     接收消息计数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示IKE安全联盟（DSP-IKESA）_25912245.md`
