---
id: UDG@20.15.2@MMLCommand@DSP PATCHINFO
type: MMLCommand
name: DSP PATCHINFO（显示系统当前补丁信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PATCHINFO
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

# DSP PATCHINFO（显示系统当前补丁信息）

## 功能

该命令用于显示VNFC系统当前补丁信息，包括补丁包名称、版本号、状态及生效时间。

补丁的加载、激活、删除都会触发补丁状态的变化，通过该命令可及时查询系统当前补丁的状态信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PATCHINFO]] · 系统当前补丁信息（PATCHINFO）

## 使用实例

显示补丁信息：

```
DSP PATCHINFO:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
  补丁单元合集版本号  =  V100R023SPH256
            补丁状态  =  运行
        补丁运行时间  =  2015-12-14 19:57:06
           补丁包名称 =  FENIXV100R023SPH256X8664.PAT
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PATCHINFO.md`
