---
id: UDG@20.15.2@MMLCommand@RMV UDGNRMINTF
type: MMLCommand
name: RMV UDGNRMINTF（删除逻辑口）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UDGNRMINTF
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 逻辑接口管理
- 逻辑接口配置
- 备份逻辑接口
status: active
---

# RMV UDGNRMINTF（删除逻辑口）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除逻辑口记录。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTNAME | 保留逻辑接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置保留的逻辑接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UDGNRMINTF]] · 逻辑口（UDGNRMINTF）

## 使用实例

假设需要删除名称为pgwusxif的逻辑口记录，配置如下：

```
RMV UDGNRMINTF: INTNAME="pgwusxif";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-UDGNRMINTF.md`
