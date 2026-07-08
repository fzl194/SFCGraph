---
id: UNC@20.15.2@MMLCommand@ADD UPCMPTCUSIE
type: MMLCommand
name: ADD UPCMPTCUSIE（增加UP节点定制信元兼容性配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UPCMPTCUSIE
command_category: 配置类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP节点协议兼容性管理
status: active
---

# ADD UPCMPTCUSIE（增加UP节点定制信元兼容性配置）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于增加UP节点定制信元兼容性配置。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入2048条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFINSTANCE | UPF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| IENAME | 定制信元名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要定制的信元名称。<br>数据来源：全网规划<br>取值范围：<br>- EFSEID（扩展F-SEID）<br>- PUSERID（私有UserID）<br>默认值：无<br>配置原则：无 |
| CUSTOMTYPE | 定制信元类型值 | 可选必选说明：必选参数<br>参数含义：该参数用于设置定制信元的类型值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是32768~65535。<br>默认值：无<br>配置原则：无 |
| CUSTOMEPID | 定制信元企业ID | 可选必选说明：必选参数<br>参数含义：该参数用于设置定制信元的企业ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UP节点定制信元兼容性配置（UPCMPTCUSIE）](configobject/UNC/20.15.2/UPCMPTCUSIE.md)

## 使用实例

增加UP节点定制信元配置，UPF实例标识为upf_instance_1，设置Extend FSEID 企业ID为2011，类型值为37101，执行如下命令：

```
ADD UPCMPTCUSIE: UPFINSTANCE="upf_instance_1", IENAME=EFSEID, CUSTOMTYPE=37101, CUSTOMEPID=2011;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加UP节点定制信元兼容性配置（ADD-UPCMPTCUSIE）_75982836.md`
