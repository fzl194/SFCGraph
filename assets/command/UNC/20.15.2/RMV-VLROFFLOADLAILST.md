---
id: UNC@20.15.2@MMLCommand@RMV VLROFFLOADLAILST
type: MMLCommand
name: RMV VLROFFLOADLAILST（删除位置区列表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: VLROFFLOADLAILST
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- MSC POOL管理
- 基于LAI的IMSI分离配置信息
status: active
---

# RMV VLROFFLOADLAILST（删除位置区列表）

## 功能

**适用网元：MME**

本命令用于删除指定的LAI。

## 注意事项

- 该命令执行后立即生效。
- 若未输入参数，表示删除所有记录。
- 如果在对4G用户执行IMSI分离操作任务期间（可通过[**DSP VLROFFLOADBYLAI**](../基于LAI的IMSI分离业务/显示IMSI分离4G用户任务运行状态(DSP VLROFFLOADBYLAI)_26145426.md)查询）执行本命令，系统仍然会对已删除的LAI对应TAI下联合附着的4G用户执行IMSI分离操作，直到当前任务结束。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LAI | LAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区标识，标识一个位置区。<br>数据来源：整网规划<br>取值范围：9～10位的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLROFFLOADLAILST]] · 位置区列表（VLROFFLOADLAILST）

## 使用实例

1. 从LAI列表中删除一个LAI，LAI的值为“308010001”：
  RMV VLROFFLOADLAILST: LAI="308010001";
2. 从LAI列表中删除所有LAI：
  RMV VLROFFLOADLAILST:;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除位置区列表(RMV-VLROFFLOADLAILST)_72345029.md`
