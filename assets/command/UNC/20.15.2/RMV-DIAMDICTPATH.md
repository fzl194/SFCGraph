---
id: UNC@20.15.2@MMLCommand@RMV DIAMDICTPATH
type: MMLCommand
name: RMV DIAMDICTPATH（删除Diameter字典加载路径）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV DIAMDICTPATH（删除Diameter字典加载路径）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除Diameter字典加载路径。

## 注意事项

- 该命令执行后立即生效。
- 对于第一套字典执行RMV命令时，表示第一套字典加载路径恢复为EPC标准字典加载路径。
- 对于第二套字典执行RMV命令时，表示第二套字典加载路径被删除。
- 当GY应用的第二套字典绑定到DCCTEMPLATE时，无法删除对应的字典路径。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATION | 应用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定字典的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GY：Gy接口字典。<br>- GX：Gx接口字典。<br>- S6B：S6b接口字典。<br>默认值：无<br>配置原则：无 |
| DICTNO | 字典序号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定字典编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DIAMDICTPATH]] · Diameter字典加载路径（DIAMDICTPATH）

## 使用实例

- 当需要将GX应用的第一套字典加载路径恢复成EPC标准字典时：
  ```
  RMV DIAMDICTPATH: APPLICATION=GX,DICTNO=1;
  ```
- 当需要将GY应用的第二套字典加载路径删除时：
  ```
  RMV DIAMDICTPATH: APPLICATION=GY,DICTNO=2;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DIAMDICTPATH.md`
