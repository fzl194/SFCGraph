---
id: UNC@20.15.2@MMLCommand@RMV HNOSRVPLMN
type: MMLCommand
name: RMV HNOSRVPLMN（删除归属网络Serving PLMN信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HNOSRVPLMN
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- 归属网络Serving PLMN管理
status: active
---

# RMV HNOSRVPLMN（删除归属网络Serving PLMN信息）

## 功能

**适用网元：SGSN**

此命令用于删除归属网络中Non-supporting UE的Serving PLMN配置。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该运营商的Serving PLMN的移动国家号码。<br>数据来源：整网规划<br>取值范围：3位十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该运营商的Serving PLMN的移动网号码。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HNOSRVPLMN]] · 归属网络Serving PLMN信息（HNOSRVPLMN）

## 使用实例

删除归属网络中Non-supporting UE的Serving PLMN配置

RMV HNOSRVPLMN: NOID=0, MCC="123", MNC="03";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-HNOSRVPLMN.md`
