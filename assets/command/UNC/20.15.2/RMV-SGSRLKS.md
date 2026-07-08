---
id: UNC@20.15.2@MMLCommand@RMV SGSRLKS
type: MMLCommand
name: RMV SGSRLKS（删除SGS服务端链路集）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SGSRLKS
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
- SGS服务端链路集
status: active
---

# RMV SGSRLKS（删除SGS服务端链路集）

## 功能

**适用NF：SMSF**

此命令用于删除SGS服务端链路集配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSX | 链路集索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定链路集的索引。<br>数据来源：本端规划<br>取值范围：0~2000<br>默认值：无 |

## 操作的配置对象

- [SGS服务端链路集（SGSRLKS）](configobject/UNC/20.15.2/SGSRLKS.md)

## 使用实例

1. 删除链路集索引为0的SGS服务端链路集配置，可以用如下命令：
  ```
  RMV SGSRLKS: LSX=0;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SGS服务端链路集-(RMV-SGSRLKS)_50427734.md`
