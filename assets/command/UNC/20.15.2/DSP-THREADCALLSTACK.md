---
id: UNC@20.15.2@MMLCommand@DSP THREADCALLSTACK
type: MMLCommand
name: DSP THREADCALLSTACK（显示线程调用栈信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: THREADCALLSTACK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 进程和组件信息
status: active
---

# DSP THREADCALLSTACK（显示线程调用栈信息）

## 功能

该命令用于查询进程内线程的调用栈信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程ID | 可选必选说明：必选参数<br>参数含义：该参数表示进程编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| THREADID | 线程ID | 可选必选说明：可选参数<br>参数含义：该参数表示线程编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～72057594037927935。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@THREADCALLSTACK]] · 线程调用栈信息（THREADCALLSTACK）

## 使用实例

为了显示线程调用栈信息，执行此命令：

```
DSP THREADCALLSTACK:PROCID=3,THREADID=139832844126016
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
      进程ID  = 3
      线程ID  = 139832844126016
    线程名字  = Thread MainThread
  线程调用栈  =   
#00 libc.so.6(epoll_wait)
#01 location(Frame_Main)
#02 libc.so.6(__libc_start_main)                                                                                          
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-THREADCALLSTACK.md`
