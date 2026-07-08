---
id: UDG@20.15.2@MMLCommand@ADD RELAYIPSECTION
type: MMLCommand
name: ADD RELAYIPSECTION（增加媒体中继IP段）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: RELAYIPSECTION
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 512
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继回源IP段配置
status: active
---

# ADD RELAYIPSECTION（增加媒体中继IP段）

## 功能

**适用NF：UPF**

该命令用于增加媒体中继IP段。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为512。
- 媒体中继IP地址段需要统一规划，不能与终端用户地址重复，不能与已配置的媒体中继IP地址重复。
- 整机支持配置的ipv4类型的媒体中继回源地址个数为8192。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | IP池名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定媒体中继IP段对应的IP池名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：IP池名与IP段ID不能与已有媒体中继IP段冲突。 |
| INSTID | 业务实例ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定对应业务实例ID。<br>数据来源：本端规划<br>取值范围：整数，取值范围0~15。<br>默认值：无<br>配置原则：该业务实例与relay-pod一一对应，需要为每个relay-pod配置一个地址池实例，可以通过DSP POD命令查询当前已存在的relay-pod。 |
| SECTIONID | IP段ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定媒体中继IP段ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0~4294967295。<br>默认值：无<br>配置原则：IP池名与IP段ID不能与已有媒体中继IP段冲突。 |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于配置IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型，取值范围为IPV4或IPV6。<br>- IPV4：IPV4。<br>- IPV6：IPV6。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于配置媒体中继IP段的IPv4地址。<br>数据来源：本端规划<br>取值范围：点分十进制。只允许配置A、B、C类地址。<br>默认值：无<br>配置原则：配置的IP段不可与已有的外部地址段冲突。 |
| IPV4MASKLEN | IPv4掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于配置IPv4掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为19～32。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于配置IPv6地址。<br>数据来源：本端规划<br>取值范围：冒号十六进制。<br>默认值：无<br>配置原则：配置的IP段不可与已有的外部地址段冲突。 |
| IPV6MASKLEN | IPv6掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于配置IPv6掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为115～128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [媒体中继IP段（RELAYIPSECTION）](configobject/UDG/20.15.2/RELAYIPSECTION.md)

## 使用实例

假设需要增加媒体中继IP段，则命令如下：

```
ADD RELAYIPSECTION: POOLNAME="pool_relay", SECTIONID=1, INSTID=1, IPVERSION=IPV4, IPV4ADDR="10.2.3.4", IPV4MASKLEN=30;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加媒体中继IP段（ADD-RELAYIPSECTION）_23946783.md`
