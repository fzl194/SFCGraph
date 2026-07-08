---
id: UDG@20.15.2@MMLCommand@MOD DFSRPAIR
type: MMLCommand
name: MOD DFSRPAIR（修改双发选收结对配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: DFSRPAIR
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN双发选收配置
- 双发选收结对配置
status: active
---

# MOD DFSRPAIR（修改双发选收结对配置）

## 功能

**适用NF：UPF**

该命令用于修改双发选收结对配置。

## 注意事项

- 该命令执行后立即生效。
- 该记录必须已经存在。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DFSRPAIRID | 双发选收结对ID | 可选必选说明：必选参数<br>参数含义：该参数用于配置双发选收结对ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1-2048。<br>默认值：无<br>配置原则：无 |
| DFSRPAIRMODE | 双发选收模式 | 可选必选说明：可选参数<br>参数含义：该参数用于配置双发选收模式。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- FRER_SRC_MAC：基于源MAC的FRER双发选收模式。<br>- FRER_PAIR：基于结对的FRER双发选收模式。<br>默认值：无<br>配置原则：无 |
| PAIRDESCRIPTION | 结对描述 | 可选必选说明：可选参数<br>参数含义：该参数用于配置结对的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DFSRPAIR]] · 双发选收结对配置（DFSRPAIR）

## 使用实例

把双发选收结对1修改为源mac模式：

```
MOD DFSRPAIR: DFSRPAIRID=1, DFSRPAIRMODE=FRER_SRC_MAC;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改双发选收结对配置（MOD-DFSRPAIR）_26514779.md`
