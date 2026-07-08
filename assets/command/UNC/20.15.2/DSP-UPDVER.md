---
id: UNC@20.15.2@MMLCommand@DSP UPDVER
type: MMLCommand
name: DSP UPDVER（显示当前版本信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: UPDVER
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

# DSP UPDVER（显示当前版本信息）

## 功能

在日常维护和版本升级时，执行该命令检查当前的基础包和补丁包的版本号信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPDVER]] · 当前版本信息（UPDVER）

## 使用实例

显示版本信息：

```
DSP UPDVER:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功 

结果如下:  
-------------------------  
基础软件包版本号 = V100R005C00B021
      补丁版本号 = SPH0020
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-UPDVER.md`
