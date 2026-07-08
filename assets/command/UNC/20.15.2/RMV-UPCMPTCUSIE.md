---
id: UNC@20.15.2@MMLCommand@RMV UPCMPTCUSIE
type: MMLCommand
name: RMV UPCMPTCUSIE（删除UP节点定制信元兼容性配置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV UPCMPTCUSIE（删除UP节点定制信元兼容性配置）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于删除UP节点定制信元兼容性配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFINSTANCE | UPF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| IENAME | 定制信元名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要定制的信元名称。<br>数据来源：全网规划<br>取值范围：<br>- EFSEID（扩展F-SEID）<br>- PUSERID（私有UserID）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPCMPTCUSIE]] · UP节点定制信元兼容性配置（UPCMPTCUSIE）

## 使用实例

删除UPF实例标识为upf_instance_1的Extend F-SEID信元相关配置，执行如下命令：

```
RMV UPCMPTCUSIE: UPFINSTANCE="upf_instance_1", IENAME=EFSEID;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-UPCMPTCUSIE.md`
