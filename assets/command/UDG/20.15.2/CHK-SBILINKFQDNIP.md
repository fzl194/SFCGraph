---
id: UDG@20.15.2@MMLCommand@CHK SBILINKFQDNIP
type: MMLCommand
name: CHK SBILINKFQDNIP（检查服务化接口链路集FQDN的IP地址）
nf: UDG
version: 20.15.2
verb: CHK
object_keyword: SBILINKFQDNIP
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口链路集管理
status: active
---

# CHK SBILINKFQDNIP（检查服务化接口链路集FQDN的IP地址）

## 功能

该命令用于检查链路集的FQDN的IP地址，如果FQDN的IP地址有变化，则刷新链路集的IP地址。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKSETID | 链路集标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要做检查的链路集标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：<br>该取值必须和<br>[**DSP SBILINKSET**](显示服务化接口链路集信息（DSP SBILINKSET）_84132098.md)<br>中显示的“Link Set ID”参数取值相同。 |
| FQDN | 域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要做检查的域名信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>该取值必须和<br>[**DSP SBILINKSET**](显示服务化接口链路集信息（DSP SBILINKSET）_84132098.md)<br>中显示的“Peer FQDN”参数取值相同。 |

## 操作的配置对象

- [检查服务化接口链路集FQDN的IP地址（SBILINKFQDNIP）](configobject/UDG/20.15.2/SBILINKFQDNIP.md)

## 使用实例

若运营商想检查全量链路集，执行如下命令:

```
CHK SBILINKFQDNIP:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/检查服务化接口链路集FQDN的IP地址（CHK-SBILINKFQDNIP）_71493014.md`
