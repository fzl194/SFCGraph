---
id: UNC@20.15.2@MMLCommand@MOD LARAGP
type: MMLCommand
name: MOD LARAGP（修改位置区群组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: LARAGP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 位置区管理
- 位置区群组管理
status: active
---

# MOD LARAGP（修改位置区群组）

## 功能

**适用网元：SGSN**

此命令用于修改位置区和路由区的区域群的名称。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LARAGPID | 区域群标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区和路由区的区域群标识。<br>数据来源：整网规划<br>取值范围：1～2048<br>默认值：无 |
| LARAGPN | 区域群名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定区域群名称。<br>数据来源：整网规划<br>取值范围：1～32位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LARAGP]] · 位置区群组（LARAGP）

## 使用实例

修改一个位置区群组，区域群标识为55，其群组名称为“shanghai”:

MOD LARAGP: LARAGPID=55, LARAGPN="shanghai";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-LARAGP.md`
