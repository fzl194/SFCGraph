---
id: UDG@20.15.2@MMLCommand@ADD UPDIAMDICTPATH
type: MMLCommand
name: ADD UPDIAMDICTPATH（增加Diameter字典加载路径）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPDIAMDICTPATH
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 5
category_path:
- 用户面服务管理
- Diameter管理
- Diameter字典管理
- 加载路径
status: active
---

# ADD UPDIAMDICTPATH（增加Diameter字典加载路径）

## 功能

**适用NF：UPF**

该命令用于增加Diameter字典加载路径。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为5。
- 该命令相关的功能当前版本暂不支持。
- 只有为某应用增加第二套字典加载路径时，才会使用该命令。
- 该命令执行后，再执行加载字典命令（LOD UPDIAMDICT）。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | APPLICATION | DICTNO | DICTPATH |
| --- | --- | --- | --- |
| 初始值 | SWM | 1 | EPC_STANDARD |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATION | 应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定字典的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：无 |
| DICTNO | 字典序号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定字典编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1。<br>默认值：无<br>配置原则：无 |
| DICTPATH | 字典加载路径 | 可选必选说明：必选参数<br>参数含义：该参数用于指定字典加载路径。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- EPC_STANDARD：EPC标准字典路径。<br>- CUSTOM1：定制字典路径1。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPDIAMDICTPATH]] · Diameter字典加载路径（UPDIAMDICTPATH）

## 使用实例

当需要为SWM应用增加第二套字典加载路径时：

```
ADD UPDIAMDICTPATH: APPLICATION=SWM, DICTNO=1, DICTPATH=EPC_STANDARD;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-UPDIAMDICTPATH.md`
