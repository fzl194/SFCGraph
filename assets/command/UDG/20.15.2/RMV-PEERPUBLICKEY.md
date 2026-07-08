---
id: UDG@20.15.2@MMLCommand@RMV PEERPUBLICKEY
type: MMLCommand
name: RMV PEERPUBLICKEY（删除对端公钥）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PEERPUBLICKEY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 接入配置管理
- 密钥配置
- 公钥配置
status: active
---

# RMV PEERPUBLICKEY（删除对端公钥）

## 功能

该命令用于删除对端公钥。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYNAME | 密钥名称 | 可选必选说明：必选参数<br>参数含义：密钥名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| PUBKEYTYPE | 密钥类型 | 可选必选说明：必选参数<br>参数含义：密钥类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RSA：RSA公钥。<br>- DSA：DSA公钥。<br>- ECC：ECC公钥。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PEERPUBLICKEY]] · 对端公钥（PEERPUBLICKEY）

## 使用实例

删除类型为RSA、名称为rsa1的对端公钥：

```
RMV PEERPUBLICKEY:KEYNAME="rsa1",PUBKEYTYPE=RSA;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-PEERPUBLICKEY.md`
