---
id: UNC@20.15.2@MMLCommand@LST QOSFLOWFUNC
type: MMLCommand
name: LST QOSFLOWFUNC（查询QoS Flow功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSFLOWFUNC
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话策略管理
- 5GC QoS Flow管理拓展功能
status: active
---

# LST QOSFLOWFUNC（查询QoS Flow功能）

## 功能

**适用NF：SMF**

该命令用于查询QoS Flow相关功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSFLOWFUNC]] · QoS Flow功能（QOSFLOWFUNC）

## 使用实例

查询QoS Flow功能，执行如下命令：

```
LST QOSFLOWFUNC:;
RETCODE = 0  操作成功

结果如下
--------
 EPS切换到5GS专有GBR类型QoS Flow策略  =  释放专有QoS Flow
插入删除I-SMF专有GBR类型QoS Flow策略  =  不释放专有QoS Flow
 延迟释放专有GBR类型QoS Flow时长(秒)  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-QOSFLOWFUNC.md`
