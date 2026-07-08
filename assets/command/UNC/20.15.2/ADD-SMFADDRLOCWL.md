---
id: UNC@20.15.2@MMLCommand@ADD SMFADDRLOCWL
type: MMLCommand
name: ADD SMFADDRLOCWL（增加位置区域地址分配用户白名单）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD SMFADDRLOCWL（增加位置区域地址分配用户白名单）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加位置区域地址分配用户白名单，加入白名单的用户不受基于位置地址分配开关控制，不基于位置区域分配地址，即针对该用户，SET IPALLOCBYLOCSW命令中的SWITCH参数相当于DISABLE。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 如果白名单中存在用户，那么至少有一条ADD POOLGRPMAP命令中不包含LOCATIONGRPNAME参数，且SET APNIPALLOCRULE或者SET IPALLOCRULE命令中IPv4/v6的三级规则中不能都有LOCATION（位置区）。

- 最多可输入20条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSISDN | MSISDN | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的MSISDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFADDRLOCWL]] · 位置区域地址分配用户白名单（SMFADDRLOCWL）

## 使用实例

增加MSISDN为123456用户到位置区域地址分配白名单中：

```
ADD SMFADDRLOCWL: MSISDN="123456";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SMFADDRLOCWL.md`
