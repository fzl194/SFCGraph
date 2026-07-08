---
id: UDG@20.15.2@MMLCommand@DSP DCSLIVEINFO
type: MMLCommand
name: DSP DCSLIVEINFO（显示直播视频信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DCSLIVEINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- MML命令
- 系统资源管理
status: active
---

# DSP DCSLIVEINFO（显示直播视频信息）

## 功能

本命令用于显示直播视频信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/DCSLIVEINFO]] · 直播视频信息（DCSLIVEINFO）

## 使用实例

显示所有实例的直播视频信息。

```
%%DSP DCSLIVEINFO:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                实例ID  =  1837857504428137284
内存空间最大大小（MB）  =  5160
内存空间申请大小（MB）  =  10
            直播用户数  =  63
          直播视频个数  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DCSLIVEINFO.md`
