---
id: UNC@20.15.2@MMLCommand@SET RGRESCTRL
type: MMLCommand
name: SET RGRESCTRL（设置RG资源控制配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: RGRESCTRL
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- RG资源控制
status: active
---

# SET RGRESCTRL（设置RG资源控制配置）

## 功能

**适用NF：PGW-C、SMF**

该命令用于设置RG老化功能以及RG超出规格后的处理动作。

## 注意事项

- 该命令执行后立即生效。

- RG老化时长是通过业务级QHT下发到UDG。
- 根据UDG上报业务QHT时，决策是否进行RG老化。
- 配置Gy接口携带流量计费信息时（ADD DCCTEMPLATE下使能QUOTATOTAL开关），RG老化功能不生效。
- 配置Gy接口携带流量计费信息时（ADD DCCTEMPLATE下使能PRIVATEATTR开关），RG老化功能不生效。
- 使用RG老化功能后，该功能与QHT功能配置有关，仅在QHT功能不使能或QHT使能但QHT值为0时生效。
- 该命令的ONLAGETIMER、OFLAGETIMER参数变更对5G融合计费是立即生效的，4G计费仅对用户激活及更新时生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ONLRGAGESW | ONLAGETIMER | ONLBLKTIMER | OFLRGAGESW | OFLAGETIMER | EXCSRVLMTACT |
| --- | --- | --- | --- | --- | --- |
| ENABLE | 20 | 0 | ENABLE | 20 | BLOCK |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ONLRGAGESW | 在线计费RG老化控制 | 可选必选说明：可选参数<br>参数含义：该参数用于控制在线计费RG老化功能。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：RG老化功能不使能<br>- “ENABLE（使能）”：RG老化功能使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RGRESCTRL查询当前参数配置值。<br>配置原则：无 |
| ONLAGETIMER | 在线计费RG老化时长 (分) | 可选必选说明：该参数在"ONLRGAGESW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于控制在线计费RG老化时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，10~1440，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RGRESCTRL查询当前参数配置值。<br>配置原则：<br>当配置为0时，表示老化时长无效。 |
| ONLBLKTIMER | 在线计费全局业务阻塞处理时间间隔 (分) | 可选必选说明：该参数在"ONLRGAGESW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于配置全局业务阻塞或重定向的时长，从阻塞或重定向开始经过这段时间以后，进行RG老化。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，10~1440，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RGRESCTRL查询当前参数配置值。<br>配置原则：<br>当配置为0时，表示阻塞时长无效。 |
| OFLRGAGESW | 离线计费RG老化控制 | 可选必选说明：可选参数<br>参数含义：该参数用于控制离线计费RG老化功能。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：RG老化功能不使能<br>- “ENABLE（使能）”：RG老化功能使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RGRESCTRL查询当前参数配置值。<br>配置原则：无 |
| OFLAGETIMER | 离线计费RG老化时长 (分) | 可选必选说明：该参数在"OFLRGAGESW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于控制离线计费RG老化时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，10~1440，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RGRESCTRL查询当前参数配置值。<br>配置原则：<br>当配置为0时，表示老化时长无效。 |
| EXCSRVLMTACT | 超出业务最大规格处理动作 | 可选必选说明：可选参数<br>参数含义：该参数用于控制新业务上报时，超过规格控制时的处理方式。<br>数据来源：本端规划<br>取值范围：<br>- “BLOCK（阻塞对应业务）”：阻塞对应业务<br>- “PASS（放通对应业务）”：放通对应业务<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RGRESCTRL查询当前参数配置值。<br>配置原则：<br>该参数对5G计费不生效，5G计费超过最大规格后默认去活用户。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RGRESCTRL]] · RG资源控制配置（RGRESCTRL）

## 使用实例

开启在线计费RG老化功能。

```
SET RGRESCTRL: ONLRGAGESW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-RGRESCTRL.md`
