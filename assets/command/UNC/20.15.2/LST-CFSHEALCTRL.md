---
id: UNC@20.15.2@MMLCommand@LST CFSHEALCTRL
type: MMLCommand
name: LST CFSHEALCTRL（查询在复杂故障场景下自愈功能控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CFSHEALCTRL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST CFSHEALCTRL（查询在复杂故障场景下自愈功能控制参数）

## 功能

该命令用于查询在复杂故障场景下自愈功能控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/CFSHEALCTRL]] · 在复杂故障场景下自愈功能控制参数（CFSHEALCTRL）

## 使用实例

显示在复杂故障场景下自愈功能控制参数。

```
%%LST CFSHEALCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
         通信亚健康隔离功能开关  =  关闭
       亚健康诊断等待时间(分钟)  =  10
         Q922连续诊断周期（次）  =  3
网元级KPI异常检测与容灾功能开关  =  关闭
         容灾决策等待时间（秒）  =  300
                   容灾执行策略  =  手动
         单主机异常自愈功能开关  =  开启
     诊断隔离处理等待时间（秒）  =  120
                  异常阈值（%）  =  90
                      差值（%）  =  20
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CFSHEALCTRL.md`
