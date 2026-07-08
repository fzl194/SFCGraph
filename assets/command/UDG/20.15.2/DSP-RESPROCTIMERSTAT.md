---
id: UDG@20.15.2@MMLCommand@DSP RESPROCTIMERSTAT
type: MMLCommand
name: DSP RESPROCTIMERSTAT（显示进程定时器计数信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RESPROCTIMERSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 系统调测
- 进程和组件信息
status: active
---

# DSP RESPROCTIMERSTAT（显示进程定时器计数信息）

## 功能

该命令用于显示进程内的定时器使用信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESOURCENAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：用于说明节点名称或容器名称。通过<br>[**DSP RES**](../../../系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)<br>命令可以查询资源信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有的节点或容器的信息。 |
| PROCID | 进程ID | 可选必选说明：可选参数<br>参数含义：用于说明进程的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RESPROCTIMERSTAT]] · 进程定时器计数信息（RESPROCTIMERSTAT）

## 使用实例

显示进程内的定时器使用情况：

```
DSP RESPROCTIMERSTAT:RESOURCENAME="OMU1";
```

```
RETCODE = 0  操作成功

结果如下:
--------
进程ID    资源名称  绝对定时器数目    相对定时器数目    APP定时器数目 

4         OMU1      0                 37                69            
1002      OMU1      0                 29                23            
1001      OMU1      0                 68                91            
1000      OMU1      0                 8                 15            
10002     OMU1      0                 6                 15            
10001     OMU1      0                 23                59            
1003      OMU1      0                 16                25            
3         OMU1      0                 55                21            
2         OMU1      0                 34                40            
(结果个数 = 9)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-RESPROCTIMERSTAT.md`
