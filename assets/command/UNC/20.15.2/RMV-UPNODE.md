---
id: UNC@20.15.2@MMLCommand@RMV UPNODE
type: MMLCommand
name: RMV UPNODE（删除UPF节点）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UPNODE
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
- UP节点管理
status: active
---

# RMV UPNODE（删除UPF节点）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于删除指定实例名称的UPF节点特征。

## 注意事项

- 该命令执行后立即生效。

- 执行RMV UPNODE时会同步删除的配置：IPALLOCBYUPFSW。
- 如果UPNODE已经绑定在UPFBINDGRP中，则不允许删除，需要执行命令RMV UPFBINDGRP解除绑定关系后再删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | UPF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPNODE]] · UPF节点（UPNODE）

## 使用实例

删除实例名称为“upf1”的UPF节点特征：

```
RMV UPNODE:NFINSTANCENAME="upf1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-UPNODE.md`
