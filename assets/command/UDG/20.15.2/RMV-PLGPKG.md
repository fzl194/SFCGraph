---
id: UDG@20.15.2@MMLCommand@RMV PLGPKG
type: MMLCommand
name: RMV PLGPKG（删除扩展包）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PLGPKG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 扩展包管理
status: active
---

# RMV PLGPKG（删除扩展包）

## 功能

![](删除扩展包（RMV PLGPKG）_59103532.assets/notice_3.0-zh-cn.png)

该命令属于高危命令，若删除的是冷扩展包，则该操作会重启系统，请谨慎使用。

该命令用于删除不需要的扩展包。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLGTYPE | 扩展包类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扩展包类型。可通过<br>[**LST PLGPKG**](查询加载的扩展包（LST PLGPKG）_59103370.md)<br>或者<br>[**DSP PLGPKG**](显示扩展包版本信息（DSP PLGPKG）_59104292.md)<br>查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| VERSIONID | 版本号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扩展包版本号。可通过<br>[**LST PLGPKG**](查询加载的扩展包（LST PLGPKG）_59103370.md)<br>或者<br>[**DSP PLGPKG**](显示扩展包版本信息（DSP PLGPKG）_59104292.md)<br>查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PLGPKG]] · 扩展包（PLGPKG）

## 使用实例

删除侦听功能扩展包：

```
RMV PLGPKG:PLGTYPE="Listening",VERSIONID="V100R020C00SPH153"
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-PLGPKG.md`
