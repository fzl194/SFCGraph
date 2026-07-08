---
id: UDG@20.15.2@MMLCommand@LST DCSSDPARA
type: MMLCommand
name: LST DCSSDPARA（查询DCS直通存储慢盘检测参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DCSSDPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- MML命令
- 系统资源配置
status: active
---

# LST DCSSDPARA（查询DCS直通存储慢盘检测参数）

## 功能

该命令用于查询DCS直通存储慢盘检测参数。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/DCSSDPARA]] · DCS直通存储慢盘检测参数（DCSSDPARA）

## 使用实例

查询DCS直通存储慢盘检测参数

```
%%LST DCSSDPARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------
   慢盘检测开关  =  开启
       检测次数  =  30
    检测周期(s)  =  1
 IO服务时间(ms)  =  30
    IO使用率(%)  =  98
慢盘故障阈值(%)  =  70
慢盘恢复阈值(%)  =  50
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DCS直通存储慢盘检测参数（LST-DCSSDPARA）_41105089.md`
