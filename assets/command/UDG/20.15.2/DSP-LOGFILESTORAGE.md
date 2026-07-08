---
id: UDG@20.15.2@MMLCommand@DSP LOGFILESTORAGE
type: MMLCommand
name: DSP LOGFILESTORAGE（显示日志存储信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LOGFILESTORAGE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 日志管理调测
status: active
---

# DSP LOGFILESTORAGE（显示日志存储信息）

## 功能

该命令用于显示日志存储信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [日志存储信息（LOGFILESTORAGE）](configobject/UDG/20.15.2/LOGFILESTORAGE.md)

## 使用实例

显示日志存储信息：

```
DSP LOGFILESTORAGE:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
日志类型    总日志空间（Byte）    使用的日志空间（Byte）    可用的日志空间（Byte）    占用百分比（%）    日志文件路径

事件日志    80530630              8921                      80521709                  1                  logfile:/          
诊断日志    362387835             1667308                   360720527                 1                  logfile:/          
安全日志    80530630              8763                      80521867                  1                  logfile:/security/ 
操作日志    120795945             1332467                   119463478                 1                  logfile:/operation/
调测日志    80530630              115568                    80415062                  1                  logfile:/  
告警日志    80530630              693621                    79837009                  1                  logfile:/alarm/
(结果个数 = 6)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示日志存储信息（DSP-LOGFILESTORAGE）_59103956.md`
