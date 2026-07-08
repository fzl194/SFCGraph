---
id: UNC@20.15.2@MMLCommand@ADD DDNPRIORITYARP
type: MMLCommand
name: ADD DDNPRIORITYARP（增加基于ARP的DDN消息优先级配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DDNPRIORITYARP
command_category: 配置类
applicable_nf:
- SGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- 基于ARP的DDN消息优先级管理
status: active
---

# ADD DDNPRIORITYARP（增加基于ARP的DDN消息优先级配置）

## 功能

**适用NF：SGW-C、SMF**

该命令用于增加基于ARP的DDN消息优先级。

## 注意事项

- 该命令执行后立即生效。

- 该命令用于DDN流控场景下，UNC识别DDN消息的优先级。
- DDN Throttling功能使能时高优先级业务流触发的DDN消息不流控。当用户不配置DDNPRIORITYARP时，则默认为低优先级。

- 最多可输入15条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ARP | ARP数值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DDN消息的优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DDN_LOW（低）<br>- DDN_HIGH（高）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DDNPRIORITYARP]] · 基于ARP的DDN消息优先级配置（DDNPRIORITYARP）

## 使用实例

设置ARP为1的DDN消息是高优先级：

```
ADD DDNPRIORITYARP: ARP=1, PRIORITY=DDN_HIGH;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DDNPRIORITYARP.md`
