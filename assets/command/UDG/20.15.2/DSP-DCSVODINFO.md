---
id: UDG@20.15.2@MMLCommand@DSP DCSVODINFO
type: MMLCommand
name: DSP DCSVODINFO（显示点播视频信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DCSVODINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- MML命令
- 系统资源管理
status: active
---

# DSP DCSVODINFO（显示点播视频信息）

## 功能

该命令用于显示点播视频信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/DCSVODINFO]] · 点播视频信息（DCSVODINFO）

## 使用实例

显示所有实例的点播视频信息。

```
%%DSP DCSVODINFO:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                      实例ID  =  18378575044282908843
      极热内存区总大小（MB）  =  4960
      极热视频片头大小（MB）  =  15969
            极热视频片头个数  =  4985
        磁盘空间总大小（MB）  =  4990
磁盘空间最大可使用大小（MB）  =  0
  磁盘空间当前使用大小（MB）  =  0
  温热差异区空间总大小（MB）  =  0
    温热差异区视频大小（MB）  =  0
          温热差异区视频个数  =  0
        元数据最大内存（MB）  =  0
元数据当前内存使用大小（MB）  =  0
                  元数据个数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DCSVODINFO.md`
