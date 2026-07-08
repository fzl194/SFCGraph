---
id: UNC@20.15.2@MMLCommand@RMV QOS5QI2QCIMAP
type: MMLCommand
name: RMV QOS5QI2QCIMAP（删除5QI到标准QCI的映射）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOS5QI2QCIMAP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- QoS映射
- 5QI到QCI映射
status: active
---

# RMV QOS5QI2QCIMAP（删除5QI到标准QCI的映射）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除5QI到标准QCI的映射。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS控制的类型。<br>数据来源：全网规划<br>取值范围：<br>- APN_LEVEL（APN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| APN | APN | 可选必选说明：该参数在"CTRLTYPE"配置为"APN_LEVEL"时为条件必选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| QOS5QISTART | 5QI范围起始点 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5QI范围的起始值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5QI到QCI的映射（QOS5QI2QCIMAP）](configobject/UNC/20.15.2/QOS5QI2QCIMAP.md)

## 使用实例

如果想删除一条QOS5QI2QCIMAP配置，执行如下命令：

```
RMV QOS5QI2QCIMAP:CTRLTYPE=APN_LEVEL,APN="huawei.com",QOS5QISTART=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5QI到标准QCI的映射（RMV-QOS5QI2QCIMAP）_87680064.md`
