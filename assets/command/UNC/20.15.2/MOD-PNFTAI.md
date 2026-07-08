---
id: UNC@20.15.2@MMLCommand@MOD PNFTAI
type: MMLCommand
name: MOD PNFTAI（修改对端NF的TAI信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PNFTAI
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
- PGW-C
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF实例TAI信息
status: active
---

# MOD PNFTAI（修改对端NF的TAI信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG、PGW-C、SGW-C**

该命令用于修改本地配置的对端NF实例支持的TAI信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAI对应的NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。NFINSTANCEID参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| TAI | 跟踪区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。该参数大小写不敏感，且会强制转大写处理。<br>默认值：无<br>配置原则：<br>5G TAI : 输入长度范围是11~12。后6位为16进制数，其余为10进制数。<br>4G TAI：输入长度范围是9~10。后4位为16进制数，其余为10进制数。 |
| PNFNSINDEX | 对端NF的切片索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF实例支持以TAI为条件配置优先级与权重时所关联的切片索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>当该值配置为空或0时，代表支持所有切片索引。 |
| PRISWITCH | 优先级功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF实例针对TAI的优先级设置方式。<br>数据来源：本端规划<br>取值范围：<br>- “INHERIT（继承）”：继承PNFPROFILE中相同字段的内容<br>- “SPECIFIC（指定）”：使用本配置记录中相同字段的内容<br>默认值：无<br>配置原则：<br>对于UPF，在选择过程的优选阶段中，会按照优先级高低排序待选列表，结合其他优选条件做综合选择。对于其它类型的NF，需要将SET NFDISCPLCY中参数CFGTAIPRISW设置为ON，才能开启基于TAI优先级的优选功能。 |
| PRIORITY | 优先级 | 可选必选说明：该参数在"PRISWITCH"配置为"SPECIFIC"时为条件必选参数。<br>参数含义：该参数用于指定对端NF所支持的TAI的优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。值越小优先级越高。<br>默认值：无<br>配置原则：无 |
| CAPSWITCH | 容量功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF支持TAI及其关联切片为条件的权重选择功能是否开启。<br>数据来源：本端规划<br>取值范围：<br>- “INHERIT（继承）”：继承PNFPROFILE中相同字段的内容<br>- “SPECIFIC（指定）”：使用本配置记录中相同字段的内容<br>默认值：无<br>配置原则：<br>当配置的对端网元是UPF，且CAPSWITCH为SPECIFIC时，CAPACITY生效的前提条件是配置UPSELECTFLAG的PRIORITYFLAG为ENABLE。 |
| CAPACITY | 容量 | 可选必选说明：该参数在"CAPSWITCH"配置为"SPECIFIC"时为条件必选参数。<br>参数含义：本参数用于指定对端UPF所支持的TAI及其关联切片为条件的相对权重。特别地，如果权重的绝对值不超过本参数的取值范围，那么本参数可以直接取用权重绝对值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| BINDNWDAFINFOID | 绑定的NWDAFINFO ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定绑定的PNFNWDAFEVENT记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>BINDNWDAFINFOID需要与ADD PNFNWDAFEVENT中的NWDAFINFOID一致。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PNFTAI]] · 对端NF的TAI信息（PNFTAI）

## 使用实例

修改对端NF所支持的TAI信息，NF实例标识为SMF_Instance_0，TAI为460001000001。

```
MOD PNFTAI: NFINSTANCEID="SMF_Instance_0", TAI="460001000001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-PNFTAI.md`
