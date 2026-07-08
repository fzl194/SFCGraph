---
id: UDG@20.15.2@MMLCommand@RMV GLBTRUNKREMARK
type: MMLCommand
name: RMV GLBTRUNKREMARK（删除整机Trunk Remark配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: GLBTRUNKREMARK
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 宽带集群流量管理
- 全局宽带集群QoS到DSCP或TOS映射
status: active
---

# RMV GLBTRUNKREMARK（删除整机Trunk Remark配置）

## 功能

**适用NF：SGW-U、PGW-U**

该命令用于删除已有的整机Trunk Remark配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QCI | QCI | 可选必选说明：必选参数<br>参数含义：该参数表示QoS流量级别。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~9，65~66，69~70。<br>默认值：无<br>配置原则：无 |
| ARPPL | ARP的优先级别 | 可选必选说明：可选参数<br>参数含义：该参数表示ARP的优先级别。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBTRUNKREMARK]] · 整机Trunk Remark配置（GLBTRUNKREMARK）

## 使用实例

删除整机中Trunk Remark配置是QCI为1，且ARP优先级为1的数据：

```
RMV GLBTRUNKREMARK: QCI=1, ARPPL=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-GLBTRUNKREMARK.md`
