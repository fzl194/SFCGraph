---
id: UDG@20.15.2@MMLCommand@LST QOSURRRPTCTRL
type: MMLCommand
name: LST QOSURRRPTCTRL（查询QoS URR上报的相关参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: QOSURRRPTCTRL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 业务QOS控制
- QoS类型URR上报控制
status: active
---

# LST QOSURRRPTCTRL（查询QoS URR上报的相关参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询QoS URR上报的相关参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/QOSURRRPTCTRL]] · QoS URR上报的相关参数（QOSURRRPTCTRL）

## 使用实例

查询QoS URR上报的相关参数：

```
LST QOSURRRPTCTRL:;
```

```

RETCODE = 0 操作成功。

设置QoS URR上报的的相关参数。
------------------------
   QoS类型URR Stop上报迟滞时间（秒）  =  20
Rule删除时触发QoS URR Stop上报的开关  = 使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-QOSURRRPTCTRL.md`
