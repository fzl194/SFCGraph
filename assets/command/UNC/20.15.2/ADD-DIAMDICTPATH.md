---
id: UNC@20.15.2@MMLCommand@ADD DIAMDICTPATH
type: MMLCommand
name: ADD DIAMDICTPATH（增加Diameter字典加载路径）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DIAMDICTPATH
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 5
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter字典管理
- 加载路径
status: active
---

# ADD DIAMDICTPATH（增加Diameter字典加载路径）

## 功能

**适用NF：PGW-C、SMF**

该命令用于增加Diameter字典加载路径。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为5。
- 只有为某应用增加第二套字典加载路径时，才会使用该命令。
- 目前只支持GY应用设置第二套字典加载路径。
- 该命令执行后，再执行加载字典命令（LOD DIAMDICT）。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | APPLICATION | DICTNO | DICTPATH |
| --- | --- | --- | --- |
| 初始值 | GY | 1 | EPC_STANDARD |
| 初始值 | GX | 1 | EPC970_STANDARD |
| 初始值 | S6B | 1 | EPC_STANDARD |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATION | 应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定字典的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GY：Gy接口字典。<br>- GX：Gx接口字典。<br>- S6B：S6b接口字典。<br>默认值：无<br>配置原则：无 |
| DICTNO | 字典序号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定字典编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2。<br>默认值：无<br>配置原则：无 |
| DICTPATH | 字典加载路径 | 可选必选说明：必选参数<br>参数含义：该参数用于指定字典加载路径。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- EPC_STANDARD：EPC标准字典路径。<br>- GU_STANDARD：GU标准字典路径。<br>- CUSTOM1：定制字典路径1。<br>- CUSTOM2：定制字典路径2。<br>- EPC970_STANDARD：EPC 970 标准字典路径。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [Diameter字典加载路径（DIAMDICTPATH）](configobject/UNC/20.15.2/DIAMDICTPATH.md)

## 使用实例

当需要为GY应用增加第二套字典加载路径时：

```
ADD DIAMDICTPATH: APPLICATION=GY,DICTNO=2,DICTPATH=CUSTOM2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Diameter字典加载路径（ADD-DIAMDICTPATH）_09897247.md`
