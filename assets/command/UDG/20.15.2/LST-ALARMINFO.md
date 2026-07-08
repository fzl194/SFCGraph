---
id: UDG@20.15.2@MMLCommand@LST ALARMINFO
type: MMLCommand
name: LST ALARMINFO（查询告警信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ALARMINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 告警管理
- 告警对象实例
status: active
---

# LST ALARMINFO（查询告警信息）

## 功能

该命令用于基于告警ID查询告警信息，包括告警级别、屏蔽状态和抑制时间等信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALARMID | 告警ID | 可选必选说明：必选参数<br>参数含义：告警ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ALARMINFO]] · 告警信息（ALARMINFO）

## 使用实例

基于告警ID（135602186）查询告警属性信息，可通过如下命令查询：

```
LST ALARMINFO:ALARMID=135602186
,SERVICEINSTANCE="ACS"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
                  告警ID  =  135602186
                告警名称  =  数据库恢复失败
  告警产生抑制周期（秒）  =  0
  告警清除抑制周期（秒）  =  0
                告警级别  =  重要
            告警屏蔽状态  =  关
                告警类别  =  故障告警
            默认告警级别  =  重要
        默认告警屏蔽状态  =  关
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询告警信息（LST-ALARMINFO）_59104072.md`
