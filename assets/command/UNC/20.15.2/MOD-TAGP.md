---
id: UNC@20.15.2@MMLCommand@MOD TAGP
type: MMLCommand
name: MOD TAGP（修改TA群组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: TAGP
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
- 跟踪区管理
- 跟踪区群组管理
status: active
---

# MOD TAGP（修改TA群组）

## 功能

**适用网元：MME**

此命令用于修改跟踪区群组记录。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAGPID | 跟踪区群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区群组标识。<br>数据来源：本端规划<br>取值范围：1～2048<br>默认值：无 |
| TANAME | 跟踪区群组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区群组名称。<br>数据来源：本端规划<br>取值范围：0～32位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TAGP]] · TA群组（TAGP）

## 使用实例

修改一个TA群组，跟踪区群组标识为1，其群组名称为“nanjing”

MOD TAGP: TAGPID=1, TANAME="nanjing";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-TAGP.md`
