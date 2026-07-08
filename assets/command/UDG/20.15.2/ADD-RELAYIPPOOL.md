---
id: UDG@20.15.2@MMLCommand@ADD RELAYIPPOOL
type: MMLCommand
name: ADD RELAYIPPOOL（增加媒体中继IP池）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: RELAYIPPOOL
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 2
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继回源IP池配置
status: active
---

# ADD RELAYIPPOOL（增加媒体中继IP池）

## 功能

**适用NF：UPF**

该命令用于增加媒体中继IP池。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为2。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | IP池名 | 可选必选说明：必选参数<br>参数含义：该参数用于配媒体中继IP池名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：无<br>配置原则：绑定VPN时需要确保该VPN已经配置（ADD VPNINST）。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYIPPOOL]] · 媒体中继IP池（RELAYIPPOOL）

## 使用实例

假设需要增媒体中继IP池，则命令如下：

```
ADD RELAYIPPOOL: POOLNAME="pool_relay";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加媒体中继IP池（ADD-RELAYIPPOOL）_73589008.md`
