---
id: UDG@20.15.2@MMLCommand@DSP ALMFLAPSURPINFO
type: MMLCommand
name: DSP ALMFLAPSURPINFO（显示告警震荡抑制信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ALMFLAPSURPINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 告警管理
- 告警震荡
status: active
---

# DSP ALMFLAPSURPINFO（显示告警震荡抑制信息）

## 功能

该命令用于显示告警震荡抑制信息以及当前处于震荡的告警实例信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AID | 告警ID | 可选必选说明：必选参数<br>参数含义：告警ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ALMFLAPSURPINFO]] · 告警震荡抑制信息（ALMFLAPSURPINFO）

## 使用实例

显示警ID为135602186的震荡告警抑制信息，可通过如下命令显示：

```
DSP ALMFLAPSURPINFO:AID=135602186
,SERVICEINSTANCE="ACS"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
                       告警ID  =  135602186
                     告警名称  =  数据库恢复失败
                 告警震荡状态  =  震荡检测状态
       告警震荡产生周期（秒）  =  400
       告警震荡恢复周期（秒）  =  600
                 告警震荡阈值  =  3
   当前告警震荡产生周期（秒）  =  3
   当前告警震荡恢复周期（秒）  =  0
                 当前震荡阈值  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-ALMFLAPSURPINFO.md`
