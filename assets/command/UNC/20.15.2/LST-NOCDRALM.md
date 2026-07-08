---
id: UNC@20.15.2@MMLCommand@LST NOCDRALM
type: MMLCommand
name: LST NOCDRALM（查询未接收到话单告警参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NOCDRALM
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
- 未接收到话单告警参数
status: active
---

# LST NOCDRALM（查询未接收到话单告警参数）

## 功能

**适用NF：NCG**

该命令用于查询 [**ALM-82021 NCG长时间未接收到话单**](../../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82021 vCG长时间未接收到话单_51174216.md) 告警的监控参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/NOCDRALM]] · 未接收到话单告警参数（NOCDRALM）

## 使用实例

查询 [**ALM-82021 NCG长时间未接收到话单**](../../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82021 vCG长时间未接收到话单_51174216.md) 告警的监控参数：

```
LST NOCDRALM:;
```

```
RETCODE = 0  操作成功。

结果如下:
------------
          告警开关  =  开启
告警检测周期(分钟)  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NOCDRALM.md`
