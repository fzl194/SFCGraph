---
id: UDG@20.15.2@MMLCommand@DSP MSACTIVE
type: MMLCommand
name: DSP MSACTIVE（显示服务主实例相关信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSACTIVE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP MSACTIVE（显示服务主实例相关信息）

## 功能

此命令用于查询所有服务的主实例的服务名，实例ID，进程ID，Pod ID，节点ID等相关信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSACTIVE]] · 服务主实例相关信息（MSACTIVE）

## 使用实例

获取所有服务主实例的服务名，实例ID，进程ID，Pod ID，节点ID等信息。

```
%%DSP MSACTIVE:;%%
RETCODE = 0  操作成功
结果如下
------------------------   
服务名称           服务实例ID            进程ID                                               Pod ID                                      节点ID           服务组ID   可选项  

UesmCtrlSvc        12532461132836508461  appctrl-pod-59f6dcf56b-f94v2192-168-0-224__1012__0   appctrl-pod-59f6dcf56b-f94v2192-168-0-224   192.168.0.1      999        NULL
SmcCtrlSvc         12532462215168265344  appctrl-pod-59f6dcf56b-f94v2192-168-0-224__1012__0   appctrl-pod-59f6dcf56b-f94v2192-168-0-224   192.168.0.2      999        NULL
AddrCtrlSvc        12532464908111989945  appctrl-pod-59f6dcf56b-lnphd192-168-0-130__1012__0   appctrl-pod-59f6dcf56b-lnphd192-168-0-130   192.168.0.3      999        NULL
UpcCtrlSvc         12532463465002981144  appctrl-pod-59f6dcf56b-lnphd192-168-0-130__1012__0   appctrl-pod-59f6dcf56b-lnphd192-168-0-130   192.168.0.4      999        NULL
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示服务主实例相关信息（DSP-MSACTIVE）_88183810.md`
