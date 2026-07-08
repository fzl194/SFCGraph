---
id: UNC@20.15.2@MMLCommand@RMV NRFGRFWDADDR
type: MMLCommand
name: RMV NRFGRFWDADDR（删除备份NRF地址）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFGRFWDADDR
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF主备容灾参数
status: active
---

# RMV NRFGRFWDADDR（删除备份NRF地址）

## 功能

**适用NF：NRF**

该命令用于删除备份NRF地址。

## 注意事项

- 该命令执行后立即生效。

- 仅供调测使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERNRFNAME | 备份NRF名称 | 可选必选说明：必选参数<br>参数含义：该参数表示对端NRF名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数表示对端NRF地址的IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| IPV4 | IPV4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数表示对端NRF的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPV6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数表示对端NRF的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PORT | 端口 | 可选必选说明：必选参数<br>参数含义：该参数表示对端NRF地址所对应的端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [备份NRF地址（NRFGRFWDADDR）](configobject/UNC/20.15.2/NRFGRFWDADDR.md)

## 使用实例

删除备份NRF地址，删除名称为peernrfname01的备份NRF地址：

```
RMV NRFGRFWDADDR: PEERNRFNAME="peernrfname01", IPTYPE=IPV4, IPV4="192.168.16.2", PORT=12345;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除备份NRF地址（RMV-NRFGRFWDADDR）_09653753.md`
