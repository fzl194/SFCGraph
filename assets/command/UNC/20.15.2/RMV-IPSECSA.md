---
id: UNC@20.15.2@MMLCommand@RMV IPSECSA
type: MMLCommand
name: RMV IPSECSA（删除IPsec安全联盟）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPSECSA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- IPsec
- IPsec安全联盟
status: active
---

# RMV IPSECSA（删除IPsec安全联盟）

## 功能

该命令用于删除IPsec安全联盟。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SANAME | 安全联盟名称 | 可选必选说明：必选参数<br>参数含义：安全联盟名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。不区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPSECSA]] · IPsec安全联盟（IPSECSA）

## 使用实例

删除IPsec安全联盟：

```
RMV IPSECSA:SANAME="1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IPSECSA.md`
