---
id: UNC@20.15.2@MMLCommand@DSP SERVICE
type: MMLCommand
name: DSP SERVICE（显示业务状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SERVICE
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 业务管理
status: active
---

# DSP SERVICE（显示业务状态）

## 功能

**适用NF：NCG**

该命令用于显示所有业务进程状态。

当系统安装后、进行系统维护时或者系统重启后，可以使用 [**DSP SERVICE**](显示业务状态（DSP SERVICE）_51174328.md) 显示业务进程状态。

如果出现业务状态异常，请检查系统的告警、日志，并进行处理。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU的ID | 可选必选说明：可选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SERVICE]] · 复位业务（SERVICE）

## 使用实例

显示所有的业务状态：

```
DSP SERVICE:;
```

```
RETCODE = 0  操作成功。

结果如下:
--------
RU的ID    模块名      模块状态 

64        cdm_proc    激活     
64        cbk_proc    激活     
64        cqb_proc    激活     
64        AP64_1      激活     
65        AP65_1      激活     
65        cdm_proc    激活     
65        cbk_proc    激活     
65        cqb_proc    激活     
(结果个数 = 8)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SERVICE.md`
