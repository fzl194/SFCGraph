---
id: UDG@20.15.2@MMLCommand@LST DCSVODPARAS
type: MMLCommand
name: LST DCSVODPARAS（查询DCS点播参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DCSVODPARAS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- MML命令
- 系统资源配置
status: active
---

# LST DCSVODPARAS（查询DCS点播参数）

## 功能

该命令用于查询DCS点播参数。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [DCS点播参数（DCSVODPARAS）](configobject/UDG/20.15.2/DCSVODPARAS.md)

## 使用实例

查询DCS点播参数。

```
%%LST DCSVODPARAS:;%%
RETCODE = 0  操作成功

操作结果如下：
------------------------
          热度更新频次  =  100
          系统最大热度  =  20000
     热度衰减速率（%）  =  50
   L0加入热度阈值（%）  =  95
   L2最大节点容量（G）  =  14336
 磁盘淘汰起始阈值（G）  =  500
 磁盘老化对象大小（G）  =  300
元数据淘汰起始阈值（%） =  95
    元数据老化对象个数  =  2000
 对象强制老化周期（h）  =  168
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DCS点播参数（LST-DCSVODPARAS）_11535957.md`
