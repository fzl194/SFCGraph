---
id: UDG@20.15.2@MMLCommand@MOD RELAYAUTHKEY
type: MMLCommand
name: MOD RELAYAUTHKEY（修改媒体中继鉴权密钥）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: RELAYAUTHKEY
command_category: 配置类
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

# MOD RELAYAUTHKEY（修改媒体中继鉴权密钥）

## 功能

**适用NF：UPF、PGW-U**

![](修改媒体中继鉴权密钥（MOD RELAYAUTHKEY）_94871973.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行该命令后，会影响媒体中继防盗链校验功能。

该命令用于修改媒体中继鉴权密钥。修改主（备）密钥会使旧的主（备）密钥失效，可以仅修改主或备密钥，也可同时修改主备密钥。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYAUTHKEYNAME | 媒体中继鉴权密钥名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定媒体中继认证密钥名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| MASTERAUTHKEY | 主鉴权密钥 | 可选必选说明：可选参数<br>参数含义：该参数用于指定主认证密钥。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为6～64，不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |
| MASTERKEYCONFIRM | 确认主鉴权密钥 | 可选必选说明：可选参数<br>参数含义：该参数用于指定确认主认证密钥。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为6～64。不支持空格。<br>默认值：无<br>配置原则：无 |
| SLAVEAUTHKEY | 备鉴权密钥 | 可选必选说明：可选参数<br>参数含义：该参数用于指定备认证密钥。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为6～64。不支持空格。<br>默认值：无<br>配置原则：无 |
| SLAVEKEYCONFIRM | 确认备鉴权密钥 | 可选必选说明：可选参数<br>参数含义：该参数用于指定确认备认证密钥。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为6～64。不支持空格。<br>默认值：无<br>配置原则：无 |
| DESC | 媒体中继鉴权密钥描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定媒体中继鉴权密钥描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYAUTHKEY]] · 媒体中继鉴权密钥（RELAYAUTHKEY）

## 使用实例

修改媒体中继鉴权密钥：

```
MOD RELAYAUTHKEY: RELAYAUTHKEYNAME="auth1", MASTERAUTHKEY="*****", MASTERKEYCONFIRM="*****";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-RELAYAUTHKEY.md`
