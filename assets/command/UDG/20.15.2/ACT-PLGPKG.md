---
id: UDG@20.15.2@MMLCommand@ACT PLGPKG
type: MMLCommand
name: ACT PLGPKG（激活扩展包）
nf: UDG
version: 20.15.2
verb: ACT
object_keyword: PLGPKG
command_category: 动作类
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

# ACT PLGPKG（激活扩展包）

## 功能

![](激活扩展包（ACT PLGPKG）_59103877.assets/notice_3.0-zh-cn.png)

该命令属于高危命令，若激活的是冷扩展包（即激活该扩展包时需要重启系统使其生效），则该操作会重启系统，请谨慎使用。

该命令用于将LOD PLGPKG加载的扩展包激活。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLGTYPE | 扩展包类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扩展包类型。可通过<br>[**LST PLGPKG**](查询加载的扩展包（LST PLGPKG）_59103370.md)<br>查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| VERSIONID | 版本号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定版本号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [扩展包（PLGPKG）](configobject/UDG/20.15.2/PLGPKG.md)

## 使用实例

激活扩展包：

```
ACT PLGPKG:PLGTYPE="Listening", VERSIONID="V100R005C00MOD"
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/激活扩展包（ACT-PLGPKG）_59103877.md`
