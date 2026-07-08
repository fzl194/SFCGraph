---
id: UDG@20.15.2@MMLCommand@LST QOSGLOBAL
type: MMLCommand
name: LST QOSGLOBAL（查询QosGlobal配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: QOSGLOBAL
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 流量管理
- Qos全局配置
status: active
---

# LST QOSGLOBAL（查询QosGlobal配置）

## 功能

**适用NF：UPF**

该命令用于显示全局的QoS信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/QOSGLOBAL]] · QosGlobal配置（QOSGLOBAL）

## 使用实例

查询QosGlobal配置：

```
LST QOSGLOBAL:;
```

```

RETCODE = 0  操作成功。

全局QoS配置信息
---------------
                      QoS功能开关  =  不使能
               下行与上行带宽比例  =  3
    具有最高优先级的non-GBR QCI值  =  5
                    Qos Profile名  =  globalqos
具有最高优先级的non-GBR PTT QCI值  =  69
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询QosGlobal配置（LST-QOSGLOBAL）_86528503.md`
