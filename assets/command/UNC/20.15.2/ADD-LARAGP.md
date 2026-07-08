---
id: UNC@20.15.2@MMLCommand@ADD LARAGP
type: MMLCommand
name: ADD LARAGP（增加位置区群组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LARAGP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 位置区管理
- 位置区群组管理
status: active
---

# ADD LARAGP（增加位置区群组）

## 功能

**适用网元：SGSN**

此命令用于增加位置区和路由区的区域群记录，为区域群成员提供区域群标识，同一个区域群中的成员具有相同的接入控制策略。

如果需要对多个区域采用相同的接入控制策略时，需要执行此命令。

## 注意事项

- 此命令最大记录数为2048。
- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LARAGPID | 区域群标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区和路由区的区域群标识。<br>数据来源：整网规划<br>取值范围：1～2048<br>默认值：无 |
| LARAGPN | 区域群名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定区域群名称。<br>数据来源：整网规划<br>取值范围：1～32位字符串<br>默认值：noname |

## 操作的配置对象

- [位置区群组（LARAGP）](configobject/UNC/20.15.2/LARAGP.md)

## 使用实例

增加一个位置区群组，区域群标识为55，其群组名称为“shanghai”:

ADD LARAGP: LARAGPID=55, LARAGPN="shanghai";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加位置区群组(ADD-LARAGP)_26305292.md`
