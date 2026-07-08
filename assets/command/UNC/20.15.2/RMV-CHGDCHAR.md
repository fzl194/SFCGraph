---
id: UNC@20.15.2@MMLCommand@RMV CHGDCHAR
type: MMLCommand
name: RMV CHGDCHAR（删除缺省计费属性参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CHGDCHAR
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 缺省计费属性参数配置
status: active
---

# RMV CHGDCHAR（删除缺省计费属性参数）

## 功能

**适用网元：SGSN**

该命令用于删除一条缺省计费属性参数配置记录，由 “用户类型” 、 “移动国家码” 和 “移动网号” 确定某一条缺省计费属性参数配置记录。

## 注意事项

该命令执行后立即生效。执行后会影响新激活用户。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ST | 用户类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户类型。用户类型是指该缺省计费属性适用于漫游用户还是拜访用户。<br>取值范围：<br>- “ROAMING(漫游用户)”：表示使用归属PLMN的GGSN的外网用户。<br>- “VISITING(拜访用户)”：表示使用本PLMN的GGSN的外网用户。<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。移动国家码是指用户的移动国家代码。<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。移动网号是指用户的移动网号。<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGDCHAR]] · 缺省计费属性参数（CHGDCHAR）

## 使用实例

删除一个缺省计费属性参数配置记录，用户类型为漫游用户，移动国家码为123，移动网号为00，配置格式为：

RMV CHGDCHAR: ST=ROAMING, MCC="123", MNC="00";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CHGDCHAR.md`
