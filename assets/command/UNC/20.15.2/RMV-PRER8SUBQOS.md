---
id: UNC@20.15.2@MMLCommand@RMV PRER8SUBQOS
type: MMLCommand
name: RMV PRER8SUBQOS（删除Pre-R8签约QoS配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PRER8SUBQOS
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- PreR8 QoS配置
- 本地PreR8 QoS
status: active
---

# RMV PRER8SUBQOS（删除Pre-R8签约QoS配置）

## 功能

**适用NF：GGSN**

该命令用于删除用户的签约QoS属性信息。

## 注意事项

命令执行后只对新接入用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBQOSINDEX | 用户QoS索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户QoS索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRER8SUBQOS]] · Pre-R8签约QoS配置（PRER8SUBQOS）

## 使用实例

删除SUBQOSINDEX为1的QoS签约信息：

```
RMV PRER8SUBQOS: SUBQOSINDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Pre-R8签约QoS配置（RMV-PRER8SUBQOS）_09653173.md`
