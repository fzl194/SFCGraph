---
id: UNC@20.15.2@MMLCommand@RMV PEERNFIPLIST
type: MMLCommand
name: RMV PEERNFIPLIST（删除对端局向连接列表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PEERNFIPLIST
command_category: 配置类
applicable_nf:
- AMF
- SMF
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# RMV PEERNFIPLIST（删除对端局向连接列表）

## 功能

**适用NF：AMF、SMF、SMSF**

本命令用于删除对端局向连接列表，本功能适用于与北向网管对接以及相关性能统计功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | 对端局向NF实例号 | 可选必选说明：必选参数<br>参数含义：对端局向NF实例号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |
| LOCALIP | 本端IP地址 | 可选必选说明：必选参数<br>参数含义：本端IP地址。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |
| PEERIP | 对端IP地址 | 可选必选说明：必选参数<br>参数含义：对端IP地址。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |
| MASK | 掩码 | 可选必选说明：可选参数<br>参数含义：掩码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PEERNFIPLIST]] · 对端局向连接列表（PEERNFIPLIST）

## 使用实例

若运营商想删除一条对端局向连接记录，可用如下命令：

```
RMV PEERNFIPLIST: NFINSTANCEID="bf33a517-7789-4637-b675-b3591b0d706b", LOCALIP="10.20.3.4", PEERIP="10.20.3.5";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PEERNFIPLIST.md`
