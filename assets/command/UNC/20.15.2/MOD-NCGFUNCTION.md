---
id: UNC@20.15.2@MMLCommand@MOD NCGFUNCTION
type: MMLCommand
name: MOD NCGFUNCTION（修改NCG功能实例信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NCGFUNCTION
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- NCG性能对象管理
status: active
---

# MOD NCGFUNCTION（修改NCG功能实例信息）

## 功能

**适用NF：NCG**

该命令用于修改NCG功能实例信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | NF实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |
| CDRPROCCAP | 话单处理容量 | 可选必选说明：可选参数<br>参数含义：该参数用于指定话单处理容量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2147483647，单位是条。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCGFUNCTION]] · NCG功能实例信息（NCGFUNCTION）

## 使用实例

修改NF实例号为"a"的NCG功能实例信息的话单处理容量为900：

```
MOD NCGFUNCTION: INSTANCEID="a", CDRPROCCAP=900;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NCGFUNCTION.md`
