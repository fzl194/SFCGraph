---
id: UNC@20.15.2@MMLCommand@DSP ACSVERSION
type: MMLCommand
name: DSP ACSVERSION（显示系统版本信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ACSVERSION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 版本信息
status: active
---

# DSP ACSVERSION（显示系统版本信息）

## 功能

该命令用于显示VNFC的版本信息。

在日常的维护和版本升级时，可使用本命令显示系统当前的基础包、补丁包版本信息。

本命令只适用于ACS服务，其他微服务请使用DSP VERSION命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [系统版本信息（ACSVERSION）](configobject/UNC/20.15.2/ACSVERSION.md)

## 使用实例

显示VNFC的版本信息：

```
DSP ACSVERSION:;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
      包类型  =  版本包
    版本类型  =  基础版本
      版本号  =  V100R005C00
版本应用类型  =  BaseApp
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示系统版本信息（DSP-ACSVERSION）_05338935.md`
