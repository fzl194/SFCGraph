---
id: UNC@20.15.2@MMLCommand@RMV NRFPROXYSMF
type: MMLCommand
name: RMV NRFPROXYSMF（删除NRF管理的ProxySMF）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV NRFPROXYSMF（删除NRF管理的ProxySMF）

## 功能

**适用NF：NRF**

该命令用于删除NRF管理的ProxySMF。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示本NRF管理的ProxySMF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFPROXYSMF]] · NRF管理的ProxySMF（NRFPROXYSMF）

## 使用实例

删除NF实例标识为Nfinstanceid01的NF的信息。

```
RMV NRFPROXYSMF: NFINSTANCEID="Nfinstanceid01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFPROXYSMF.md`
