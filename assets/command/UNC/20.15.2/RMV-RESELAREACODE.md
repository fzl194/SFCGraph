---
id: UNC@20.15.2@MMLCommand@RMV RESELAREACODE
type: MMLCommand
name: RMV RESELAREACODE（删除AMF重选功能区域编码）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RESELAREACODE
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF区域重选功能管理
- AMF重选功能区域编码
status: active
---

# RMV RESELAREACODE（删除AMF重选功能区域编码）

## 功能

**适用NF：AMF**

该命令用于删除AMF重选功能的区域编码。

## 注意事项

- 该命令执行后立即生效。

- 删除前请确保RESELAREACODE在ADD RESELAREAMEM和ADD NGAREARESELPLCY中没有被引用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESELAREACODE | AMF重选功能区域编码 | 可选必选说明：必选参数<br>参数含义：该参数用于唯一标识AMF服务的某个区域，该区域由一个或者若干个跟踪区组成。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RESELAREACODE]] · AMF重选功能区域编码（RESELAREACODE）

## 使用实例

删除编码为“ReSelZone”的区域定义，执行如下命令：

```
RMV RESELAREACODE: RESELAREACODE="ReSelZone";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RESELAREACODE.md`
