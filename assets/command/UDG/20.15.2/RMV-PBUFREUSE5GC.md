---
id: UDG@20.15.2@MMLCommand@RMV PBUFREUSE5GC
type: MMLCommand
name: RMV PBUFREUSE5GC（删除pbuf重用检测开关设置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PBUFREUSE5GC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
- PBUF
status: active
---

# RMV PBUFREUSE5GC（删除pbuf重用检测开关设置）

## 功能

此命令用于删除MSS的pbuf重用检测开关设置，恢复未设置时的默认状态。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | pod类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定pod类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |
| POOLNAME | 内存池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定内存池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PBUFREUSE5GC]] · pbuf重用检测开关设置（PBUFREUSE5GC）

## 使用实例

通过如下命令删除podtype为aa的pod内PAE内存池的pbuf重用检测开关设置：

```
RMV PBUFREUSE5GC:PODTYPE="aa",POOLNAME="PAE";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-PBUFREUSE5GC.md`
