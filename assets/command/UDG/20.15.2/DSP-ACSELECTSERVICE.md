---
id: UDG@20.15.2@MMLCommand@DSP ACSELECTSERVICE
type: MMLCommand
name: DSP ACSELECTSERVICE（查询仲裁服务状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ACSELECTSERVICE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 仲裁服务状态
status: active
---

# DSP ACSELECTSERVICE（查询仲裁服务状态）

## 功能

该命令用于查询仲裁服务状态。

本命令只适用于ACS服务，其他微服务请使用DSP ELECTSERVICE命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ACSELECTSERVICE]] · 仲裁服务状态（ACSELECTSERVICE）

## 使用实例

查询仲裁服务开关状态：

```
DSP ACSELECTSERVICE:;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
       仲裁服务开关状态 =  使能
(结果个数 = 1)
 ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-ACSELECTSERVICE.md`
