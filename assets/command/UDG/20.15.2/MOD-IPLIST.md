---
id: UDG@20.15.2@MMLCommand@MOD IPLIST
type: MMLCommand
name: MOD IPLIST（修改IP地址列表）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: IPLIST
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- IP地址列表
status: active
---

# MOD IPLIST（修改IP地址列表）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改配置IP地址。

## 注意事项

- 该命令执行后立即生效。
- 对于已经存在的IPList，如果IP地址已经存在于该IPList中，则修改记录，否则添加记录。
- 当IPList已经被绑定到Filter时，不允许将其从IPv4的地址类型直接修改为IPv6的地址类型，也不允许将其从IPv6的地址类型直接修改为IPv4的地址类型。
- 向IPList添加一个IP地址后，需要执行SET REFRESHSRV使当前配置生效，建议该操作在对所有IPList的配置修改完成后执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPLISTNAME | IP列表名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址版本类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址版本类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| MASKVALUE | IP地址掩码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址掩码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。IPVERSION为IPV4时，取值范围是0~32。IPVERSION为IPV6时，取值范围是0~128。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPLIST]] · IP地址列表（IPLIST）

## 使用实例

修改IP地址列表，IPLISTNAME为test01，IPVERSION为IPV4：

```
MOD IPLIST:IPLISTNAME="test01",IPVERSION=IPV4,IPV4ADDR="10.0.0.1",MASKVALUE=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改IP地址列表（MOD-IPLIST）_82837338.md`
