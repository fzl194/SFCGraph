---
id: UNC@20.15.2@MMLCommand@RMV USRBLACKLST
type: MMLCommand
name: RMV USRBLACKLST（删除用户黑名单限制列表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USRBLACKLST
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 接入限制
- 黑名单接入限制
status: active
---

# RMV USRBLACKLST（删除用户黑名单限制列表）

## 功能

**适用NF：SGSN、MME、AMF**

该命令用于删除黑名单限制的用户列表。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定限制用户黑名单接入的IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRBLACKLST]] · 用户黑名单限制列表（USRBLACKLST）

## 使用实例

删除一条黑名单限制记录，执行如下命令：

```
RMV USRBLACKLST: IMSI="123456789012345";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户黑名单限制列表（RMV-USRBLACKLST）_15553257.md`
