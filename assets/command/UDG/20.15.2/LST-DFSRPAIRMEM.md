---
id: UDG@20.15.2@MMLCommand@LST DFSRPAIRMEM
type: MMLCommand
name: LST DFSRPAIRMEM（查询双发选收结对成员配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DFSRPAIRMEM
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN双发选收配置
- 双发选收结对成员配置
status: active
---

# LST DFSRPAIRMEM（查询双发选收结对成员配置）

## 功能

**适用NF：UPF**

该命令用于查询双发选收结对IMSI成员记录。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DFSRPAIRID | 双发选收结对ID | 可选必选说明：可选参数<br>参数含义：该参数用于配置双发选收结对ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1-2048。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [双发选收结对成员配置（DFSRPAIRMEM）](configobject/UDG/20.15.2/DFSRPAIRMEM.md)

## 使用实例

显示所有双发选收结对下的成员：

```
LST DFSRPAIRMEM:;
```

```

```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询双发选收结对成员配置（LST-DFSRPAIRMEM）_26514781.md`
