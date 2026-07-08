---
id: UDG@20.15.2@MMLCommand@DSP INNERCOMPVERSION
type: MMLCommand
name: DSP INNERCOMPVERSION（显示系统内部部件版本信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: INNERCOMPVERSION
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

# DSP INNERCOMPVERSION（显示系统内部部件版本信息）

## 功能

该命令用于显示系统内部构件的版本信息。

在日常的维护时，可使用本命令显示系统当前的FENIX版本号、DOPRA版本号、VIST版本号、VPP版本号信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [系统内部部件版本信息（INNERCOMPVERSION）](configobject/UDG/20.15.2/INNERCOMPVERSION.md)

## 使用实例

显示系统内部版本信息：

```
DSP INNERCOMPVERSION:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
Fenix版本  =  FENIXV100R005C10B090
Dopra版本  =  DOPRA SSP V300R003C00B051
 Vist版本  =  vist_fenix5.0.170421
  Vpp版本  =  VPP V300R003C26SPC217B010
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示系统内部部件版本信息（DSP-INNERCOMPVERSION）_59103441.md`
