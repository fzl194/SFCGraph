---
id: UNC@20.15.2@MMLCommand@DSP ACSPATCHINFO
type: MMLCommand
name: DSP ACSPATCHINFO（显示系统当前补丁信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ACSPATCHINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 补丁管理
status: active
---

# DSP ACSPATCHINFO（显示系统当前补丁信息）

## 功能

该命令用于显示VNFC系统当前补丁信息，包括补丁包名称、版本号、状态及生效时间。

补丁的加载、激活、删除都会触发补丁状态的变化，通过该命令可及时查询系统当前补丁的状态信息。

本命令只适用于ACS服务，其他微服务请使用DSP PATCHINFO命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [系统当前补丁信息（ACSPATCHINFO）](configobject/UNC/20.15.2/ACSPATCHINFO.md)

## 使用实例

显示补丁信息：

```
DSP ACSPATCHINFO:;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
  补丁单元合集版本号  =  V100R023SPH256
            补丁状态  =  运行
        补丁运行时间  =  2015-12-14 19:57:06
        补丁包名称    =  FENIXV100R023SPH256X8664.PAT
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示系统当前补丁信息（DSP-ACSPATCHINFO）_05338949.md`
