---
id: UDG@20.15.2@MMLCommand@RMV UPDIAMDICTPATH
type: MMLCommand
name: RMV UPDIAMDICTPATH（删除Diameter字典加载路径）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UPDIAMDICTPATH
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter管理
- Diameter字典管理
- 加载路径
status: active
---

# RMV UPDIAMDICTPATH（删除Diameter字典加载路径）

## 功能

**适用NF：UPF**

![](删除Diameter字典加载路径（RMV UPDIAMDICTPATH）_97314551.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会删除Diameter字典加载路径，可能影响下一次字典加载。

该命令用于删除Diameter字典加载路径。

## 注意事项

- 该命令执行后立即生效。
- 对于第一套字典执行RMV命令时，表示第一套字典加载路径恢复为EPC标准字典加载路径。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATION | 应用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定字典的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：无 |
| DICTNO | 字典序号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定字典编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [Diameter字典加载路径（UPDIAMDICTPATH）](configobject/UDG/20.15.2/UPDIAMDICTPATH.md)

## 使用实例

当需要将SWM应用的第一套字典加载路径恢复成EPC标准字典时：

```
RMV UPDIAMDICTPATH: APPLICATION=SWM, DICTNO=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除Diameter字典加载路径（RMV-UPDIAMDICTPATH）_97314551.md`
