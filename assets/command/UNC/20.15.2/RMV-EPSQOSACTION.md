---
id: UNC@20.15.2@MMLCommand@RMV EPSQOSACTION
type: MMLCommand
name: RMV EPSQOSACTION（删除EPS QoS控制动作配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EPSQOSACTION
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- EPS QoS配置
- EPS QoS控制动作
status: active
---

# RMV EPSQOSACTION（删除EPS QoS控制动作配置）

## 功能

**适用NF：PGW-C**

该命令用于删除4G用户QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。

## 注意事项

命令执行后只对新接入用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS Profile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |
| QCI | QCI值 | 可选必选说明：必选参数<br>参数含义：该参数表示QoS流量级别。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@EPSQOSACTION]] · EPS QoS控制动作配置（EPSQOSACTION）

## 使用实例

删除“QOSPROFILENAME”为“test”，“QCI”为“2”的上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作：

```
RMV EPSQOSACTION:QOSPROFILENAME="test",QCI=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-EPSQOSACTION.md`
