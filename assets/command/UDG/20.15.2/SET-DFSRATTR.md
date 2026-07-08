---
id: UDG@20.15.2@MMLCommand@SET DFSRATTR
type: MMLCommand
name: SET DFSRATTR（设置双发选收属性配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DFSRATTR
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN双发选收配置
- 双发选收属性配置
status: active
---

# SET DFSRATTR（设置双发选收属性配置）

## 功能

**适用NF：UPF**

该命令用于设置双发选收相关属性信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | NEPRIFLAG | PAIRUEACTTIME |
| --- | --- | --- |
| 初始值 | PRIMARY | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NEPRIFLAG | 网元主备用标识 | 可选必选说明：可选参数<br>参数含义：当网元主备部署时，该参数用于指定网元是主用网元还是备用网元。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PRIMARY：主用。<br>- SECONDARY：备用。<br>默认值：无<br>配置原则：无 |
| PAIRUEACTTIME | 双发选收结对内用户激活时长 | 可选必选说明：条件必选参数<br>前提条件：该参数在“NEPRIFLAG”配置为“SECONDARY”时为必选参数。<br>参数含义：该参数用于配置双发选收结对内两个UE激活的最大时间间隔，超过配置的间隔则已激活的用户会被去激活。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3-300秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DFSRATTR]] · 双发选收属性配置（DFSRATTR）

## 使用实例

设置网元主备类型为备用，设置双发选收结对中ue会话老化时间为20秒：

```
SET DFSRATTR: NEPRIFLAG=SECONDARY, PAIRUEACTTIME=20;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-DFSRATTR.md`
