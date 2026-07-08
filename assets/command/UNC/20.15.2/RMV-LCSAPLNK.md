---
id: UNC@20.15.2@MMLCommand@RMV LCSAPLNK
type: MMLCommand
name: RMV LCSAPLNK（删除LCSAP链路配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LCSAPLNK
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- LCSAP链路配置
status: active
---

# RMV LCSAPLNK（删除LCSAP链路配置）

## 功能

**适用网元：MME**

此命令用于删除LCSAP链路配置。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKIDX | 链路索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定链路索引。<br>取值范围：0～23<br>默认值：无 |

## 操作的配置对象

- [LCSAP链路配置（LCSAPLNK）](configobject/UNC/20.15.2/LCSAPLNK.md)

## 使用实例

删除一条 “链路索引” 为 “1” 的LCSAP链路配置记录：

RMV LCSAPLNK: LINKIDX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除LCSAP链路配置(RMV-LCSAPLNK)_26145808.md`
