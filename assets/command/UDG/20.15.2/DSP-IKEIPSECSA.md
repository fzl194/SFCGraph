---
id: UDG@20.15.2@MMLCommand@DSP IKEIPSECSA
type: MMLCommand
name: DSP IKEIPSECSA（显示IKE IPsec安全联盟）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IKEIPSECSA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IKE IPsec安全联盟
status: active
---

# DSP IKEIPSECSA（显示IKE IPsec安全联盟）

## 功能

该命令用于显示IKE IPsec安全联盟。

> **说明**
> - 该命令执行后立即生效。
> - 该命令在有大量智家随行业务的家庭网关在线时，如果查询全量的IKE IPsec安全联盟，可能存在链路过多查询失败的风险。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：IPsec策略的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~15。<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IKEIPSECSA]] · IPSEC安全联盟（IKEIPSECSA）

## 使用实例

显示IKE IPsec安全联盟

```
DSP IKEIPSECSA:;
RETCODE = 0  操作成功

结果如下
--------
                        接口名称  =  Tunnel37
                        策略名称  =  ipsecply37
                         POD名称  =  ipsecexec-pod-0192-168-1-1
                     VPN实例名称  =  _public_
                          序列号  =  1
                          实例ID  =  0
                        策略模式  =  ISAKMP模式
               入方向VPN实例名称  =  _public_
               出方向VPN实例名称  =  _public_
                          连接ID  =  788529152
                     ACL规则编号  =  3037
                        封装模式  =  隧道模式
                        地址类型  =  IPv4地址
                    隧道本端地址  =  10.1.1.1
                    隧道远端地址  =  10.1.1.2
                    源流起始地址  =  10.10.1.1
                源IPv4地址反掩码  =  0.0.0.0
                  目的流起始地址  =  10.10.1.2
              目的IPv4地址反掩码  =  0.0.0.0
                隧道本端地址IPV6  =  ::
                隧道远端地址IPV6  =  ::
                源流起始地址IPV6  =  ::
                源IPv6地址正掩码  =  0
              目的流起始地址IPV6  =  ::
              目的IPv6地址正掩码  =  0
                         源流PID  =  0
                          源流SP  =  0
                         源流SEP  =  0
                       目的流PID  =  0
                        目的流DP  =  0
                       目的流DEP  =  0
                  入方向AH SA ID  =  0
                 入方向ESP SA ID  =  1874311275
                  出方向AH SA ID  =  0
                 出方向ESP SA ID  =  2304413776
             入方向AH SA创建时间  =  NULL
            入方向AH安全参数索引  =  0
    十六进制入方向AH安全参数索引  =  NULL
                    入方向AH提议  =  NULL
 入方向AH SA剩余密钥长度(单位KB)  =  0
 入方向AH SA剩余密钥长度(单位秒)  =  0
              入方向AH最大序列号  =  0
                入方向AH UDP封装  =  NULL
             出方向AH SA创建时间  =  NULL
            出方向AH安全参数索引  =  0
                    出方向AH提议  =  NULL
              出方向AH最大序列号  =  0
    十六进制出方向AH安全参数索引  =  NULL
 出方向AH SA剩余密钥长度(单位KB)  =  0
 出方向AH SA剩余密钥长度(单位秒)  =  0
                出方向AH UDP封装  =  NULL
            出方向ESP SA创建时间  =  2021-12-22 09:08:45
           出方向ESP安全参数索引  =  2304413776
                   出方向ESP提议  =  ESP-ENCRYPT-256-AES ESP-AUTH-SHA2-256
             出方向ESP最大序列号  =  0
   十六进制出方向ESP安全参数索引  =  895a9050
出方向ESP SA剩余密钥长度(单位KB)  =  1843200
出方向ESP SA剩余密钥长度(单位秒)  =  1558
               出方向ESP UDP封装  =  N
            入方向ESP SA创建时间  =  2021-12-22 09:08:45
           入方向ESP安全参数索引  =  1874311275
                   入方向ESP提议  =  ESP-ENCRYPT-256-AES ESP-AUTH-SHA2-256
             入方向ESP最大序列号  =  0
   十六进制入方向ESP安全参数索引  =  6fb7b86b
入方向ESP SA剩余密钥长度(单位KB)  =  1843200
入方向ESP SA剩余密钥长度(单位秒)  =  1558
               入方向ESP UDP封装  =  N
        显示全局持续长度(单位KB)  =  0
        显示全局持续长度(单位秒)  =  3600
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示IKE-IPsec安全联盟（DSP-IKEIPSECSA）_80910988.md`
