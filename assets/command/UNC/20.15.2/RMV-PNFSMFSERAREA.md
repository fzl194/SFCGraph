---
id: UNC@20.15.2@MMLCommand@RMV PNFSMFSERAREA
type: MMLCommand
name: RMV PNFSMFSERAREA（删除对端NF的SMF服务区域信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PNFSMFSERAREA
command_category: 配置类
applicable_nf:
- SMF
- NCG
- SGW-C
- GGSN
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端SMF服务区管理
status: active
---

# RMV PNFSMFSERAREA（删除对端NF的SMF服务区域信息）

## 功能

**适用NF：SMF、NCG、SGW-C、GGSN、PGW-C**

该命令用于删除本地配置的对端NF实例支持的为SMF提供服务区域的信息。

## 注意事项

- 该命令执行后立即生效。

- 当删除一条PNFNSINDEX为0的记录时，必须满足记录中不存在与将删除记录的NFINSTANCEID和SMFSERVINGAREA一样且PNFNSINDEX不为0的记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4；不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| SMFSERVINGAREA | SMF服务区域 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF为SMF提供的服务区域。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| PNFNSINDEX | 对端NF的切片索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF实例支持以SMFSERAREA为条件配置优先级与权重时所关联的切片索引，不用于切片过滤，对端NF支持的NS以PNFNS为准。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFSMFSERAREA]] · 对端NF的SMF服务区域信息（PNFSMFSERAREA）

## 使用实例

由于规划变更，对端NF实例标识为UPF_Instance_0的NF不能再为本端SMF提供服务区域area01，需要删除。

```
RMV PNFSMFSERAREA: NFINSTANCEID="UPF_Instance_0", SMFSERVINGAREA="area01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PNFSMFSERAREA.md`
