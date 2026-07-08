---
id: UDG@20.15.2@MMLCommand@DSP SCALEGROUP
type: MMLCommand
name: DSP SCALEGROUP（查询ScaleGroup信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SCALEGROUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 资源管理
- ScaleGroup信息
status: active
---

# DSP SCALEGROUP（查询ScaleGroup信息）

## 功能

该命令用来查看VNFC下所有ScaleGroup的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识，不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的RU状态查询。 |

## 操作的配置对象

- [ScaleGroup信息（SCALEGROUP）](configobject/UDG/20.15.2/SCALEGROUP.md)

## 使用实例

查看ScaleGroup的信息。

DSP SCALEGROUP :SERVICEINSTANCE="CSLB_VNFC_999" ;

```
%%/*4166*/DSP SCALEGROUP:
SERVICEINSTANCE="CSLB_VNFC_999"
;%%
RETCODE = 0  操作成功。

结果如下
--------
          组索引  =  1
  ScaleGroup名字  =  SG0_CSLB_IPFWD
(结果个数 = 1)
---    END 
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ScaleGroup信息(DSP-SCALEGROUP)_29626972.md`
