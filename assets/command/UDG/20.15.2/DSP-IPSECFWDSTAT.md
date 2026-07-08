---
id: UDG@20.15.2@MMLCommand@DSP IPSECFWDSTAT
type: MMLCommand
name: DSP IPSECFWDSTAT（显示IPsec转发统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IPSECFWDSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- 操作维护
- 系统调测
- IPsec调测
- 转发统计信息
status: active
---

# DSP IPSECFWDSTAT（显示IPsec转发统计）

## 功能

该命令用于显示IPSEC转发统计。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |
| QRYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：查询类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（查询该IPSEC pod的流量情况，PODNAME为空就查询所有IPSEC pod的流量情况。）<br>- QRYBYPEER（查询该对等体的流量情况）<br>默认值：无<br>配置原则：无 |
| PEERNAME | Peer名称 | 可选必选说明：该参数在"QRYTYPE"配置为"QRYBYPEER"时为条件必选参数。<br>参数含义：Peer名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IPsec转发统计（IPSECFWDSTAT）](configobject/UDG/20.15.2/IPSECFWDSTAT.md)

## 使用实例

显示IPSEC转发统计。

```
DSP IPSECFWDSTAT: QRYTYPE=ALL;
RETCODE = 0  操作成功  
结果如下 
-------------------------                                  
Pod名称  =   ipsecexec-pod-0192-168-1-1
IPSEC会话加密报文个数/s = X
IPSEC会话解密报文个数/s = X
IPSEC会话加密的报文千字节数/s = X
IPSEC会话解密的报文千字节数/s = X
(结果个数 = 1) 

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示IPsec转发统计（DSP-IPSECFWDSTAT）_81179857.md`
