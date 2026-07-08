---
id: UNC@20.15.2@MMLCommand@ADD NRFPROXYSMF
type: MMLCommand
name: ADD NRFPROXYSMF（增加NRF管理的ProxySMF）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFPROXYSMF
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# ADD NRFPROXYSMF（增加NRF管理的ProxySMF）

## 功能

**适用NF：NRF**

该命令用于增加本NRF管理的ProxySMF，对于国际漫游业务，通过本命令配置的ProxySMF可以使NRF在服务发现流程中识别是否是ProxySMF。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示本NRF管理的ProxySMF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：无 |
| NFNAME | NF名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF管理的ProxySMF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFPROXYSMF]] · NRF管理的ProxySMF（NRFPROXYSMF）

## 使用实例

增加NRFPROXYSMF，NF实例标识为Nfinstanceid01，NF名称为ProxySMF01

```
ADD NRFPROXYSMF: NFINSTANCEID="Nfinstanceid01", NFNAME="ProxySMF01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NRFPROXYSMF.md`
