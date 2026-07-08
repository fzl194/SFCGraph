---
id: UNC@20.15.2@MMLCommand@RMV NGTAGP
type: MMLCommand
name: RMV NGTAGP（删除5G TA群组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGTAGP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGRAN跟踪区管理
- NGRAN跟踪区群组管理
status: active
---

# RMV NGTAGP（删除5G TA群组）

## 功能

**适用NF：AMF**

该命令用于删除跟踪区群组记录。

## 注意事项

- 该命令执行后立即生效。

- 删除跟踪区群组时必须首先删除该跟踪区群组下的所有成员，可执行RMV NGTAGPMEM命令进行删除。
- 删除跟踪区群组时必须保证相关表中不存在该跟踪区域群组的相关记录。可执行LST NGRANACCCTRL查看相关表的记录，基于区域基站限制接入的功能关闭或者该群组无引用时可删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTAGPID | 跟踪区群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区群组标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~256。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGTAGP]] · 5G TA群组（NGTAGP）

## 使用实例

删除一个TA群组，跟踪区群组标识为1。

```
RMV NGTAGP: NGTAGPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5G-TA群组（RMV-NGTAGP）_09732734.md`
