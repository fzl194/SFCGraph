---
id: UNC@20.15.2@MMLCommand@DSP DBGCLICMDPRXYREG
type: MMLCommand
name: DSP DBGCLICMDPRXYREG（显示通过命令代理可执行命令行调试命令的白名单）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DBGCLICMDPRXYREG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 调试命令
status: active
---

# DSP DBGCLICMDPRXYREG（显示通过命令代理可执行命令行调试命令的白名单）

## 功能

该命令用于显示通过命令代理可执行命令行调试命令的白名单。

## 注意事项

- 该命令执行后立即生效。
- 该命令用于收集定位信息，需要谨慎执行，请在华为工程师指导下执行。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DBGCLICMDPRXYREG]] · 通过命令代理可执行命令行调试命令的白名单（DBGCLICMDPRXYREG）

## 使用实例

显示通过命令代理可执行命令行调试命令的白名单：

```
DSP DBGCLICMDPRXYREG:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0 操作成功

结果如下:
--------
调试命令类ID    调试命令  

135667988       display cli trace               
135667985       display cli workspace 
135684353       display ml-string 
(结果个数 = 3)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DBGCLICMDPRXYREG.md`
