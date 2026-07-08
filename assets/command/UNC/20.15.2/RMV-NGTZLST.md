---
id: UNC@20.15.2@MMLCommand@RMV NGTZLST
type: MMLCommand
name: RMV NGTZLST（删除5G多时区参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGTZLST
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 多时区管理
- 5G多时区参数
status: active
---

# RMV NGTZLST（删除5G多时区参数）

## 功能

**适用NF：AMF**

该命令用于删除位置区对应的时区和夏令时信息。

## 注意事项

- 该命令执行后立即生效。

- 删除前请确保当前时区标识在ADD NGAREATZ中没有被引用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TZID | 时区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待增加时区的索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~24。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGTZLST]] · 5G多时区参数（NGTZLST）

## 使用实例

删除“时区标识”为“1”的时区和夏令时配置信息，执行如下命令：

```
RMV NGTZLST: TZID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGTZLST.md`
