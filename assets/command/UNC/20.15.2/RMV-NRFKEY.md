---
id: UNC@20.15.2@MMLCommand@RMV NRFKEY
type: MMLCommand
name: RMV NRFKEY（删除NRF密钥）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFKEY
command_category: 配置类
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

# RMV NRFKEY（删除NRF密钥）

## 功能

**适用NF：NRF**

当运营商不再使用原规划的私钥信息时，可以使用此命令删除。该命令只能删除未激活状态的密钥信息。

## 注意事项

- 该命令执行后立即生效。

- 不允许删除处于激活状态的密钥信息，可以通过LST SBINRFKEY命令查询对应的公钥信息。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYNAME | 密钥名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示在NRF上配置的密钥名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NRF密钥（NRFKEY）](configobject/UNC/20.15.2/NRFKEY.md)

## 使用实例

系统中存在未激活状态的密钥名称为keyname001的NRF密钥信息，运营商规划后面不再使用此密钥信息，执行此命令。

```
RMV NRFKEY: KEYNAME="keyname001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NRF密钥（RMV-NRFKEY）_09652231.md`
