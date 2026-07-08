---
id: UDG@20.15.2@MMLCommand@ADD REDUNDRDTIP
type: MMLCommand
name: ADD REDUNDRDTIP（增加冗余备份重定向IP地址）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: REDUNDRDTIP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 2
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 静态地址用户路由冗余
- 冗余备份重定向IP
status: active
---

# ADD REDUNDRDTIP（增加冗余备份重定向IP地址）

## 功能

**适用NF：PGW-U、UPF**

该命令用来配置全局的冗余备份隧道虚拟重定向IP，即用于将业务流重定向到Gre Tunnel的虚拟IP地址。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为2。
- 执行该命令配置IPV4ADDRESS/IPV6ADDRESS参数时，需要确保对应路由存在，否则主UPF故障期间在备UPF上激活的用户，在主UPF恢复后，这部分用户的下行业务不能发往备UPF。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于设置冗余备份重定向IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPv4：表示地址类型为IPv4。<br>- IPv6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPV4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于设置地址类型为IPv4的冗余备份重定向的目的地址，即用于将业务流重定向到Gre Tunnel的虚拟IP地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。必须是合法的ipv4地址，采用点分十进制"X.X.X.X"形式。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPV6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于设置地址类型为IPv6的冗余备份重定向的目的地址，即用于将业务流重定向到Gre Tunnel的虚拟IP地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。必须是合法的ipv6地址，16进制数，采用"X:X::X:X"形式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [冗余备份重定向IP（REDUNDRDTIP）](configobject/UDG/20.15.2/REDUNDRDTIP.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00055]]

## 使用实例

配置地址类型为IPv4的冗余备份隧道虚拟重定向地址：

```
ADD REDUNDRDTIP: IPVERSION=IPv4, IPV4ADDRESS="192.168.0.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加冗余备份重定向IP地址（ADD-REDUNDRDTIP）_75097445.md`
