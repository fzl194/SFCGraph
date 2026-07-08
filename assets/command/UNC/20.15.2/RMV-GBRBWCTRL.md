---
id: UNC@20.15.2@MMLCommand@RMV GBRBWCTRL
type: MMLCommand
name: RMV GBRBWCTRL（删除GBR承载带宽速率控制配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GBRBWCTRL
command_category: 配置类
applicable_nf:
- GGSN
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- QoS映射
- GBR带宽控制
status: active
---

# RMV GBRBWCTRL（删除GBR承载带宽速率控制配置）

## 功能

**适用NF：GGSN、PGW-C、SMF**

该命令用来删除GBR承载带宽速率控制配置。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS控制的类型。<br>数据来源：全网规划<br>取值范围：<br>- APN_LEVEL（APN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：该参数在"CTRLTYPE"配置为"APN_LEVEL"时为条件必选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [GBR承载带宽速率控制配置（GBRBWCTRL）](configobject/UNC/20.15.2/GBRBWCTRL.md)

## 使用实例

如果想删除一条GBRBWCTRL配置，执行如下命令：

```
RMV GBRBWCTRL:CTRLTYPE=APN_LEVEL,APN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GBR承载带宽速率控制配置（RMV-GBRBWCTRL）_87520124.md`
