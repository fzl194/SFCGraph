---
id: UDG@20.15.2@MMLCommand@CHK APPDATA
type: MMLCommand
name: CHK APPDATA（检查APP配置数据）
nf: UDG
version: 20.15.2
verb: CHK
object_keyword: APPDATA
command_category: 调测类
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

# CHK APPDATA（检查APP配置数据）

## 功能

该命令用于检查APP配置数据和OMU配置数据是否一致。如果数据不一致，则记录差异信息。用户可以通过 [**DSP APPDATADIFF**](查询APP与OMU配置数据差异信息（DSP APPDATADIFF）_59103640.md) 命令查询差异信息。

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

- [同步APP配置数据（APPDATA）](configobject/UDG/20.15.2/APPDATA.md)

## 使用实例

检查3号进程APP配置数据和OMU是否一致：

```
CHK APPDATA:PROCESSID=3
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/检查APP配置数据（CHK-APPDATA）_59103798.md`
