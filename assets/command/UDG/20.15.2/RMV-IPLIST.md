---
id: UDG@20.15.2@MMLCommand@RMV IPLIST
type: MMLCommand
name: RMV IPLIST（删除IP地址列表）
nf: UDG
version: 20.15.2
verb: RMV
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

# RMV IPLIST（删除IP地址列表）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除配置IP地址。

## 注意事项

- 该命令执行后立即生效。
- 删除指定IPList时，IPList如果被绑定到Filter中，提示不允许删除，须先解除绑定关系。
- 删除IPList中的IP地址时，IPList如果被绑定到Filter中，系统会自动删除与该IP地址相关的Filter。
- 删除IPList中的IP地址时，如果该IP为IPList中的最后一个IP并且该IPList已经绑定了Filter，则提示不允许删除。
- IPList删除一个IP地址后，需要执行SET REFRESHSRV使当前配置生效，建议该操作在对所有IPList的配置修改完成后执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPLISTNAME | IP列表名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址版本类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址版本类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPLIST]] · IP地址列表（IPLIST）

## 使用实例

删除IP地址列表RMV IPLIST，IPLISTNAME为test01命令为：

```
RMV IPLIST:IPLISTNAME="test01";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-IPLIST.md`
