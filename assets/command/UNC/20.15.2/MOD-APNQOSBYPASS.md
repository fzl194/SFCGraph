---
id: UNC@20.15.2@MMLCommand@MOD APNQOSBYPASS
type: MMLCommand
name: MOD APNQOSBYPASS（修改BYPASS场景QoS描述配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNQOSBYPASS
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 5GC UDM全故障Qos
status: active
---

# MOD APNQOSBYPASS（修改BYPASS场景QoS描述配置）

## 功能

**适用NF：SMF**

该命令用于修改APNQOSBYPASS的配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| SUBQOSINDEX | 5G用户QoS索引 | 可选必选说明：可选参数<br>参数含义：该参数表示用户QoS索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>该取值必须和ADD 5GCSUBQOS中配置的“SUBQOSINDEX”参数取值相同。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNQOSBYPASS]] · BYPASS场景QoS描述配置（APNQOSBYPASS）

## 使用实例

当UDM全故障进入ByPass状态时，需要修改用户的QoS信息，此时修改APNQOSBYPASS配置信息：

```
MOD APNQOSBYPASS:APN="huawei.com",SUBQOSINDEX=5;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改BYPASS场景QoS描述配置（MOD-APNQOSBYPASS）_22556859.md`
