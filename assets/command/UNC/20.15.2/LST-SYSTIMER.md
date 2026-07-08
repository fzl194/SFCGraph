---
id: UNC@20.15.2@MMLCommand@LST SYSTIMER
type: MMLCommand
name: LST SYSTIMER（查询系统定时器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SYSTIMER
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 维护管理
- 设置系统定时器
status: active
---

# LST SYSTIMER（查询系统定时器）

## 功能

**适用NF：NCG**

该命令用于查询NCG的系统定时器信息。

## 注意事项

定时器时长的单位为分钟。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SYSTIMER]] · 系统定时器（SYSTIMER）

## 使用实例

查询NCG的系统定时器信息：

```
LST SYSTIMER:;
```

```
RETCODE = 0  操作成功。

结果如下:
---------
定时器名称                      定时器时长(分钟)

统计2G/3G的PDP信息老化定时器    30              
统计4G的Bearer信息老化定时器    75              
统计5G的Bearer信息老化定时器    75              
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SYSTIMER.md`
