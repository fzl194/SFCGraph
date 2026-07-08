---
id: UNC@20.15.2@MMLCommand@DSP CFGRECOVERRESULT
type: MMLCommand
name: DSP CFGRECOVERRESULT（显示系统配置恢复结果）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CFGRECOVERRESULT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 配置维护
- 配置恢复结果
status: active
---

# DSP CFGRECOVERRESULT（显示系统配置恢复结果）

## 功能

该命令用于显示系统配置恢复结果。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CFGRECOVERRESULT]] · 系统配置恢复结果（CFGRECOVERRESULT）

## 使用实例

显示系统配置恢复结果：

```
DSP CFGRECOVERRESULT:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
配置恢复类型  =  CFG方式启动
配置恢复结果  =  配置恢复成功
    配置文件  =  nps_configuration.cfg
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-CFGRECOVERRESULT.md`
