---
id: UDG@20.15.2@MMLCommand@DSP RESPROCFILEHDLSTAT
type: MMLCommand
name: DSP RESPROCFILEHDLSTAT（显示进程文件句柄使用信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RESPROCFILEHDLSTAT
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

# DSP RESPROCFILEHDLSTAT（显示进程文件句柄使用信息）

## 功能

该命令用于显示进程内的文件句柄使用信息。

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

- [[configobject/UDG/20.15.2/RESPROCFILEHDLSTAT]] · 进程文件句柄使用信息（RESPROCFILEHDLSTAT）

## 使用实例

显示进程内的文件句柄使用情况：

```
DSP RESPROCFILEHDLSTAT:RESOURCENAME="OMU1";
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
进程ID        资源名称     文件句柄数目         文件句柄最大数目

4             OMU1         52                   1024                  
1002          OMU1         34                   1024                  
1001          OMU1         32                   1024                  
1000          OMU1         33                   1024                  
10002         OMU1         32                   1024                  
10001         OMU1         32                   1024                  
1003          OMU1         38                   1024                  
3             OMU1         42                   1024                  
2             OMU1         36                   1024              
(结果个数 = 9)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-RESPROCFILEHDLSTAT.md`
