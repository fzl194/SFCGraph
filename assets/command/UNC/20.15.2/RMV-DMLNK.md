---
id: UNC@20.15.2@MMLCommand@RMV DMLNK
type: MMLCommand
name: RMV DMLNK（删除Diameter链路配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DMLNK
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter链路
status: active
---

# RMV DMLNK（删除Diameter链路配置）

## 功能

![](删除Diameter链路配置(RMV DMLNK)_26306086.assets/notice_3.0-zh-cn_2.png)

删除该链路，将导致其他链路的负荷增大。如果同一链路集下的所有链路都被删除，将导致业务中断。

**适用网元：SGSN、MME**

该命令用于删除一条Diameter链路。

## 注意事项

- 该命令执行后立即生效。
- 删除该链路，将导致该链路上的业务倒换到同一链路集下的其他链路上，从而使其他链路的负荷增大。
- 如果同一链路集下的所有链路都被删除，将导致业务中断。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKIDX | 链路索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定准备删除的Diameter链路的索引。<br>取值范围：0~1279<br>默认值：无<br>说明：可以通过<br>[**LST DMLNK**](查询Diameter链路配置(LST DMLNK)_26146276.md)<br>命令查看已有配置，确认所要删除的Diameter链路的索引。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMLNK]] · Diameter链路配置（DMLNK）

## 使用实例

删除链路索引为0的Diameter链路：

RMV DMLNK: LINKIDX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Diameter链路配置(RMV-DMLNK)_26306086.md`
