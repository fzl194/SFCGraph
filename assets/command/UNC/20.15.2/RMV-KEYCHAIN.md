---
id: UNC@20.15.2@MMLCommand@RMV KEYCHAIN
type: MMLCommand
name: RMV KEYCHAIN（删除Keychain的配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: KEYCHAIN
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- Keychain
- Keychain配置
status: active
---

# RMV KEYCHAIN（删除Keychain的配置）

## 功能

该命令用于删除一个Keychain实例。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYCHAINNAME | Keychain名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Keychain名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。不含问号或空格，大小写不敏感。<br>默认值：无 |

## 操作的配置对象

- [Keychain的配置（KEYCHAIN）](configobject/UNC/20.15.2/KEYCHAIN.md)

## 使用实例

删除Keychain实例：

```
RMV KEYCHAIN:KEYCHAINNAME="ospf";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Keychain的配置（RMV-KEYCHAIN）_00841577.md`
