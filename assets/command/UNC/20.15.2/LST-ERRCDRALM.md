---
id: UNC@20.15.2@MMLCommand@LST ERRCDRALM
type: MMLCommand
name: LST ERRCDRALM（查询错误话单告警参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ERRCDRALM
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
- 错误话单告警管理
status: active
---

# LST ERRCDRALM（查询错误话单告警参数）

## 功能

**适用NF：NCG**

该命令用于查询NCG上报错误话单告警时对错误话单采用的监控模式。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/ERRCDRALM]] · 错误话单告警参数（ERRCDRALM）

## 使用实例

查询NCG对错误话单的监控模式：

```
LST ERRCDRALM:;
```

```
RETCODE = 0  操作成功。

结果如下:
------------
监控模式  =  周期性
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ERRCDRALM.md`
