---
id: UNC@20.15.2@MMLCommand@RMV SBCAPLNK
type: MMLCommand
name: RMV SBCAPLNK（删除SBc链路）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SBCAPLNK
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
- SBc链路
status: active
---

# RMV SBCAPLNK（删除SBc链路）

## 功能

**适用网元：MME**

该命令用于删除一条MME作为客户端的SBc链路。

## 注意事项

- 该命令执行后立即生效。
- 如果链路被删除，将导致业务中断。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNKINDEX | 链路索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要删除的SBc链路号。<br>取值范围：0~127<br>默认值：无<br>说明：可以通过<br>[**LST SBCAPLNK**](查询SBc链路(LST SBCAPLNK)_26306186.md)<br>命令查看已有配置，确认所要删除的SBc链路的索引。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SBCAPLNK]] · SBc链路（SBCAPLNK）

## 使用实例

删除链路号为0的SBc链路：

RMV SBCAPLNK: LNKINDEX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SBCAPLNK.md`
