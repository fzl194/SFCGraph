---
id: UNC@20.15.2@MMLCommand@MOD MMECAPBYTA
type: MMLCommand
name: MOD MMECAPBYTA（修改基于跟踪区的MME相对权重配置）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD MMECAPBYTA（修改基于跟踪区的MME相对权重配置）

## 功能

**适用网元：MME**

此命令用于修改指定跟踪区下，本MME在MME Pool区内的相对权重值。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| CAP | 相对权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定此跟踪区下，MME负荷能力在MME Pool区中的相对权重值。<br>数据来源：整网规划<br>取值范围：整数类型，取值范围为0~255。<br>默认值：无 |

## 操作的配置对象

- [基于跟踪区的MME相对权重配置（MMECAPBYTA）](configobject/UNC/20.15.2/MMECAPBYTA.md)

## 使用实例

修改跟踪区123030200的相对权重为100：

MOD MMECAPBYTA: MCC="123", MNC="03", TAC="0x200", CAP=100;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于跟踪区的MME相对权重配置(MOD-MMECAPBYTA)_26146266.md`
