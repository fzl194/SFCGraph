---
id: UNC@20.15.2@MMLCommand@DSP STARTUP
type: MMLCommand
name: DSP STARTUP（显示本次和下次启动文件）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: STARTUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 配置维护
- 启动文件
status: active
---

# DSP STARTUP（显示本次和下次启动文件）

## 功能

该命令用于显示与本次及下次启动相关的系统软件、配置文件名、PAF文件名和补丁文件名。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/STARTUP]] · 本次和下次启动文件（STARTUP）

## 使用实例

查询与本次及下次启动相关的系统软件、配置文件名、PAF文件名和补丁文件名：

```
DSP STARTUP:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
                   OMU类型  =  Master
            指定的系统文件  =  home:/V100R005C10B010/base/FENIXV100R005C10B010D0417.cc
  本次启动所使用的系统软件  =  home:/V100R005C10B010/base/FENIXV100R005C10B010D0417.cc
下一次启动所使用的系统软件  =  home:/V100R005C10B010/base/FENIXV100R005C10B010D0417.cc
  本次启动时使用的配置文件  =  home:/vrpcfg.dat
下一次启动时使用的配置文件  =  home:/vrpcfg.dat
  本次启动时使用的补丁文件  =  NULL
下一次启动时使用的补丁文件  =  NULL
   本次启动时使用的PAF文件  =  default
 下一次启动时使用的PAF文件  =  default
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示本次和下次启动文件（DSP-STARTUP）_59103711.md`
