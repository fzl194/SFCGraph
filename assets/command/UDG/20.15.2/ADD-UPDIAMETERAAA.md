---
id: UDG@20.15.2@MMLCommand@ADD UPDIAMETERAAA
type: MMLCommand
name: ADD UPDIAMETERAAA（增加Diameter AAA服务器）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPDIAMETERAAA
command_category: 配置类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
max_records: 10
category_path:
- 用户面服务管理
- Diameter AAA管理
- 服务器配置
- Diameter AAA信息
status: active
---

# ADD UPDIAMETERAAA（增加Diameter AAA服务器）

## 功能

**适用NF：UPF**

此命令用于添加Diameter AAA服务器，配置Diameter AAA服务器主机名、域名和VPN实例。如果UPF需要向Diameter AAA服务器请求授权，需要执行该命令。

## 注意事项

- 该命令执行后对新接入的会话生效。
- 该命令最大记录数为10。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA服务器的主机名。<br>数据来源：本端规划<br>取值范围：只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，由软参BIT2670控制是否区分大小写。BIT2670值为0时，不区分大小写；值为1时，区分大小写，但不允许配置多个仅大小写不同的host-name或realm-name。<br>默认值：无<br>配置原则：无 |
| REALMNAME | 域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA服务器的域名。<br>数据来源：本端规划<br>取值范围：只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，由软参BIT2670控制是否区分大小写。BIT2670值为0时，不区分大小写；值为1时，区分大小写，但不允许配置多个仅大小写不同的host-name或realm-name。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter AAA服务器所在的VPN实例。<br>数据来源：本端规划<br>取值范围：区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD VPNINST命令配置生成。<br>- 输入单空格将删除该参数已有配置项。 |
| WALVALUE | WAL值 | 可选必选说明：可选参数<br>参数含义：该参数表示整机（UPF）每秒发送给该Diameter AAA服务器的最大消息数，但STR消息的发送不受发送窗口限制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~65534。<br>默认值：无<br>配置原则：缺省为0，表示不控制消息数。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMETERAAA]] · Diameter AAA服务器（UPDIAMETERAAA）

## 使用实例

根据网络规划，需要新增一个Diameter AAA服务器在域“www.huawei.com”上激活用户，在UPF上规划Diameter AAA服务器的VPN实例为“vpn1”：

```
ADD UPDIAMETERAAA:HOSTNAME="diameteraaa1",REALMNAME="www.huawei.com",VPNINSTANCE="vpn1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-UPDIAMETERAAA.md`
