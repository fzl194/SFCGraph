---
id: UNC@20.15.2@MMLCommand@RMV SFELBHASH
type: MMLCommand
name: RMV SFELBHASH（删除IP转发负载分担hash计算模式）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SFELBHASH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP性能配置
- IP转发负载分担hash模式配置
status: active
---

# RMV SFELBHASH（删除IP转发负载分担hash计算模式）

## 功能

该命令用于删除IP转发负载分担hash计算模式。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。
- 该命令仅支持发往Fabric口方向的报文做负载分担hash。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PKTTYPE | 报文类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示负载分担hash模式的报文类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IP：IP报文做负载分担hash计算。<br>默认值：无 |

## 操作的配置对象

- [IP转发负载分担hash计算模式（SFELBHASH）](configobject/UNC/20.15.2/SFELBHASH.md)

## 使用实例

删除负载分担hash计算模式：

```
RMV SFELBHASH: PKTTYPE=IP;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IP转发负载分担hash计算模式（RMV-SFELBHASH）_00601441.md`
