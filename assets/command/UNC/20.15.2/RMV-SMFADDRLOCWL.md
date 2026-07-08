---
id: UNC@20.15.2@MMLCommand@RMV SMFADDRLOCWL
type: MMLCommand
name: RMV SMFADDRLOCWL（删除位置区域地址分配用户白名单）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMFADDRLOCWL
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 位置区域地址分配白名单
status: active
---

# RMV SMFADDRLOCWL（删除位置区域地址分配用户白名单）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除按照区域地址分配用户白名单。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSISDN | MSISDN | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的MSISDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFADDRLOCWL]] · 位置区域地址分配用户白名单（SMFADDRLOCWL）

## 使用实例

删除用户MSISDN为123456的区域地址分配白名单：

```
RMV SMFADDRLOCWL: MSISDN="123456";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除位置区域地址分配用户白名单（RMV-SMFADDRLOCWL）_35636463.md`
