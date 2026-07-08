---
id: UDG@20.15.2@MMLCommand@MOD SRVCHAIN
type: MMLCommand
name: MOD SRVCHAIN（修改业务链）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: SRVCHAIN
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- 业务链配置
status: active
---

# MOD SRVCHAIN（修改业务链）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改业务链配置，可以修改上下行业务链ID，为Rule提供业务链转发策略。

## 注意事项

- 该命令执行后立即生效。
- 修改被Rule关联的SrvChain配置的UPSRVCHAINID或DNSRVCHAINID参数数值时，请确保SFIP上已关联相应的Uplink ID或Downlink ID，保证分流业务不受影响。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVCHAINNAME | 业务链名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置业务链名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| UPSRVCHAINID | 上行业务链ID | 可选必选说明：可选参数<br>参数含义：该参数用于设置上行业务链ID。<br>数据来源：全网规划<br>取值范围：0~16777215。<br>默认值：无<br>配置原则：无 |
| DNSRVCHAINID | 下行业务链ID | 可选必选说明：可选参数<br>参数含义：该参数用于设置下行业务链ID。<br>数据来源：全网规划<br>取值范围：0~16777215。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVCHAIN]] · 业务链（SRVCHAIN）

## 使用实例

如果运营商想要修改业务链名称为TestSrvChain的流量分类策略，设置上行业务链ID为101，下行业务链ID为201。命令如下：

```
MOD SRVCHAIN:SRVCHAINNAME="TestSrvChain",UPSRVCHAINID=101,DNSRVCHAINID=201;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改业务链（MOD-SRVCHAIN）_47006830.md`
