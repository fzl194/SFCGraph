---
id: UDG@20.15.2@MMLCommand@SET SGLPASSPERIOD
type: MMLCommand
name: SET SGLPASSPERIOD（设置单通检测周期）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SGLPASSPERIOD
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- 网络侧连通性检测
- 单通检测周期
status: active
---

# SET SGLPASSPERIOD（设置单通检测周期）

## 功能

**适用NF：PGW-U、UPF**

配置单通故障检测时间周期。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 修改单通故障检测的时间周期后，检测按照新的周期重新开始，检测结果按照新的检测周期产生的单通故障检测结果呈现。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | PERIOD |
| --- | --- |
| 初始值 | 10 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PERIOD | 周期 | 可选必选说明：必选参数<br>参数含义：配置单通故障检测周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～300，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SGLPASSPERIOD]] · 单通检测周期（SGLPASSPERIOD）

## 使用实例

配置单通故障检测时间周期为20秒：

```
SET SGLPASSPERIOD: PERIOD=20;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SGLPASSPERIOD.md`
