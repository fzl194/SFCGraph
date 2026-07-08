---
id: UDG@20.15.2@MMLCommand@LST NGBINDDFSRPAIR
type: MMLCommand
name: LST NGBINDDFSRPAIR（查询5G LAN实例绑定双发选收结对配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NGBINDDFSRPAIR
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN双发选收配置
- 5G LAN实例绑定双发选收结对
status: active
---

# LST NGBINDDFSRPAIR（查询5G LAN实例绑定双发选收结对配置）

## 功能

**适用NF：UPF**

该命令用于查询双发选收结对与5G LAN会话实例绑定记录。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为18～37。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NGBINDDFSRPAIR]] · 5G LAN实例绑定双发选收结对配置（NGBINDDFSRPAIR）

## 使用实例

显示双发选收结对绑定5G LAN会话实例的记录：

```
LST NGBINDDFSRPAIR:;
```

```

```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-NGBINDDFSRPAIR.md`
