---
id: UDG@20.15.2@MMLCommand@DSP DFSRPAIRMEMSTA
type: MMLCommand
name: DSP DFSRPAIRMEMSTA（显示双发选收结对成员状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DFSRPAIRMEMSTA
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN双发选收配置
- 双发选收结对成员配置
status: active
---

# DSP DFSRPAIRMEMSTA（显示双发选收结对成员状态）

## 功能

**适用NF：UPF**

该命令用于查询双发选收结对内IMSI成员激活状态。

## 注意事项

- 状态激活显示为Active，状态不激活显示为Inactive。
- 只有当该IMSI对应的用户激活在该双发选收结对绑定的5G LAN组会话下，状态才是Active。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DFSRPAIRID | 双发选收结对ID | 可选必选说明：必选参数<br>参数含义：该参数用于配置双发选收结对ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1-2048。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [双发选收结对成员状态（DFSRPAIRMEMSTA）](configobject/UDG/20.15.2/DFSRPAIRMEMSTA.md)

## 使用实例

显示双发选收结对1中成员的激活状态：

```
DSP DFSRPAIRMEMSTA: DFSRPAIRID=1;
```

```

```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示双发选收结对成员状态（DSP-DFSRPAIRMEMSTA）_23157714.md`
