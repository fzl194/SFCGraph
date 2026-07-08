---
id: UNC@20.15.2@MMLCommand@RMV VPROBEIP
type: MMLCommand
name: RMV VPROBEIP（删除vProbe报表本地IP资源池）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: VPROBEIP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- vProbe管理
- vProbe本地IP
status: active
---

# RMV VPROBEIP（删除vProbe报表本地IP资源池）

## 功能

该命令用于删除vProbe的报表本地IP资源池。

## 注意事项

- 该命令执行后立即生效。

- 执行命令前请确认vProbe服务处于上线状态，可通过DSP FUNCTIONSETINFO命令查询确认。
- 删除报表的IP资源池后，报表数据将无法上报至服务器。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定记录索引号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [vProbe报表本地IP资源池（VPROBEIP）](configobject/UNC/20.15.2/VPROBEIP.md)

## 使用实例

运营商A不再使用索引为3的本地IP资源池记录，将该条记录删除：

```
RMV VPROBEIP: INDEX=3;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除vProbe报表本地IP资源池（RMV-VPROBEIP）_88563612.md`
