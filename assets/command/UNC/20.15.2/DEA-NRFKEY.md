---
id: UNC@20.15.2@MMLCommand@DEA NRFKEY
type: MMLCommand
name: DEA NRFKEY（去激活NRF的密钥信息）
nf: UNC
version: 20.15.2
verb: DEA
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

# DEA NRFKEY（去激活NRF的密钥信息）

## 功能

![](去激活NRF的密钥信息（DEA NRFKEY）_25120878.assets/notice_3.0-zh-cn_2.png)

如果当前密钥处于激活状态，会导致Token分配功能不可用。

**适用NF：NRF**

该命令用于去激活NRF的密钥信息。

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

去激活密钥名称为keyname001的NRF密钥：

```
DEA NRFKEY: KEYNAME="keyname001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/去激活NRF的密钥信息（DEA-NRFKEY）_25120878.md`
