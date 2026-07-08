---
id: UNC@20.15.2@MMLCommand@RMV LAIVLRBLACKLIST
type: MMLCommand
name: RMV LAIVLRBLACKLIST（删除LAIVLR黑名单）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LAIVLRBLACKLIST
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- MSC POOL管理
- LAIVLR黑名单管理
status: active
---

# RMV LAIVLRBLACKLIST（删除LAIVLR黑名单）

## 功能

**适用网元：MME**

该命令用于删除LAI与VLR的黑名单对应关系。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VN | VLR号 | 可选必选说明：必选参数<br>参数说明：该参数用于表示位置区对应的VLR号码。<br>数据来源：整网规划<br>取值范围： 1～15位十进制数字<br>默认值：无 |
| BGNLAI | LAI | 可选必选说明：必选参数<br>参数说明：该参数是指对应一个VLR号的LAI黑名单的起始位置区，由“MCC”、“MNC”和“LAC”组成。<br>数据来源：整网规划<br>取值范围：9~10位的数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LAIVLRBLACKLIST]] · LAIVLR黑名单（LAIVLRBLACKLIST）

## 使用实例

删除起始LAI为"308013101"的LAI区间与VLR为"12345678912"的黑名单对应关系：

RMV LAIVLRBLACKLIST: VN="12345678912", BGNLAI="308013101";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除LAIVLR黑名单(RMV-LAIVLRBLACKLIST)_72345025.md`
