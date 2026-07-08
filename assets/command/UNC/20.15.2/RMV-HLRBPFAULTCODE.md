---
id: UNC@20.15.2@MMLCommand@RMV HLRBPFAULTCODE
type: MMLCommand
name: RMV HLRBPFAULTCODE（删除HLR BYPASS故障状态码）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HLRBPFAULTCODE
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HLR BYPASS故障状态码
status: active
---

# RMV HLRBPFAULTCODE（删除HLR BYPASS故障状态码）

## 功能

**适用网元：SGSN**

该命令用于删除HLR BYPASS故障状态码。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 生效范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定特定故障码的生效范围。<br>取值范围：<br>- ALL（整系统）：整系统 |
| FAULTCODE | 故障码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定进入HLR BYPASS状态的原因值。<br>取值范围：0-65535<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HLRBPFAULTCODE]] · HLR BYPASS故障状态码（HLRBPFAULTCODE）

## 使用实例

删除HLR BYPASS故障状态码配置，生效范围为ALL（整系统），故障码为3002。

```
RMV HLRBPFAULTCODE: RANGE=ALL, FAULTCODE=3002;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-HLRBPFAULTCODE.md`
