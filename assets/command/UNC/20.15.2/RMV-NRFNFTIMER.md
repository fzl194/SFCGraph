---
id: UNC@20.15.2@MMLCommand@RMV NRFNFTIMER
type: MMLCommand
name: RMV NRFNFTIMER（删除指定NF在NRF上的时长信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFNFTIMER
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- 定时器参数
status: active
---

# RMV NRFNFTIMER（删除指定NF在NRF上的时长信息）

## 功能

**适用NF：NRF**

该命令用于删除指定NF在NRF上的时长信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNFTIMER]] · 指定NF在NRF上的时长信息（NRFNFTIMER）

## 使用实例

运营商不需要在NRF上单独设置实例标识为"88888888-6666-1234-5678-123456789ABC"的时长信息时，执行如下命令。

```
RMV NRFNFTIMER: NFINSTANCEID="88888888-4444-1234-5678-123456789ABC";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除指定NF在NRF上的时长信息（RMV-NRFNFTIMER）_60449037.md`
