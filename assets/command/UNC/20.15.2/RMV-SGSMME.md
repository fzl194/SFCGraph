---
id: UNC@20.15.2@MMLCommand@RMV SGSMME
type: MMLCommand
name: RMV SGSMME（删除SGS MME实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SGSMME
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- SGS MME实体
status: active
---

# RMV SGSMME（删除SGS MME实体）

## 功能

**适用NF：SMSF**

该命令用于删除SGS MME实体指定配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEX | MME索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个MME实体，在全局范围内唯一。<br>数据来源：本端规划<br>取值范围：0～1999。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGSMME]] · SGS MME实体（SGSMME）

## 使用实例

删除MME索引为1的SGS MME实体。

```
RMV SGSMME: MMEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SGSMME.md`
