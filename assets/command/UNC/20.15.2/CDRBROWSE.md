---
id: UNC@20.15.2@MMLCommand@CDRBROWSE
type: MMLCommand
name: CDRBROWSE（话单查询浏览）
nf: UNC
version: 20.15.2
verb: CDRBROWSE
object_keyword: ''
command_category: 调测类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 话单查询浏览
status: active
---

# CDRBROWSE（话单查询浏览）

## 功能

**适用NF：NCG**

该命令用于在网管上赋予自建命令组使用话单查询浏览功能的权限。

## 注意事项

该命令在CSP前台执行无意义。

## 权限

manage-ug
G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ID | 身份标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定话单查询浏览标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：0<br>配置原则：无 |

## 使用实例

在网管上将CDRBROWSE命令权限加入自定义的M_0命令组中，赋予自建网管用户M_0命令组权限，使用该自建网管用户登录CSP，点击查询浏览，查询和浏览功能都可以使用。

```
无
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CDRBROWSE.md`
