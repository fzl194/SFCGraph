---
id: UDG@20.15.2@MMLCommand@DSP SCALINGWORKLOAD
type: MMLCommand
name: DSP SCALINGWORKLOAD（显示扩缩容负载查询）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SCALINGWORKLOAD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 弹性开关
status: active
---

# DSP SCALINGWORKLOAD（显示扩缩容负载查询）

## 功能

此命令用于显示当前系统中每个资源对象的负载情况，作为自动扩缩容的参考依据。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [扩缩容负载查询（SCALINGWORKLOAD）](configobject/UDG/20.15.2/SCALINGWORKLOAD.md)

## 使用实例

DSP SCALINGWORKLOAD:;

```
%%DSP SCALINGWORKLOAD:;%%
RETCODE = 0  操作成功
结果如下
--------
资源对象  KPI类型   负载
PBU_P-L   workload  25    
OMU_L     workload  29    
SDU       workload  7 
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示扩缩容负载查询（DSP-SCALINGWORKLOAD）_09587919.md`
