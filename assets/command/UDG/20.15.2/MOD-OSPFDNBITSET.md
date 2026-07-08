---
id: UDG@20.15.2@MMLCommand@MOD OSPFDNBITSET
type: MMLCommand
name: MOD OSPFDNBITSET（修改DN比特位配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFDNBITSET
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF DN比特位配置
status: active
---

# MOD OSPFDNBITSET（修改DN比特位配置）

## 功能

该命令用于修改OSPF LSA的DN位设置。

## 注意事项

- 该命令执行后立即生效。
- 只有在配置了OSPF进程后才能使用此命令。
- 仅支持在OSPF私网进程下配置，并且只在PE上生效。
- 可选参数至少选一项，并且至少禁止设置一种OSPF LSA的DN位。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| DNBITSETASEFLAG | 禁止配置ASE LSA的DN位 | 可选必选说明：可选参数<br>参数含义：禁止配置ASE LSA的DN位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| DNBITSETNSSAFLAG | 禁止配置NSSA LSA的DN位 | 可选必选说明：可选参数<br>参数含义：禁止配置NSSA LSA的DN位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| DNBITSETSUMMARYFLAG | 禁止配置Summary LSA的DN位 | 可选必选说明：可选参数<br>参数含义：禁止配置Summary LSA的DN位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| DNBITCHKASEFLAG | 禁止检查ASE LSA的DN位 | 可选必选说明：可选参数<br>参数含义：禁止检查ASE LSA的DN位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| DNBITCHKNSSAFLAG | 禁止检查NSSA LSA的DN位 | 可选必选说明：可选参数<br>参数含义：禁止检查NSSA LSA的DN位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| DNBITCHKSUMMARYFLAG | 禁止检查Summary LSA的DN位 | 可选必选说明：可选参数<br>参数含义：禁止检查Summary LSA的DN位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [DN比特位配置（OSPFDNBITSET）](configobject/UDG/20.15.2/OSPFDNBITSET.md)

## 使用实例

使能OSPF进程1下设置AS-external-LSA的DN位：

```
MOD OSPFDNBITSET:PROCID=1,DNBITSETASEFLAG=TRUE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改DN比特位配置（MOD-OSPFDNBITSET）_49802238.md`
