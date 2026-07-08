---
id: UNC@20.15.2@MMLCommand@ACT NRFKEY
type: MMLCommand
name: ACT NRFKEY（激活NRF密钥）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: NRFKEY
command_category: 动作类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- 密钥管理
status: active
---

# ACT NRFKEY（激活NRF密钥）

## 功能

![](激活NRF密钥（ACT NRFKEY）_09652288.assets/notice_3.0-zh-cn_2.png)

执行该命令会使原来使用的密钥失效。

**适用NF：NRF**

该命令用于激活NRF的密钥信息。密钥信息需要先通过ADD NRFKEY配置，然后使用此命令激活才能生效。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYNAME | 密钥名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示在NRF上配置的密钥名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFKEY]] · NRF密钥（NRFKEY）

## 使用实例

激活密钥名称为keyname001的NRF密钥：

```
ACT NRFKEY: KEYNAME="keyname001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACT-NRFKEY.md`
