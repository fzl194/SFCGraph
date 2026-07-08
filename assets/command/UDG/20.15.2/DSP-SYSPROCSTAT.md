---
id: UDG@20.15.2@MMLCommand@DSP SYSPROCSTAT
type: MMLCommand
name: DSP SYSPROCSTAT（查询系统处理状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SYSPROCSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 资源管理
- scale功能管理
status: active
---

# DSP SYSPROCSTAT（查询系统处理状态）

## 功能

该命令用来查看VNFC是否处于稳态，是否允许下发扩缩容或者动态上下线等命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识，不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的RU状态查询。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SYSPROCSTAT]] · 系统处理状态（SYSPROCSTAT）

## 使用实例

查看VNFC下的系统处理状态的信息。

```
DSP SYSPROCSTAT:
SERVICEINSTANCE="CSLB_VNFC_999"
; 
```

```
RETCODE = 0  操作成功。

结果如下
--------
  状态级别  ScaleGroup的名字   状态
  系统      NA                 稳态
  本地      SG0_CSLB_IPFWD     稳态
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询系统处理状态(DSP-SYSPROCSTAT)_29626935.md`
