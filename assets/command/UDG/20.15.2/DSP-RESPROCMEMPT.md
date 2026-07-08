---
id: UDG@20.15.2@MMLCommand@DSP RESPROCMEMPT
type: MMLCommand
name: DSP RESPROCMEMPT（显示进程内存分区信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RESPROCMEMPT
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

# DSP RESPROCMEMPT（显示进程内存分区信息）

## 功能

该命令用于显示进程内的分区内存使用信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESOURCENAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：用于说节点名称或容器名称。通过<br>[**DSP RES**](../../../系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)<br>命令可以查询资源信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有的节点或容器的信息。 |
| PROCID | 进程ID | 可选必选说明：可选参数<br>参数含义：用于说明进程的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RESPROCMEMPT]] · 进程内存分区信息（RESPROCMEMPT）

## 使用实例

显示进程内分区内存的使用情况：

```
DSP RESPROCMEMPT:RESOURCENAME="OMU1",PROCID=1001;
```

```
RETCODE = 0  操作成功

结果如下:
--------
进程ID    资源名称  内存分区名         分区内存总大小（Kbytes）  分区内存使用大小（Kbytes）  分区内存使用最大值（Kbytes）  分区内存使用率（%）

1001      OMU1      SYSPT              846773                    845837                      846050                        99                
1001      OMU1      dbPT               4096                      2395                        3682                          58                
1001      OMU1      pipePT             7171                      6532                        6532                          91                
1001      OMU1      USRPT              3906                      2                           2                             0                 
1001      OMU1      msq_node           1562                      1561                        1561                          99                
1001      OMU1      commonPt           102400                    31003                       31153                         30                
1001      OMU1      tempPt             512                       3                           191                           0                 
1001      OMU1      simplePt           6146                      5135                        5135                          83                
1001      OMU1      dopra_pt_perf_f    65536                     796                         796                           1    
(结果个数 = 9)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-RESPROCMEMPT.md`
