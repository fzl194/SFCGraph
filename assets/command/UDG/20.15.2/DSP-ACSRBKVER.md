---
id: UDG@20.15.2@MMLCommand@DSP ACSRBKVER
type: MMLCommand
name: DSP ACSRBKVER（显示升级可回退版本信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ACSRBKVER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 升级维护
status: active
---

# DSP ACSRBKVER（显示升级可回退版本信息）

## 功能

该命令用于显示升级维护可回退版本信息。

在日常的维护和版本升级时，可使用本命令显示系统可回退的基础软件包和补丁版本信息。

本命令只适用于ACS服务，其他微服务请使用DSP RBKVER命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RBKTYPE | 回退类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定回退类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LAST：上一个版本。<br>- BASESOFTWARE：基础版本。<br>- PATCH：补丁。<br>默认值：LAST |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ACSRBKVER]] · 升级可回退版本信息（ACSRBKVER）

## 使用实例

显示可回退版本信息：

```
DSP ACSRBKVER:;
```

```
RETCODE = 0  操作成功 

结果如下: 
------------------------- 
        回退类型 = 基础版本
基础软件包版本号 = V100R005C00
      补丁版本号 = SPH0010
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-ACSRBKVER.md`
