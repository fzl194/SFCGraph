---
id: UNC@20.15.2@MMLCommand@SAV LOGFILE
type: MMLCommand
name: SAV LOGFILE（保存黑匣子的数据到日志文件中）
nf: UNC
version: 20.15.2
verb: SAV
object_keyword: LOGFILE
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 日志管理
status: active
---

# SAV LOGFILE（保存黑匣子的数据到日志文件中）

## 功能

该命令用于将日志黑匣子(缓存)中的数据保存到日志文件中。

## 注意事项

- 该命令执行后立即生效。
- 系统会通过日志的形式实时记录设备运行时出现的各种情况。为减少写存储设备的次数，日志内容在写入信息文件之前，会先缓存在系统64K的内存中，通常当缓冲区满或者30分钟定时器到，设备会立即将64K缓存的内容写入到信息文件。
- 如果在缓冲区未满或者定时器未到的情况下，需要手工将系统64K缓存的内容写入到信息文件，此时可以使用本命令。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOGTYPE | 日志类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要保存的日志类型。<br>数据来源：本端规划<br>取值范围：整数类型，0、1、2。<br>默认值：0<br>配置原则：配置为0时表示保存普通日志文件（安全日志、操作日志、事件日志、告警日志）。 配置为1时表示保存诊断日志。配置为2时表示收集DB文件config.dat、vrpcfg.dat、master、base_config.dat并上传至OM Portal的<br>“系统>文件传输>ACS DB文件”<br>下。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOGFILE]] · 保存黑匣子的数据到日志文件中（LOGFILE）

## 使用实例

- 保存安全日志，操作日志，事件日志，告警日志到日志文件中，可通过执行如下命令：
  ```
  SAV LOGFILE:
  SERVICEINSTANCE="vnfc"
  ;
  ```
- 保存诊断日志到文件中，可通过执行如下命令：
  ```
  SAV LOGFILE:LOGTYPE=1
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
- 收集ACS大颗粒的DB文件并上传至OM Portal的 “ 系统 > 文件传输 > ACS DB文件 ” 下，可通过执行如下命令：
  ```
  SAV LOGFILE:LOGTYPE=2
  ,SERVICEINSTANCE="ACS"
  ;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SAV-LOGFILE.md`
