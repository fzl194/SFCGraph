---
id: UDG@20.15.2@MMLCommand@UPD RELAYAUTHKEY
type: MMLCommand
name: UPD RELAYAUTHKEY（更新媒体中继鉴权密钥）
nf: UDG
version: 20.15.2
verb: UPD
object_keyword: RELAYAUTHKEY
command_category: 动作类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继鉴权密钥
status: active
---

# UPD RELAYAUTHKEY（更新媒体中继鉴权密钥）

## 功能

**适用NF：UPF、PGW-U**

![](更新媒体中继鉴权密钥（UPD RELAYAUTHKEY）_94632049.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行该命令后，会影响媒体中继防盗链校验功能。

该命令用于更新主鉴权密钥，原主鉴权密钥置为备鉴权密钥。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYAUTHKEYNAME | 媒体中继鉴权密钥名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定媒体中继认证密钥名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| NEWAUTHKEY | 新增鉴权密钥 | 可选必选说明：必选参数<br>参数含义：该参数用于指定新增认证密钥。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为6～64。不支持空格。<br>默认值：无<br>配置原则：无 |
| NEWKEYCONFIRM | 确认新增鉴权密钥 | 可选必选说明：必选参数<br>参数含义：该参数用于指定确认新增认证密钥。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为6～64。不支持空格。<br>默认值：无<br>配置原则：无 |
| DESC | 媒体中继鉴权密钥描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定媒体中继鉴权密钥描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYAUTHKEY]] · 媒体中继鉴权密钥（RELAYAUTHKEY）

## 使用实例

更新媒体中继鉴权密钥：

```
UPD RELAYAUTHKEY: RELAYAUTHKEYNAME="auth1", NEWAUTHKEY="*****", NEWKEYCONFIRM="*****";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/更新媒体中继鉴权密钥（UPD-RELAYAUTHKEY）_94632049.md`
