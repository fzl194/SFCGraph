---
id: UNC@20.15.2@MMLCommand@DSP PLGPKG
type: MMLCommand
name: DSP PLGPKG（显示扩展包版本信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PLGPKG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 扩展包管理
status: active
---

# DSP PLGPKG（显示扩展包版本信息）

## 功能

该命令用于显示扩展包版本信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLGTYPE | 扩展包类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展包类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLGPKG]] · 扩展包（PLGPKG）

## 使用实例

显示扩展包版本信息：

```
DSP PLGPKG:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功
 
结果如下:
 -------------------------
 扩展包类型 = Listening
     版本号 = V100R005C00MOD    
 (结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示扩展包版本信息（DSP-PLGPKG）_59104292.md`
