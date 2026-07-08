---
id: UNC@20.15.2@MMLCommand@MOD EPSSUBQOS
type: MMLCommand
name: MOD EPSSUBQOS（修改EPS签约QoS配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: EPSSUBQOS
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- EPS QoS配置
- 本地EPS QoS
status: active
---

# MOD EPSSUBQOS（修改EPS签约QoS配置）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来修改用户的签约QoS属性。当APN下使能COA功能时，RADIUS鉴权服务器会下发subscriber-qos index，UNC根据index匹配到subscriber-qos配置，用来进行用户QoS的协商控制，主动调整带宽等。如果RADIUS鉴权服务器没有下发subscriber-qos index，则根据APN下绑定的qos-profile下的subscriber-qos index进行用户QoS的协商控制、调整带宽等。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 该配置必须和网络规划一致，否则会导致用户的带宽和业务级别等控制出现问题。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBQOSINDEX | 用户QoS索引 | 可选必选说明：必选参数<br>参数含义：该参数表示用户QoS索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| QCI | 标准QCI | 可选必选说明：可选参数<br>参数含义：该参数表示QoS业务类型参数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~9，69~70。<br>默认值：无<br>配置原则：无 |
| ARPPL | ARP的优先级别 | 可选必选说明：可选参数<br>参数含义：该参数表示分配优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| AMBRDL | 下行APN AMBRR(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置下行APN-AMBR比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2000000。<br>默认值：无<br>配置原则：无 |
| AMBRUL | 上行APN AMBRR(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置上行APN-AMBR比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2000000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [EPS签约QoS配置（EPSSUBQOS）](configobject/UNC/20.15.2/EPSSUBQOS.md)

## 使用实例

修改EPSSUBQOS，“SUBQOSINDEX”为“123”，“AMBRDL”为“564116”，“AMBRUL”为“302222”，“ARPPL”为“12”，“QCI”为“7”：

```
MOD EPSSUBQOS: SUBQOSINDEX=123, QCI=7, ARPPL=12, AMBRDL=564116, AMBRUL=302222;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改EPS签约QoS配置（MOD-EPSSUBQOS）_09654145.md`
