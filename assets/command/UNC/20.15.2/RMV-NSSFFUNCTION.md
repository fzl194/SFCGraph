---
id: UNC@20.15.2@MMLCommand@RMV NSSFFUNCTION
type: MMLCommand
name: RMV NSSFFUNCTION（删除NSSF功能实例信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NSSFFUNCTION
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- NSSF性能对象管理
status: active
---

# RMV NSSFFUNCTION（删除NSSF功能实例信息）

## 功能

**适用NF：NSSF**

该命令用于删除NSSF功能实例信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | NSSF功能实例号 | 可选必选说明：必选参数<br>参数含义：NSSF功能实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NSSF功能实例信息（NSSFFUNCTION）](configobject/UNC/20.15.2/NSSFFUNCTION.md)

## 使用实例

删除NSSF功能实体号为Instanceid01的NSSF功能实例信息。

```
RMV NSSFFUNCTION:INSTANCEID="Instanceid01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NSSF功能实例信息（RMV-NSSFFUNCTION）_09653801.md`
