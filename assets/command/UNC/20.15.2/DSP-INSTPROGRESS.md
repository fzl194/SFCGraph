---
id: UNC@20.15.2@MMLCommand@DSP INSTPROGRESS
type: MMLCommand
name: DSP INSTPROGRESS（查询VNFC实例化进度）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: INSTPROGRESS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 资源管理
- VNFC实例化
status: active
---

# DSP INSTPROGRESS（查询VNFC实例化进度）

## 功能

该命令用来查看实例化进度。

## 注意事项

- 实例化中，执行该命令，查到的进度有5%、10%、35%、50%、70%。
- 实例化完成后，执行该命令，查到的进度一直为100%。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识，不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的RU状态查询。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/INSTPROGRESS]] · VNFC实例化进度（INSTPROGRESS）

## 使用实例

显示当前实例化进度：

```
DSP INSTPROGRESS:
SERVICEINSTANCE="CSLB_VNFC_999"
;
```

```
RETCODE = 0  操作成功。

结果如下
--------
VNFC实例化进度  =  70%
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VNFC实例化进度(DSP-INSTPROGRESS)_29626909.md`
