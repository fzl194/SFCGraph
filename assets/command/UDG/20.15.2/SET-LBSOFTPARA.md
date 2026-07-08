---
id: UDG@20.15.2@MMLCommand@SET LBSOFTPARA
type: MMLCommand
name: SET LBSOFTPARA（设置CSLB软件调试参数表）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: LBSOFTPARA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 系统调测
- 公共调测
- 软件参数管理
status: active
---

# SET LBSOFTPARA（设置CSLB软件调试参数表）

## 功能

该命令用于设置CSLB系统软件参数。

## 注意事项

- 系统初次上电运行时，会执行系统初始设置值。
- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAID | 参数标识 | 可选必选说明：必选参数<br>参数含义：软件参数ID<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：无 |
| PARAVALUE | 参数值 | 可选必选说明：必选参数<br>参数含义：软件参数值<br>数据来源：本端规划<br>取值范围：0~4294967295<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LBSOFTPARA]] · CSLB软件调试参数表（LBSOFTPARA）

## 使用实例

设置系统软件参数ID为1023的参数值为2:

SET LBSOFTPARA: PARAID=1023, PARAVALUE=2;

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-LBSOFTPARA.md`
