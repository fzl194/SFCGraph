---
id: UDG@20.15.2@MMLCommand@DSP RESHASTAT
type: MMLCommand
name: DSP RESHASTAT（查询系统HA状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RESHASTAT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 系统管理
- 资源管理
- 资源实例管理
status: active
---

# DSP RESHASTAT（查询系统HA状态）

## 功能

该命令用于查询系统资源的HA状态，HA（High Availability）是为系统存储服务提供高可靠性的模块。当系统进行升级时，需要确保所有组件状态正常，可以使用该命令确定资源的进程、组件状态是否正常。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESNAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：该参数表示节点或容器资源的名称。<br>配置原则：当不输入时显示所有资源的HA状态。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无 |

## 操作的配置对象

- [系统HA状态（RESHASTAT）](configobject/UDG/20.15.2/RESHASTAT.md)

## 使用实例

查询 “OMU1” 的HA状态：

```
DSP RESHASTAT:RESNAME="OMU1";
```

```
RETCODE = 0  操作成功
 
结果如下:
 -------------------------
 逻辑资源编号 = 1
     资源名称 = OMU1
       HA状态 = 正常    
 (结果个数 = 1)
  ---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询系统HA状态（DSP-RESHASTAT）_38001520.md`
