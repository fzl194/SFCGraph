---
id: UNC@20.15.2@MMLCommand@RMV DMRT
type: MMLCommand
name: RMV DMRT（删除Diameter域路由配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DMRT
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
- Diameter路由
status: active
---

# RMV DMRT（删除Diameter域路由配置）

## 功能

![](删除Diameter域路由配置(RMV DMRT)_72345889.assets/notice_3.0-zh-cn_2.png)

删除Diameter域路由配置将导致通过该域路由连接的对端的Diameter链路发生中断。

**适用网元：SGSN、MME**

该命令用于删除一条Diameter域路由。

## 注意事项

- 该命令执行后立即生效。
- 删除该域路由，将导致通过该域路由连接的对端的Diameter链路发生中断。
- 如果Diameter域路由满足以下两个条件：
    1. Diameter路由组引用该域路由索引；
    2. 相同域路由索引的记录只有1条；
  则该记录不能删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROUTEIDX | 路由索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter域路由索引。<br>取值范围：0~2047<br>默认值：无<br>说明：可以通过<br>[**LST DMRT**](查询Diameter域路由配置(LST DMRT)_72225969.md)<br>命令查看已有配置，确认所要删除的Diameter域路由的索引。 |
| PEERIDX | 对端实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对等端索引，用于标识目的对等端。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD DMPE**](../Diameter对端实体/增加Diameter对端实体(ADD DMPE)_72225963.md)<br>设置此参数。<br>取值范围：0~639<br>默认值：无<br>说明：一个路由索引最多可配置10个对等端索引。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMRT]] · Diameter域路由配置（DMRT）

## 使用实例

删除索引号为0的Diameter域路由：

RMV DMRT: ROUTEIDX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DMRT.md`
