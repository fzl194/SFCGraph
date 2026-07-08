---
id: UNC@20.15.2@MMLCommand@DSP RESPROCMSGAREA
type: MMLCommand
name: DSP RESPROCMSGAREA（显示进程消息分区信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RESPROCMSGAREA
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

# DSP RESPROCMSGAREA（显示进程消息分区信息）

## 功能

该命令用于显示进程内的消息分区使用信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESOURCENAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：用于说明节点名称或容器名称。通过<br>[**DSP RES**](../../../系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)<br>命令可以查询资源信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无 |
| PROCID | 进程ID | 可选必选说明：可选参数<br>参数含义：用于说明进程的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESPROCMSGAREA]] · 进程消息分区信息（RESPROCMSGAREA）

## 使用实例

显示进程内消息分区的使用情况：

```
DSP RESPROCMSGAREA:RESOURCENAME="OMU1",PROCID=1001;
```

```
RETCODE = 0  操作成功

结果如下:
--------
进程ID    资源名称    消息分区名       最大消息单元数目    已分配的消息单元数目    消息分配百分比（%）    已使用的消息分区数目  消息分区总数 

1001      OMU1        AREA_SYS         1048576             0                       0                      1                     5                      
1001      OMU1        AREA_MGNT        1048576             0                       0                      1                     5                      
1001      OMU1        AREA_FLOWCTRL    5242880             0                       0                      1                     10                     
1001      OMU1        AREA_OTHER       1048576             768                     0                      1                     10   
（结果个数 = 4）
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示进程消息分区信息（DSP-RESPROCMSGAREA）_57993317.md`
