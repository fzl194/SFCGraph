---
id: UNC@20.15.2@MMLCommand@MOD AREAGP
type: MMLCommand
name: MOD AREAGP（修改区域群）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: AREAGP
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
- 移动性管理
- 区域漫游限制管理
- 区域群管理
status: active
---

# MOD AREAGP（修改区域群）

## 功能

**适用网元：SGSN、MME**

此命令用于修改区域群的名称。

当需要修改区域群的名称时，需要执行此命令。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：必选参数<br>参数含义：待修改的区域群标识。<br>数据来源：整网规划<br>取值范围：1~50<br>默认值：无 |
| AREAN | 区域群名称 | 可选必选说明：可选参数<br>参数含义：待修改的区域群名称。<br>数据来源：整网规划<br>取值范围：1~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AREAGP]] · 区域群（AREAGP）

## 使用实例

修改一条区域群记录，将区域群标识为1的区域群名称改为GROUP30：

MOD AREAGP: AREAID=1, AREAN="GROUP30";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-AREAGP.md`
