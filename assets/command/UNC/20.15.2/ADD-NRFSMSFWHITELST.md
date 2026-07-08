---
id: UNC@20.15.2@MMLCommand@ADD NRFSMSFWHITELST
type: MMLCommand
name: ADD NRFSMSFWHITELST（增加SMSF白名单）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFSMSFWHITELST
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- SMSF割接场景NRF处理策略
status: active
---

# ADD NRFSMSFWHITELST（增加SMSF白名单）

## 功能

![](增加SMSF白名单（ADD NRFSMSFWHITELST）_71623458.assets/notice_3.0-zh-cn_2.png)

该命令与SET NRFSMSFWHLISTSW配合使用，在白名单未设置完成时请勿打开SMSFWHLISTSW，否则未加入到白名单中的SMSF在发现参数仅携带TargetNftype时将无法被发现。

**适用NF：NRF**

该命令用于增加SMSF白名单内的SMSF实例。白名单用于配置现网存量SMSF，确保存量SMSF可以为存量用户提供业务，避免错误业务导流。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入64条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示需要增加到SMSF白名单中的NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSMSFWHITELST]] · SMSF白名单（NRFSMSFWHITELST）

## 使用实例

将实例ID为“88888888-4444-1234-5678-123456789ABC”的SMSF添加到白名单中，可执行如下命令。

```
ADD NRFSMSFWHITELST: NFINSTANCEID="88888888-4444-1234-5678-123456789ABC";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SMSF白名单（ADD-NRFSMSFWHITELST）_71623458.md`
