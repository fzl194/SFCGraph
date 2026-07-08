---
id: UDG@20.15.2@MMLCommand@RMV PAEPERFMODE
type: MMLCommand
name: RMV PAEPERFMODE（删除配置表中的PAE性能模式）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PAEPERFMODE
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 性能模式
status: active
---

# RMV PAEPERFMODE（删除配置表中的PAE性能模式）

## 功能

该命令用于删除配置表中的PAE性能模式。

> **说明**
> 该命令执行后需要重新启动系统才能生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | Pod类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定POD类型，可以通过使用命令<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>PODTYPE数值来源为DSP POD命令的查询结果。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAEPERFMODE]] · 配置表中的PAE性能模式（PAEPERFMODE）

## 使用实例

删除配置表中的PAE性能模式

```
+++    UNC/*MEID:0 MENAME:unc*/        2024-05-20 18:54:35
O&M    #75
%%RMV PAEPERFMODE: PODTYPE="sfpod";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除配置表中的PAE性能模式（RMV-PAEPERFMODE）_41355453.md`
