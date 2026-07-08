---
id: UNC@20.15.2@MMLCommand@DSP NSEUSR
type: MMLCommand
name: DSP NSEUSR（显示删除NSE列表下的用户任务运行状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NSEUSR
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- MS上下文管理
- 基于NSE的MS上下文管理
status: active
---

# DSP NSEUSR（显示删除NSE列表下的用户任务运行状态）

## 功能

**适用网元：SGSN**

该命令用于查询 [**RMV NSEUSR**](删除NSE列表下的用户(RMV NSEUSR)_26305832.md) 任务运行状态。当 [**RMV NSEUSR**](删除NSE列表下的用户(RMV NSEUSR)_26305832.md) 任务正在运行时，该命令可以查询任务的剩余时间。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSEUSR]] · NSE列表下的用户（NSEUSR）

## 使用实例

查询删除NSE列表下的用户的任务状态：

DSP NSEUSR:;

```
%%DSP NSEUSR:;%%
RETCODE = 0  执行成功。

结果如下
-------------------------------
           任务状态 = 正在运行
    任务剩余时间(s) = 1200

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NSEUSR.md`
