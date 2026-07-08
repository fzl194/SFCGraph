---
id: UNC@20.15.2@MMLCommand@RMV NFGROUPID
type: MMLCommand
name: RMV NFGROUPID（删除NF群组信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NFGROUPID
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF GROUP信息管理
status: active
---

# RMV NFGROUPID（删除NF群组信息）

## 功能

**适用NF：SMSF**

该命令用于删除本端NF实例支持的群组信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。本参数的构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，SMSF_Instance_0。<br>默认值：无<br>配置原则：<br>本参数取值与ADD NFUUID命令中的“NF实例名称”参数取值保持一致时，关联关系生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFGROUPID]] · NF群组信息（NFGROUPID）

## 使用实例

删除NF实例标识为SMSF_Instance_0的群组标识。

```
RMV NFGROUPID: NFINSTANCENAME="SMSF_Instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF群组信息（RMV-NFGROUPID）_91460557.md`
