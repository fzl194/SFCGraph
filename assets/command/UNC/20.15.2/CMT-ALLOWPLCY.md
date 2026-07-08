---
id: UNC@20.15.2@MMLCommand@CMT ALLOWPLCY
type: MMLCommand
name: CMT ALLOWPLCY（提交允许访问策略配置）
nf: UNC
version: 20.15.2
verb: CMT
object_keyword: ALLOWPLCY
command_category: 调测类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- 访问授权控制
- 访问授权策略管理
status: active
---

# CMT ALLOWPLCY（提交允许访问策略配置）

## 功能

![](提交允许访问策略配置（CMT ALLOWPLCY）_09651378.assets/notice_3.0-zh-cn_2.png)

该命令会将之前通过ADD ALLOWEDPLMNS/RMV ALLOWEDPLMNS/ADD ALLOWEDNSSAIS/RMV ALLOWEDNSSAIS/ADD ALLOWEDNFTYPES/RMV ALLOWEDNFTYPES/ADD ALLOWEDDOMAINS/RMV ALLOWEDDOMAINS配置的所有访问授权控制策略提交并生效。

**适用NF：NRF**

该命令用于提交配置的访问授权控制策略。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMTTYPE | 提交类型 | 可选必选说明：可选参数<br>参数含义：该参数表示访问授权控制策略提交的范围。<br>数据来源：本端规划<br>取值范围：<br>- ALL（ALL）<br>默认值：ALL<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALLOWPLCY]] · 提交允许访问策略配置（ALLOWPLCY）

## 使用实例

提交所有访问授权控制策略配置信息。

```
CMT ALLOWPLCY: CMTTYPE=ALL;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CMT-ALLOWPLCY.md`
