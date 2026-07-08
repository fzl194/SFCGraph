---
id: UDG@20.15.2@MMLCommand@MOD QOSPROP
type: MMLCommand
name: MOD QOSPROP（修改QoS属性）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: QOSPROP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 业务QOS控制
- 业务质量属性
status: active
---

# MOD QOSPROP（修改QoS属性）

## 功能

**适用NF：PGW-U、UPF**

该命令是用来修改PCC预定义规则的QoS参数。

## 注意事项

- 该命令执行后立即生效。
- 修改QoS属性，执行MOD QOSPROP命令前，需要确定修改记录是否存在，存在才能修改记录，否则修改失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROPNAME | Qos属性名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| GBRUPLKVALUE | 保证的上行比特率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定上行保证带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| GBRDNLKVALUE | 保证的下行比特率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下行保证带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| MBRUPLKVALUE | 最大上行比特率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定上行最大带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| MBRDNLKVALUE | 最大下行比特率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下行最大带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| QOSURRNAME | QoS使用量上报规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置QoS URR名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD URR命令配置生成。<br>- 输入单空格将删除该参数已有配置项。<br>- 设置的QOSURRNAME必须是系统已经存在的QoS URR名称。 |
| DECOUPLINGSW | 上下行解耦开关 | 可选必选说明：可选参数<br>参数含义：基于上下行解耦的视频差异化调度功能开关。当上下行解耦开关功能开启时，该配置设置的下行链路模式优先级高于ADD SaDedicBearer命令的配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| KEYFLOWDETECTSW | 关键流检测开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置识别关键业务流的开关是否开启。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| KEYFLOWTIME | 关键流时长（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“KEYFLOWDETECTSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定识别关键业务流的最低持续时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～60。<br>默认值：无<br>配置原则：无 |
| KEYFLOWSPEED | 关键流速率（二进制千比特每秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“KEYFLOWDETECTSW”配置为“ENABLE”时为可选参数。<br>参数含义：1、该参数用于指定关键业务流的最低传输速率。 2、参数单位是二进制千比特每秒，即Kibps，1Kibps等于1024bps。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2048。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/QOSPROP]] · QoS属性（QOSPROP）

## 使用实例

修改名称为“test”的QoS属性，保证的上行比特率为10，保证的下行比特率为1000，最大上行比特率为20，最大下行比特率为2000，开启关键流检测，时长和速率分别为5秒和50Kbps的命令为：

```
MOD QOSPROP: QOSPROPNAME="test", GBRUPLKVALUE=10, GBRDNLKVALUE=1000, MBRUPLKVALUE=20, MBRDNLKVALUE=2000, KEYFLOWDETECTSW=ENABLE, KEYFLOWTIME=5, KEYFLOWSPEED=50;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-QOSPROP.md`
