---
id: UDG@20.15.2@MMLCommand@RMV TWAMPLOGICINF
type: MMLCommand
name: RMV TWAMPLOGICINF（删除本地逻辑接口）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TWAMPLOGICINF
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- 本端逻辑接口配置
status: active
---

# RMV TWAMPLOGICINF（删除本地逻辑接口）

## 功能

该命令用于删除本地逻辑接口。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 逻辑接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置逻辑接口名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TWAMPLOGICINF]] · 本地逻辑接口（TWAMPLOGICINF）

## 使用实例

删除逻辑接口名称为：n3if1/1/0的实例：

```
RMV TWAMPLOGICINF: NAME="n3if1/1/0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-TWAMPLOGICINF.md`
