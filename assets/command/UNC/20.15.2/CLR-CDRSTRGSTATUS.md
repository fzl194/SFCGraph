---
id: UNC@20.15.2@MMLCommand@CLR CDRSTRGSTATUS
type: MMLCommand
name: CLR CDRSTRGSTATUS（清除话单缓存目录状态）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: CDRSTRGSTATUS
command_category: 动作类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费缓存
- 缓存目录
status: active
---

# CLR CDRSTRGSTATUS（清除话单缓存目录状态）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来清除话单缓存目录状态的记录。对于目录状态是锁定的目录不会清除，请执行前将预期清除的记录先置为解锁状态。

## 注意事项

- 该命令执行后立即生效。
- 目录状态被标记位“锁定”的记录不会被清除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRSTRGSTATUS]] · 话单缓存目录状态（CDRSTRGSTATUS）

## 使用实例

清除话单缓存目录状态记录：

```
CLR CDRSTRGSTATUS: PODNAME="PodName";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-CDRSTRGSTATUS.md`
