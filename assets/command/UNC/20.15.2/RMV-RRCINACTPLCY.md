---
id: UNC@20.15.2@MMLCommand@RMV RRCINACTPLCY
type: MMLCommand
name: RMV RRCINACTPLCY（删除RRC Inactive策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RRCINACTPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- RRC Inactive业务管理
- RRC Inactive策略
status: active
---

# RMV RRCINACTPLCY（删除RRC Inactive策略）

## 功能

**适用NF：AMF**

该命令用于删除RRC Inactive功能的开启策略，通过此命令删除指定用户或者指定号段的RRC Inactive功能。若将指定号段全部删除，则所有用户均开启RRC Inactive功能。

## 注意事项

- 该命令执行后立即生效。

- 如果需要关闭RRC Inactive功能，执行[**SET NGMMFUNC**](../../MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)命令，配置"RRC Inactive功能"参数为"NO"。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIBEGN | IMSI起始号段 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的IMSI起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>若期望下发基于指定IMSI前缀的号段匹配策略，需要用十进制数字"0"和"9"分别补齐IMSIBEGN和IMSIEND的剩余长度。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RRCINACTPLCY]] · RRC Inactive策略（RRCINACTPLCY）

## 使用实例

删除基于IMSI起始号段“123450000000000”开启的RRC Inactive功能，执行如下命令：

```
RMV RRCINACTPLCY: IMSIBEGN="123450000000000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除RRC-Inactive策略（RMV-RRCINACTPLCY）_23782826.md`
