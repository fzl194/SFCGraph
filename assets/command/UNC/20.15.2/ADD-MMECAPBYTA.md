---
id: UNC@20.15.2@MMLCommand@ADD MMECAPBYTA
type: MMLCommand
name: ADD MMECAPBYTA（增加基于跟踪区的MME相对权重配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MMECAPBYTA
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 20000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- 基于跟踪区的MME相对权重
status: active
---

# ADD MMECAPBYTA（增加基于跟踪区的MME相对权重配置）

## 功能

**适用网元：MME**

此命令用于配置指定跟踪区下，本MME的MME负荷能力在MME Pool区内的相对权重值。

当针对不同的跟踪区，向eNodeB下发不同的MME负荷能力，需要执行此命令。

## 注意事项

- 当一个eNodeB在S1 Setup Request消息中携带多个TAI时，不建议使用该命令，MME下发的相对权重可能匹配错误。
- 此命令执行后立即生效。
- 此命令最大记录数为20000。
- 配置此命令后，系统会根据跟踪区匹配本配置记录，成功后优先使用本命令配置的相对权重参数取值，匹配失败则使用SET SYS命令配置的设备能力参数值。
- 当SET SYS配置的设备能力参数取值为0，则MME会向整系统内所有的eNodeB下发负荷能力为0的值，以供应急场景使用，例如执行MME Pool用户迁移将所有用户迁出。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| CAP | 相对权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定此跟踪区下，MME负荷能力在MME Pool区中的相对权重值。<br>数据来源：整网规划<br>取值范围：整数类型，取值范围为0~255。<br>默认值：255 |

## 操作的配置对象

- [基于跟踪区的MME相对权重配置（MMECAPBYTA）](configobject/UNC/20.15.2/MMECAPBYTA.md)

## 使用实例

增加跟踪区123031223对应的相对权重为200。

ADD MMECAPBYTA: MCC="123", MNC="03", TAC="0x1223", CAP=200;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加基于跟踪区的MME相对权重配置(ADD-MMECAPBYTA)_72345865.md`
