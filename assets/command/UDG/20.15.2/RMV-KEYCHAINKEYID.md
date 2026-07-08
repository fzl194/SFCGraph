---
id: UDG@20.15.2@MMLCommand@RMV KEYCHAINKEYID
type: MMLCommand
name: RMV KEYCHAINKEYID（删除Keychain Key ID的配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: KEYCHAINKEYID
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- Keychain
- Keychain Key ID配置
status: active
---

# RMV KEYCHAINKEYID（删除Keychain Key ID的配置）

## 功能

该命令用于删除一个Keychain Key ID的配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYCHAINNAME | Keychain名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Keychain名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。不含问号或空格，大小写不敏感。<br>默认值：无 |
| KEYID | Key索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Key索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/KEYCHAINKEYID]] · Keychain Key ID的配置（KEYCHAINKEYID）

## 使用实例

删除Keychain Key ID配置：

```
RMV KEYCHAINKEYID:KEYCHAINNAME="ospf",KEYID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除Keychain-Key-ID的配置（RMV-KEYCHAINKEYID）_00441061.md`
