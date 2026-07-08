---
id: UNC@20.15.2@MMLCommand@RMV NFSUBS
type: MMLCommand
name: RMV NFSUBS（删除NF的订阅上下文）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NFSUBS
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF参数管理
- 注册与订阅管理
status: active
---

# RMV NFSUBS（删除NF的订阅上下文）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于向NRF发起去订阅流程及删除指定的订阅上下文信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBSCRIPTIONID | 订阅上下文标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要发起去订阅的NF订阅上下文的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~512。<br>默认值：无<br>配置原则：<br>该参数需要与DSP NFSUBCONDITIONS命令中的订阅标识值保持一致。 |

## 操作的配置对象

- [NF的订阅上下文（NFSUBS）](configobject/UNC/20.15.2/NFSUBS.md)

## 使用实例

当前NF不再订阅SUBSCRIPTIONID为0相关的订阅条件。

```
RMV NFSUBS: SUBSCRIPTIONID="0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF的订阅上下文（RMV-NFSUBS）_09654188.md`
