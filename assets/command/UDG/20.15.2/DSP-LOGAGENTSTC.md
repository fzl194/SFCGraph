---
id: UDG@20.15.2@MMLCommand@DSP LOGAGENTSTC
type: MMLCommand
name: DSP LOGAGENTSTC（查询日志代理丢弃的日志信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LOGAGENTSTC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 日志管理
status: active
---

# DSP LOGAGENTSTC（查询日志代理丢弃的日志信息）

## 功能

该命令用于查询日志代理丢弃的日志信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOGCLASS | 日志类别 | 可选必选说明：必选参数<br>参数含义：日志类别。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- log：普通日志。<br>- debug：调试信息（包括诊断日志）。<br>- alarm：告警信息。<br>- operlog：操作日志。<br>默认值：无 |
| PROCESSID | 进程ID | 可选必选说明：可选参数<br>参数含义：进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [日志代理丢弃的日志信息（LOGAGENTSTC）](configobject/UDG/20.15.2/LOGAGENTSTC.md)

## 使用实例

查询日志代理丢弃的告警日志统计信息，可通过如下命令查询：

```
DSP LOGAGENTSTC:LOGCLASS=alarm,PROCESSID=3
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
             日志代理PID  =  2147680264
                  日志ID  =  139591683
                丢弃原因  =  告警ID不存在
                丢弃数量  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询日志代理丢弃的日志信息（DSP-LOGAGENTSTC）_59103389.md`
