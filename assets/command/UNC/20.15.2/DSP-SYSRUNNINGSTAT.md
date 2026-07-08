---
id: UNC@20.15.2@MMLCommand@DSP SYSRUNNINGSTAT
type: MMLCommand
name: DSP SYSRUNNINGSTAT（系统状态查询）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SYSRUNNINGSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 服务部署管理
status: active
---

# DSP SYSRUNNINGSTAT（系统状态查询）

## 功能

该命令用于查询系统运行状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：该参数用于标识网元ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~40。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [系统状态查询（SYSRUNNINGSTAT）](configobject/UNC/20.15.2/SYSRUNNINGSTAT.md)

## 使用实例

DSP SYSRUNNINGSTAT;

```
DSP SYSRUNNINGSTAT;
%%DSP SYSRUNNINGSTAT:;%%
RETCODE = 0  操作成功

结果如下
--------
系统状态 = 系统状态正常
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/系统状态查询（DSP-SYSRUNNINGSTAT）_34307331.md`
