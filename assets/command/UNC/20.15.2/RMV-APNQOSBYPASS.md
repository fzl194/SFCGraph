---
id: UNC@20.15.2@MMLCommand@RMV APNQOSBYPASS
type: MMLCommand
name: RMV APNQOSBYPASS（删除BYPASS场景QoS描述配置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV APNQOSBYPASS（删除BYPASS场景QoS描述配置）

## 功能

**适用NF：SMF**

该命令用于删除APNQOSBYPASS的配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [BYPASS场景QoS描述配置（APNQOSBYPASS）](configobject/UNC/20.15.2/APNQOSBYPASS.md)

## 使用实例

删除APN为"huawei.com"的配置信息：

```
RMV APNQOSBYPASS:APN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BYPASS场景QoS描述配置（RMV-APNQOSBYPASS）_77197036.md`
