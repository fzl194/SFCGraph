---
id: UNC@20.15.2@MMLCommand@MOD DIAMDICTPATH
type: MMLCommand
name: MOD DIAMDICTPATH（修改Diameter字典加载路径）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DIAMDICTPATH
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter字典管理
- 加载路径
status: active
---

# MOD DIAMDICTPATH（修改Diameter字典加载路径）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改Diameter字典加载路径。

## 注意事项

- 该命令执行后立即生效。
- 目前只有GY应用支持设置第二套字典加载路径。
- 该命令执行后，再执行加载字典命令（LOD DIAMDICT）。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATION | 应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定字典的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GY：Gy接口字典。<br>- GX：Gx接口字典。<br>- S6B：S6b接口字典。<br>默认值：无<br>配置原则：无 |
| DICTNO | 字典序号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定字典编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2。<br>默认值：无<br>配置原则：无 |
| DICTPATH | 字典加载路径 | 可选必选说明：必选参数<br>参数含义：该参数用于指定字典加载路径。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- EPC_STANDARD：EPC标准字典路径。<br>- GU_STANDARD：GU标准字典路径。<br>- CUSTOM1：定制字典路径1。<br>- CUSTOM2：定制字典路径2。<br>- EPC970_STANDARD：EPC 970 标准字典路径。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIAMDICTPATH]] · Diameter字典加载路径（DIAMDICTPATH）

## 使用实例

当需要为GX应用的第一套字典加载路径修改为定制字典路径时：

```
MOD DIAMDICTPATH: APPLICATION=GX,DICTNO=1,DICTPATH=CUSTOM1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DIAMDICTPATH.md`
