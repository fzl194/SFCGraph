---
id: UNC@20.15.2@MMLCommand@RMV HPLMN
type: MMLCommand
name: RMV HPLMN（删除本地PLMN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HPLMN
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- MNO管理
- MNO网络配置表
status: active
---

# RMV HPLMN（删除本地PLMN）

## 功能

![](删除本地PLMN(RMV HPLMN)_72225753.assets/notice_3.0-zh-cn_2.png)

- 删除后该PLMN的用户将无法再附着进来，已经附着的用户不受影响。
- 删除HPLMN将导致与该HPLMN相关的S1链路会出现链路异常。

**适用网元：SGSN、MME**

此命令用于删除归属PLMN配置信息。

## 注意事项

- 此命令执行后立即生效。
- 删除后该PLMN的用户将无法再附着进来，已经附着的用户不受影响。
- 删除HPLMN将导致与该HPLMN相关的S1链路会出现链路异常。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：待删除HPLMN的移动国家号码。<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：待删除HPLMN的移动网号码。<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HPLMN]] · 本地PLMN（HPLMN）

## 使用实例

删除移动国家码为123，移动网号为30的HPLMN配置：

RMV HPLMN: MCC="123", MNC="30";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-HPLMN.md`
