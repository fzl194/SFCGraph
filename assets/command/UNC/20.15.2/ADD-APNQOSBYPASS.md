---
id: UNC@20.15.2@MMLCommand@ADD APNQOSBYPASS
type: MMLCommand
name: ADD APNQOSBYPASS（增加BYPASS场景QoS描述配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNQOSBYPASS
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 对新用户生效
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

# ADD APNQOSBYPASS（增加BYPASS场景QoS描述配置）

## 功能

**适用NF：SMF**

该命令用于UDM全故障BYPASS场景下设置指定APN的QoS的描述信息。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| SUBQOSINDEX | 5G用户QoS索引 | 可选必选说明：必选参数<br>参数含义：该参数表示用户QoS索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>该取值必须和ADD 5GCSUBQOS中配置的“SUBQOSINDEX”参数取值相同。 |

## 操作的配置对象

- [BYPASS场景QoS描述配置（APNQOSBYPASS）](configobject/UNC/20.15.2/APNQOSBYPASS.md)

## 使用实例

当UDM全故障进入BYPASS状态时，需要设置用户的QoS信息，此时增加APNQOSBYPASS配置信息：

```
ADD APNQOSBYPASS:APN="huawei.com",SUBQOSINDEX=5;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加BYPASS场景QoS描述配置（ADD-APNQOSBYPASS）_77197030.md`
