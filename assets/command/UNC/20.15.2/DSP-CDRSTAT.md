---
id: UNC@20.15.2@MMLCommand@DSP CDRSTAT
type: MMLCommand
name: DSP CDRSTAT（显示话单统计信息）
nf: UNC
version: 20.15.2
verb: DSP
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

# DSP CDRSTAT（显示话单统计信息）

## 功能

**适用NF：NCG**

该命令用于显示话单统计任务的状态。该命令执行后，系统返回相应的话单统计任务状态值。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CDRSTAT]] · 话单统计（CDRSTAT）

## 使用实例

显示所有话单统计任务状态：

```
DSP CDRSTAT:;
```

```
RETCODE = 0  操作成功
  
结果如下: 
---------
     话单统计标识  =  cdrstat1
 接入网元分组标识  =  PS2
           RU的ID  =  65
   当前统计文件名  =  ./frontsave/AP65_1/20240611/AP65_10000000004.bil
     文件修改时间  =  2024-06-11 20:42:35
     话单统计状态  =  进行中
 (结果个数 = 1)
  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-CDRSTAT.md`
