---
id: UDG@20.15.2@MMLCommand@MOD MULTREDIRECT
type: MMLCommand
name: MOD MULTREDIRECT（修改多级重定向密码）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: MULTREDIRECT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- 多级重定向控制
- 多级重定向密码
status: active
---

# MOD MULTREDIRECT（修改多级重定向密码）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改多级重定向字段加密的密码。

## 注意事项

- 该命令执行后立即生效。
- 该命令与软参BIT_1704配合使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MULTREDIRECTNAME | 多级重定向名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置多级重定向密码配置名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31，不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |
| AES256CBCKEY | AES256 CBC密码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对多级重定向字段加密的密码。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度为1~32位的字符串，不支持空格。<br>默认值：无<br>配置原则：无 |
| AES256CBCKEYCONF | AES256 CBC密码确认 | 可选必选说明：必选参数<br>参数含义：该参数用于确认对多级重定向字段加密的密码。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度为1~32位的字符串，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MULTREDIRECT]] · 多级重定向密码（MULTREDIRECT）

## 使用实例

假如运营商想要修改加密密码为1234567890123456，配置如下：

```
MOD MULTREDIRECT:MULTREDIRECTNAME="test",AES256CBCKEY="1234567890123456",AES256CBCKEYCONF="1234567890123456";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改多级重定向密码（MOD-MULTREDIRECT）_93749059.md`
