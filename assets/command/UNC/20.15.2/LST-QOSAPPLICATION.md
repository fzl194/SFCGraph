---
id: UNC@20.15.2@MMLCommand@LST QOSAPPLICATION
type: MMLCommand
name: LST QOSAPPLICATION（查询流策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSAPPLICATION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 流量策略
status: active
---

# LST QOSAPPLICATION（查询流策略）

## 功能

该命令用来查询接口上应用流量策略的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DIRECTION | 报文方向 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在接口入方向还是出方向应用流量策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- inbound：入方向报文。<br>- outbound：出方向报文。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用流量策略的接口，以太主接口/子接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| POLICYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用的流量策略。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| LAYER | 层信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用的流量策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- default：此策略应用在IP层。<br>- link_layer：此策略应用在链路层。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSAPPLICATION]] · 流策略（QOSAPPLICATION）

## 使用实例

查询应用在接口上的所有流量策略：

```
LST QOSAPPLICATION:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
报文方向  =  入方向
接口名称  =  Ethernet66/0/3
策略名称  =  p1
  层信息  =  默认值
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-QOSAPPLICATION.md`
