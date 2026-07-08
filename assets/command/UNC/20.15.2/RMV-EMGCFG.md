---
id: UNC@20.15.2@MMLCommand@RMV EMGCFG
type: MMLCommand
name: RMV EMGCFG（删除运营商紧急呼叫功能配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EMGCFG
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 紧急呼叫配置
- 紧急呼叫功能配置
status: active
---

# RMV EMGCFG（删除运营商紧急呼叫功能配置）

## 功能

**适用网元：MME**

该命令用于删除指定MNO/MVNO对应的紧急呼叫配置数据。

## 注意事项

该命令执行后立即生效。

删除记录会导致此MNO/MVNO下的用户无法使用紧急呼叫业务。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：运营商规划<br>取值范围： 0～64，128～254<br>默认值： 无<br>配置原则：<br>“NOID”<br>指定的记录已经通过<br>[**ADD EMGCFG**](增加运营商紧急呼叫功能配置（ADD EMGCFG）_26305316.md)<br>配置了。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EMGCFG]] · 运营商紧急呼叫功能配置（EMGCFG）

## 使用实例

删除 “运营商标识” 为 “0” 的运营商紧急呼叫功能的配置：

RMV EMGCFG: NOID=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-EMGCFG.md`
