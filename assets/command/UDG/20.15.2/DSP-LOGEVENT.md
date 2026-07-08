---
id: UDG@20.15.2@MMLCommand@DSP LOGEVENT
type: MMLCommand
name: DSP LOGEVENT（显示事件日志信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LOGEVENT
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

# DSP LOGEVENT（显示事件日志信息）

## 功能

该命令用于显示事件日志信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LOGEVENT]] · 事件日志信息（LOGEVENT）

## 使用实例

显示事件日志信息：

```
DSP LOGEVENT:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
事件序列号    事件ID       事件级别         事件产生时间           事件描述信息                                                                                                                                                                        

2             135594006    提示             2017-09-03 17:31:32    配置发生更改。（配置流水号＝16， 绕接次数＝0， 配置变更点最大数目＝10000， 配置恢复时间＝2017-09-03 17:29:50）                              
1             135594006    提示             2017-09-03 17:31:14    配置发生更改。（配置流水号＝15， 绕接次数＝0， 配置变更点最大数目＝10000， 配置恢复时间＝2017-09-03 17:29:50）  
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-LOGEVENT.md`
