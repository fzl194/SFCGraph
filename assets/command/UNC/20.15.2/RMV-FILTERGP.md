---
id: UNC@20.15.2@MMLCommand@RMV FILTERGP
type: MMLCommand
name: RMV FILTERGP（删除过滤组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: FILTERGP
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- 过滤器组管理
status: active
---

# RMV FILTERGP（删除过滤组）

## 功能

**适用NF：SMF**

该命令用于删除过滤组。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILTERGPID | 过滤组ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定过滤组唯一标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FILTERGP]] · 过滤组（FILTERGP）

## 使用实例

删除指定过滤组ID是1的过滤组：

```
RMV FILTERGP: FILTERGPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除过滤组（RMV-FILTERGP）_09651780.md`
