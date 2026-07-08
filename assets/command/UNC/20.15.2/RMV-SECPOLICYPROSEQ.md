---
id: UNC@20.15.2@MMLCommand@RMV SECPOLICYPROSEQ
type: MMLCommand
name: RMV SECPOLICYPROSEQ（删除安全策略匹配顺序）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SECPOLICYPROSEQ
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略匹配顺序
status: active
---

# RMV SECPOLICYPROSEQ（删除安全策略匹配顺序）

## 功能

该命令用来删除安全策略匹配顺序。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：必选参数<br>参数含义：安全策略号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |

## 操作的配置对象

- [安全策略匹配顺序（SECPOLICYPROSEQ）](configobject/UNC/20.15.2/SECPOLICYPROSEQ.md)

## 使用实例

删除安全策略匹配顺序：

```
RMV SECPOLICYPROSEQ:SECPOLICYID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除安全策略匹配顺序（RMV-SECPOLICYPROSEQ）_50280974.md`
