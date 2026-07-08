---
id: UNC@20.15.2@MMLCommand@RMV LCSPARAEX
type: MMLCommand
name: RMV LCSPARAEX（删除LCS扩展参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LCSPARAEX
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- LCS扩展参数
status: active
---

# RMV LCSPARAEX（删除LCS扩展参数）

## 功能

**适用网元：MME**

该命令用于基于运营商删除LCS扩展参数。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：整网规划<br>取值范围：0~64,128~254<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LCSPARAEX]] · LCS扩展参数（LCSPARAEX）

## 使用实例

删除NOID为0的运营商的LCS扩展参数。

RMV LCSPARAEX: NOID=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除LCS扩展参数(RMV-LCSPARAEX)_72345415.md`
