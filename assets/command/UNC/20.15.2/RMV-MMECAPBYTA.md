---
id: UNC@20.15.2@MMLCommand@RMV MMECAPBYTA
type: MMLCommand
name: RMV MMECAPBYTA（删除基于跟踪区的MME相对权重配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MMECAPBYTA
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- 基于跟踪区的MME相对权重
status: active
---

# RMV MMECAPBYTA（删除基于跟踪区的MME相对权重配置）

## 功能

**适用网元：MME**

此命令用于删除指定跟踪区下，本MME在MME Pool区内的相对权重值。

## 注意事项

- 此命令执行后立即生效。
- 删除指定跟踪区的相对权重值配置，针对这些跟踪区下的eNodeB，将使用SET SYS命令的设备能力参数取值。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMECAPBYTA]] · 基于跟踪区的MME相对权重配置（MMECAPBYTA）

## 使用实例

删除跟踪区123030200对应的相对权重配置：

RMV MMECAPBYTA: MCC="123", MNC="03", TAC="0x200";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MMECAPBYTA.md`
