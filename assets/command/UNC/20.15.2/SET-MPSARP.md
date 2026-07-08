---
id: UNC@20.15.2@MMLCommand@SET MPSARP
type: MMLCommand
name: SET MPSARP（设置MPS ARP配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MPSARP
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
- MPS配置
- MPS ARP信息配置
status: active
---

# SET MPSARP（设置MPS ARP配置）

## 功能

**适用网元：MME**

此命令用于设置MPS ARP配置。即通过此命令打开MPS功能，并配置MPS的ARP优先级临界值。优先级高于临界值的用户在MPS功能打开的情况下，将不会被流控接入限制，并且可以在下发寻呼的时候获得较高的寻呼优先级。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MPSFUNC | MPS功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示MPS功能的开关。<br>数据来源：运营商规划<br>取值范围：<br>- OFF(关)<br>- ON(开)<br>系统初始设置值：<br>“OFF(关)”<br>。 |
| PRILVL | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于表示ARP优先级临界值。<br>数据来源：运营商规划<br>取值范围：0～15<br>系统初始设置值：<br>“8”<br>。<br>配置原则：数值越小，优先级越高。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MPSARP]] · MPS ARP配置（MPSARP）

## 使用实例

设置MPS ARP配置，MPS功能开关为“OFF(关)”，优先级为“8”：

SET MPSARP: MPSFUNC=OFF, PRILVL=8;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-MPSARP.md`
