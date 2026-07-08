---
id: UNC@20.15.2@MMLCommand@STR USEROFFLOAD
type: MMLCommand
name: STR USEROFFLOAD（执行用户迁移）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: USEROFFLOAD
command_category: 动作类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 网关故障管理
status: active
---

# STR USEROFFLOAD（执行用户迁移）

## 功能

**适用网元：MME**

S-GW或P-GW发生故障时，本命令用于立即启动单个用户业务迁移功能，其中业务迁移是指将用户业务迁移至正常的S-GW，或者去激活PDN使用户在其他正常的P-GW上重新激活PDN，本命令主要用于测试场景。

## 注意事项

- 此命令需要S-GW/P-GW故障下的业务恢复特性（特性编号：WSFD-201203，license部件编码：LKV2SRGF01）的License支持才可以。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要迁移用户的国际移动用户标识。<br>数据来源：本端规划<br>取值范围：6~15位数字<br>默认值：无 |

## 操作的配置对象

- [用户迁移（USEROFFLOAD）](configobject/UNC/20.15.2/USEROFFLOAD.md)

## 使用实例

对IMSI为 “123001234567890” 的用户进行迁移操作：

STR USEROFFLOAD: IMSI="123001234567890";

## 证据

- 原始手册：`evidence/UNC/20.15.2/执行用户迁移(STR-USEROFFLOAD)_72225763.md`
