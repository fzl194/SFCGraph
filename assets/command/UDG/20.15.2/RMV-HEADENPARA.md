---
id: UDG@20.15.2@MMLCommand@RMV HEADENPARA
type: MMLCommand
name: RMV HEADENPARA（删除头增强参数）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HEADENPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- 头增强参数
status: active
---

# RMV HEADENPARA（删除头增强参数）

## 功能

**适用NF：PGW-U、UPF**

![](删除头增强参数（RMV HEADENPARA）_13700305.assets/notice_3.0-zh-cn.png)

本命令属于高危命令,执行本命令后将删除指定或所有头增强的参数配置，将头增强相关参数设置为默认值，可能导致头增强对外呈现发生变化，请谨慎使用。

该命令用来删除头增强配置的相关参数。用于取消用户相应的头增强参数配置。

## 注意事项

- 该命令执行后立即生效。
- 删除HeadEn配置会同时删除对应的HeadenPara配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HEADERENNAME | 头增强名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置头增强名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD HEADEN命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HEADENPARA]] · 头增强参数（HEADENPARA）

## 使用实例

假如运营商想删除名称为“headen1”的头增强配置参数记录：

```
RMV HEADENPARA:HEADERENNAME="headen1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-HEADENPARA.md`
