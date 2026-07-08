---
id: UNC@20.15.2@MMLCommand@RMV M2MSIGCTRL
type: MMLCommand
name: RMV M2MSIGCTRL（删除M2M信令控制配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: M2MSIGCTRL
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
- M2M管理
- M2M信令控制
status: active
---

# RMV M2MSIGCTRL（删除M2M信令控制配置）

## 功能

**适用网元：MME**

该命令用于删除M2M用户的信令控制。

## 注意事项

- 该命令执行后立即生效。
- 如果待删除记录被[**ADD M2MPLCY**](../M2M策略参数配置/增加M2M策略参数(ADD M2MPLCY)_72225443.md)配置引用，则不能删除

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFGINDEX | 配置索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定信令控制策略的索引。<br>数据来源：本端规划<br>取值范围：0～31<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M2MSIGCTRL]] · M2M信令控制配置（M2MSIGCTRL）

## 使用实例

删除 *配置索引* 为 “1” 的M2M信令控制配置记录。

RMV M2MSIGCTRL: CFGINDEX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除M2M信令控制配置(RMV-M2MSIGCTRL)_72345367.md`
