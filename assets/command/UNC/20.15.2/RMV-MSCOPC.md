---
id: UNC@20.15.2@MMLCommand@RMV MSCOPC
type: MMLCommand
name: RMV MSCOPC（删除MSC信令点）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MSCOPC
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
- MSC管理
status: active
---

# RMV MSCOPC（删除MSC信令点）

## 功能

**适用NF：SMSF**

该命令用于删除MSC本局信令点指定配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPX | MSC信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MSC本局信令点索引。<br>数据来源：本端规划<br>取值范围：1~2<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSCOPC]] · MSC信令点（MSCOPC）

## 使用实例

删除MSC信令点索引为1的MSC信令点。

```
RMV MSCOPC: OPX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MSCOPC.md`
