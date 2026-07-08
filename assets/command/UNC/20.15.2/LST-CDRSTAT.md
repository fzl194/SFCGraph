---
id: UNC@20.15.2@MMLCommand@LST CDRSTAT
type: MMLCommand
name: LST CDRSTAT（查询话单统计）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDRSTAT
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 话单统计
status: active
---

# LST CDRSTAT（查询话单统计）

## 功能

**适用NF：NCG**

该命令用于查询当前的话单统计信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRSTAT]] · 话单统计（CDRSTAT）

## 使用实例

查询系统当前的话单统计配置：

```
LST CDRSTAT:;
```

```
RETCODE = 0  操作成功
  
结果如下: 
---------
         话单统计标识  =  cdrstat1
     接入网元分组标识  =  PS2
             通道名称  =  CHFCDR
         数据网络名称  =  huawei.com
     统计结果保存天数  =  30
     话单文件开始时间  =  2024-06-11 10:33:27
     话单文件结束时间  =  2024-06-11 23:33:56
         统计开始时间  =  00:30
         统计结束时间  =  05:00
 结果文件输出时间阈值  =  1440
     文件定时扫描间隔  =  3600
         会话老化时长  =  21600
       话单统计匿名化  =  关闭
 (结果个数 = 1)
  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CDRSTAT.md`
