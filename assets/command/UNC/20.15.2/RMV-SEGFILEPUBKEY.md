---
id: UNC@20.15.2@MMLCommand@RMV SEGFILEPUBKEY
type: MMLCommand
name: RMV SEGFILEPUBKEY（删除号段配置文件的签名验证公钥）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SEGFILEPUBKEY
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- 号段导入文件公钥管理
status: active
---

# RMV SEGFILEPUBKEY（删除号段配置文件的签名验证公钥）

## 功能

**适用NF：NRF**

该命令用于删除号段配置文件的签名验证公钥。

使用该命令后，后续号段配置文件加载会出现失败。需要通过ADD SEGFILEPUBKEY命令重新添加签名验证公钥。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYNAME | 公钥名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示在NRF上配置的号段配置文件的签名验证公钥名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SEGFILEPUBKEY]] · 号段配置文件的签名验证公钥（SEGFILEPUBKEY）

## 使用实例

号段配置文件的签名验证私钥发生变更以后，签名验证公钥会相应的变更，需要删除现在的签名验证公钥，删除公钥名称为keyname001的号段配置文件的签名验证公钥。

```
RMV SEGFILEPUBKEY: KEYNAME="keyname001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SEGFILEPUBKEY.md`
