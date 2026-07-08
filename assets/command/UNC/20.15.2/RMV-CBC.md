---
id: UNC@20.15.2@MMLCommand@RMV CBC
type: MMLCommand
name: RMV CBC（删除CBC）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CBC
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
- CBC配置
status: active
---

# RMV CBC（删除CBC）

## 功能

**适用网元：MME**

此命令用于删除CBC配置。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令前，需要提前在UNCMML窗口上执行命令[**RMV SBCAPLNK**](../SBc链路/删除SBc链路(RMV SBCAPLNK)_26146374.md)，删除SBc链路中引用此CBC的链路。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CBCIDX | CBC索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除的CBC的索引。<br>数据来源：本端规划<br>取值范围：0~127<br>默认值：无<br>说明：可以通过<br>[**LST CBC**](查询CBC(LST CBC)_26146372.md)<br>命令查看已有配置，确认所要修改的CBC的索引。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CBC]] · CBC（CBC）

## 使用实例

删除一个索引为0的CBC配置:

RMV CBC: CBCIDX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CBC.md`
