---
id: UNC@20.15.2@MMLCommand@SET UPRESELECTFUNC
type: MMLCommand
name: SET UPRESELECTFUNC（设置UP重选功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: UPRESELECTFUNC
command_category: 配置类
applicable_nf:
- SMF
- GGSN
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF重选
status: active
---

# SET UPRESELECTFUNC（设置UP重选功能）

## 功能

**适用NF：SMF、GGSN、PGW-C**

该命令用于修改UP重选相关的功能控制，如触发UP重选的场景。

## 注意事项

- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPRESELSCENE | UP重选场景 | 可选必选说明：可选参数<br>参数含义：该参数用来配置触发UP重选的场景。<br>数据来源：全网规划<br>取值范围：<br>- SMFALLOCIPFAULT（SMF分配地址失败）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPRESELECTFUNC查询当前参数配置值。<br>配置原则：<br>当SMF、PGW-C或GGSN-C本地分配地址失败，期望进行UP重选时，则勾选“SMFALLOCIPFAULT”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPRESELECTFUNC]] · UP重选功能（UPRESELECTFUNC）

## 使用实例

设置触发UP重选的场景为C面分地址失败：

```
SET UPRESELECTFUNC:UPRESELSCENE=SMFALLOCIPFAULT-1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置UP重选功能（SET-UPRESELECTFUNC）_95141456.md`
