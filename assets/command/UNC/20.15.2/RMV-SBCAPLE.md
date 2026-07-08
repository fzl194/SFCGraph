---
id: UNC@20.15.2@MMLCommand@RMV SBCAPLE
type: MMLCommand
name: RMV SBCAPLE（删除SBCAP本地实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SBCAPLE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- SBCAP本地实体
status: active
---

# RMV SBCAPLE（删除SBCAP本地实体）

## 功能

**适用网元：MME**

该命令用于删除SBc链路本地实体。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，会导致和此本地实体相连的CBC网元链路中断。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LLEINDEX | 本端实体号 | 可选必选说明：必选参数<br>参数含义：待删除的SBc链路本地实体号。<br>取值范围：0～127<br>默认值：无<br>说明：可以通过<br>[**LST SBCAPLE**](查询SBCAP本地实体(LST SBCAPLE)_26146378.md)<br>命令查看已有配置，确认所要删除的SBc链路的索引。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBCAPLE]] · SBCAP本地实体（SBCAPLE）

## 使用实例

删除一个SBc链路本地实体：

RMV SBCAPLE: LLEINDEX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SBCAPLE.md`
