---
id: UNC@20.15.2@MMLCommand@ADD CGBINDING
type: MMLCommand
name: ADD CGBINDING（增加CG绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CGBINDING
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG组管理
- CG绑定
status: active
---

# ADD CGBINDING（增加CG绑定关系）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来增加CG绑定关系。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1024。
- 用户选定CG Group后，CG优先级使用绑定CG到CG Group时指定的优先级，不使用配置CG时指定的优先级。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CGGRPID | CG组ID | 可选必选说明：必选参数<br>参数含义：指定CG组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：该参数使用ADD CGGROUP命令配置生成。 |
| CGIPVERSION | CG IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CG IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：IPv4。<br>- IPV6：IPv6。<br>默认值：IPV4<br>配置原则：无 |
| CGIPV4ADDR | CG IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CGIPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：CG服务器IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CGIPV6ADDR | CG IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CGIPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：CG服务器的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| CGPORT | CG端口号 | 可选必选说明：必选参数<br>参数含义：CG服务器端口号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1024～65535。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 等级 | 可选必选说明：必选参数<br>参数含义：CG服务器的等级。值越小优先级越高，即0的优先级最高，100的优先级最低。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [CG绑定关系（CGBINDING）](configobject/UNC/20.15.2/CGBINDING.md)

## 关联任务

- [[UNC@20.15.2@Task@0-00011]]

## 使用实例

增加CG绑定关系，CG组ID为“1”，CG的IP地址为“192.168.0.2”，CG的端口号为“25009”，CG优先级为“1”：

```
ADD CGBINDING: CGGRPID=1, CGIPVERSION=IPV4, CGIPV4ADDR="192.168.0.2", CGPORT=25009, PRIORITY=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加CG绑定关系（ADD-CGBINDING）_09896874.md`
