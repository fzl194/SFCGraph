---
id: UDG@20.15.2@MMLCommand@SYN APPDATA
type: MMLCommand
name: SYN APPDATA（同步APP配置数据）
nf: UDG
version: 20.15.2
verb: SYN
object_keyword: APPDATA
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 配置维护
- APP配置检查
status: active
---

# SYN APPDATA（同步APP配置数据）

## 功能

该命令用于从主控OMU同步APP配置数据，实现APP配置数据与主控OMU一致。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令会对系统加锁，导致配置命令无法执行。操作结束后，可以正常进行配置。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCESSID | 进程ID | 可选必选说明：必选参数<br>参数含义：进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APPDATA]] · 同步APP配置数据（APPDATA）

## 使用实例

同步主控OMU配置数据至3号进程APP：

```
SYN APPDATA:PROCESSID=3
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SYN-APPDATA.md`
