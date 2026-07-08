---
id: UNC@20.15.2@MMLCommand@RMV SECPOLICY
type: MMLCommand
name: RMV SECPOLICY（删除防攻击策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SECPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略
status: active
---

# RMV SECPOLICY（删除防攻击策略）

## 功能

该命令用于删除安全策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYID | 安全策略编号 | 可选必选说明：必选参数<br>参数含义：策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SECPOLICY]] · 防攻击策略（SECPOLICY）

## 使用实例

删除安全策略：

```
RMV SECPOLICY:POLICYID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SECPOLICY.md`
