---
id: UDG@20.15.2@MMLCommand@RMV DFSRPAIRMEM
type: MMLCommand
name: RMV DFSRPAIRMEM（删除双发选收结对成员配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: DFSRPAIRMEM
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN双发选收配置
- 双发选收结对成员配置
status: active
---

# RMV DFSRPAIRMEM（删除双发选收结对成员配置）

## 功能

**适用NF：UPF**

该命令用于删除双发选收结对内IMSI成员。

## 注意事项

- 该命令执行后立即生效。
- 记录存在。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DFSRPAIRID | 双发选收结对ID | 可选必选说明：必选参数<br>参数含义：该参数用于配置双发选收结对ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1-2048。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：双发选收结对成员IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15，每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DFSRPAIRMEM]] · 双发选收结对成员配置（DFSRPAIRMEM）

## 使用实例

删除双发选收中imsi为460111111111111的结对成员：

```
RMV DFSRPAIRMEM: DFSRPAIRID=1, IMSI="460111111111111";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除双发选收结对成员配置（RMV-DFSRPAIRMEM）_22918678.md`
