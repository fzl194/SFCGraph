---
id: UNC@20.15.2@MMLCommand@MOD IMSIBINDUP
type: MMLCommand
name: MOD IMSIBINDUP（修改用户和UPF的绑定关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IMSIBINDUP
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 用户绑定UPF
status: active
---

# MOD IMSIBINDUP（修改用户和UPF的绑定关系）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于修改用户和UPF的绑定关系，支持修改一个用户和UPF的绑定。

## 注意事项

- 如果REDIRECT属性为DISABLE，则只在会话建立流程有效；如果REDIRECT属性为ENABLE，则在会话建立和切换流程同时有效。

- 使用该命令时，参数PAUPNFINSTNAME和参数IMUPNFINSTNAME为必填参数。
- 使用该命令时，如果用户在SGW-C、PGW-C、I-SMF、SMFN16a、VSMF、SMFN16形态下想要选中特定UPF，建议将参数PAUPNFINSTNAME和参数IMUPNFINSTNAME配置为同一个UPF。
- 使用该命令时，如果为参数AUXUPNFINSTNAME或RAUXUPNFINSTNAME下发空格，则默认将该参数清空。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 起始IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI号段的起始IMSI，当只有一个IMSI时，起始IMSI和末位IMSI相同。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~15。IMSI参数每一位只能是数字0-9；当IMSI长度不足15位时，会自动低位补0直到15位。<br>默认值：无<br>配置原则：无 |
| ACCESSTYPE | 接入类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的接入类型。<br>数据来源：本端规划<br>取值范围：<br>- GUL（2/3/4G接入）<br>- NG（5G接入）<br>默认值：无<br>配置原则：无 |
| PAUPNFINSTNAME | 主锚点UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定主锚点UPF实例名称。<br>主锚点UPF为用户接入数据网络使用到的中心UPF锚点。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| AUXUPNFINSTNAME | 辅锚点UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定辅锚点UPF实例名称。<br>辅锚点UPF为用户接入数据网络使用到的边缘UPF锚点。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| IMUPNFINSTNAME | N3/S1-U口UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N3/S1-U口UPF实例名称。<br>N3/S1U口UPF是用户与锚点UPF之间的IUPF。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>若通过IMSIBINDUP选择插入I-UPF，请针对该I-UPF增加服务区域信息（ADD PNFSMFSERAREA），服务区域需要绑定到TAI或LAI。 |
| ULCLDEPLOYMODE | ULCL部署模式 | 可选必选说明：该参数在"ACCESSTYPE"配置为"NG"时为条件可选参数。<br>参数含义：该参数用于表示ULCL部署模式。<br>数据来源：本端规划<br>取值范围：当ACCESSTYPE为GUL时，自动修改此值为PSASHUNTMUST。<br>- “AUXSHUNTPREFER（优先使用辅锚点分流）”：优先辅锚点分流。如果没有与辅锚点合设的ULCL，则使用分离的ULCL。<br>- “PSASHUNTMUST（只使用主锚点分流）”：只使用主锚点分流。<br>默认值：无<br>配置原则：无 |
| REDIRECT | 重选到绑定UPF | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否允许用户在UP重选的场景下，选择IMSI绑定的UPF。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（关）<br>- ENABLE（开）<br>默认值：无<br>配置原则：无 |
| RAUXUPINSTNAME | 重选指向的辅锚点UPF实例名称 | 可选必选说明：该参数在"REDIRECT"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于重选指向的辅锚点UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| RIMUPINSTNAME | 重选指向的接入UPF实例名称 | 可选必选说明：该参数在"REDIRECT"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于重选指向的接入UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| RULCLDEPLOYMODE | 重选后的ULCL部署模式 | 可选必选说明：该参数在"REDIRECT"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于表示重选后的ULCL部署模式。<br>数据来源：本端规划<br>取值范围：当ACCESSTYPE为GUL时，自动修改此值为PSASHUNTMUST。<br>- “AUXSHUNTPREFER（优先使用辅锚点分流）”：优先辅锚点分流。如果没有与辅锚点合设的ULCL，则使用分离的ULCL。<br>- “PSASHUNTMUST（只使用主锚点分流）”：只使用主锚点分流。<br>默认值：无<br>配置原则：无 |
| MDNUPNFINSTNAME | 智能分流专用会话锚点UPF实例名称 | 可选必选说明：该参数在"ACCESSTYPE"配置为"NG"时为条件可选参数。<br>参数含义：该参数用于指定智能分流专用会话的锚点UPF。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMSIBINDUP]] · 用户和UPF的绑定关系（IMSIBINDUP）

## 使用实例

修改用户“111111”在5G的UP绑定关系：主锚点绑定UP1，辅锚点绑定UP2，N3锚点绑定UP3：

```
MOD IMSIBINDUP: IMSI="111111", ACCESSTYPE=NG, PAUPNFINSTNAME="UP1", AUXUPNFINSTNAME="UP2", IMUPNFINSTNAME="UP3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-IMSIBINDUP.md`
