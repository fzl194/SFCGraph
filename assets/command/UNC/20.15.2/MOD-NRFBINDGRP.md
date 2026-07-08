---
id: UNC@20.15.2@MMLCommand@MOD NRFBINDGRP
type: MMLCommand
name: MOD NRFBINDGRP（修改对端NRF实例组成员）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NRFBINDGRP
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF拓扑配置
- NRF实例组成员管理
status: active
---

# MOD NRFBINDGRP（修改对端NRF实例组成员）

## 功能

**适用NF：NRF**

该命令用于修改对端NRF实例组的成员。

该命令的使用场景：当业务侧需要在对端NRF组中修改组成员信息时（例如注册状态、优先级或权重），则通过该命令修改。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFINSTNAME | NRF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示对端NRF实例组中NRF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~38。<br>默认值：无<br>配置原则：无 |
| GROUPNAME | 实例组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示对端NRF实例组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |
| ISREGED | 对端NRF是否注册 | 可选必选说明：可选参数<br>参数含义：该参数用于表示对端NRF是否作为南向NRF在当前NRF注册过。<br>NRF通过此参数提高后续南向路由选择的可靠性：<br>- 对于已注册的对端南向NRF，当前NRF会在本地持有的NF profile中判断其状态是否正常，正常则作为后续路由选择，异常则过滤掉不再选择；<br>- 对于未注册的对端南向NRF不做判断。<br>数据来源：本端规划<br>取值范围：<br>- FALSE（未注册的NRF）<br>- TRUE（已注册的南向NRF）<br>默认值：无<br>配置原则：无 |
| NRFINSTID | NRF实例标识 | 可选必选说明：该参数在"ISREGED"配置为"TRUE"时为条件必选参数。<br>参数含义：该参数用于表示对端NRF组中当前配置的NRF成员的实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。不区分大小写。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于表示对端NRF实例在NRF组中的优先级，参数值越小，优先级越高。<br>当前NRF选择对端NRF时，优先选择优先级高的NRF组成员进行消息通信，如果优先级相同，则随机选择其中一个。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| CAPACITY | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NRF的权重。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFBINDGRP]] · 对端NRF实例组成员（NRFBINDGRP）

## 使用实例

当需要修改南向的一个NRF注册状态为已注册，且此NRF实例名称为nrfinstname001，实例组名称为nrfgroup001，实例标识为123e4567-e89b-12d3-a456-426655440000时，配置此命令。

```
MOD NRFBINDGRP: NRFINSTNAME="nrfinstname001", GROUPNAME="nrfgroup001", ISREGED=TRUE, NRFINSTID="123e4567-e89b-12d3-a456-426655440000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NRFBINDGRP.md`
