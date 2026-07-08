---
id: UDG@20.15.2@MMLCommand@SET WHITEURLLISTBIND
type: MMLCommand
name: SET WHITEURLLISTBIND（设置用户模板的URL白名单列表）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: WHITEURLLISTBIND
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 105000
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- 用户模板
status: active
---

# SET WHITEURLLISTBIND（设置用户模板的URL白名单列表）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置用户模板的URL白名单列表。配置该URL白名单列表后，用户进行内容计费的在线计费时，如果匹配的费率组的配额不足，用户报文会触发SMF/UPF 向OCS发送配额请求消息，如果OCS返回的是重定向处理，并且业务报文的URL匹配了其中配置的URL，用户业务可以正常访问URL，无需进行重定向处理。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为105000。
- 该命令设定后的数据，需要通过LST USERPROFILE命令进行查看。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及“,”、“;”、“"”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |
| WHITELISTNAME | URL白名单名称 | 可选必选说明：必选参数<br>参数含义：指定URL白名单名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD WHITEURLLIST命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/WHITEURLLISTBIND]] · 用户模板的URL白名单列表（WHITEURLLISTBIND）

## 使用实例

假如运营商需要绑定URL白名单列表“testwhiteurllist”到名称为“testuserprofilename”的用户模板：

```
SET WHITEURLLISTBIND:USERPROFILENAME="testuserprofilename",WhiteListName="testwhiteurllist";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置用户模板的URL白名单列表（SET-WHITEURLLISTBIND）_82837282.md`
