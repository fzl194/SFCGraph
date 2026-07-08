---
id: UDG@20.15.2@MMLCommand@RMV RSA1024
type: MMLCommand
name: RMV RSA1024（删除RSA1024公钥配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RSA1024
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- RSA1024公钥配置
status: active
---

# RMV RSA1024（删除RSA1024公钥配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除RSA1024的相关配置。

## 注意事项

- 该命令执行后立即生效。
- 已经被绑定到HeadEn命令中的RSA1024配置不能删除，若需要删除该RSA1024信息，需要先执行MOD HEADEN或RMV HEADEN命令解除绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RSA1024NAME | RSA1024公钥名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RSA1024公钥配置名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [RSA1024公钥配置（RSA1024）](configobject/UDG/20.15.2/RSA1024.md)

## 使用实例

假如运营商想删除名称为“test”的RSA1024配置：

```
RMV RSA1024: RSA1024NAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除RSA1024公钥配置（RMV-RSA1024）_82837573.md`
