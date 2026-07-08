---
id: UDG@20.15.2@MMLCommand@DSP DPSCALEUP
type: MMLCommand
name: DSP DPSCALEUP（查询硬盘分区扩容进展）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DPSCALEUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 资源管理
- 磁盘管理
status: active
---

# DSP DPSCALEUP（查询硬盘分区扩容进展）

## 功能

该命令用于查看当前VNFC下硬盘分区扩容进展。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU的ID | 可选必选说明：可选参数。<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识，不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的RU状态查询。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DPSCALEUP]] · 硬盘分区扩容进展（DPSCALEUP）

## 使用实例

查看硬盘分区扩容进展。

```
DSP DPSCALEUP:
SERVICEINSTANCE="CSLB_VNFC_999"
;
```

```
RETCODE = 0  操作成功。

结果如下
-----------------------
RU的ID    硬盘分区扩容进展

64       扩容中                  
65       扩容中                  
66       扩容中                  
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DPSCALEUP.md`
