---
id: UNC@20.15.2@MMLCommand@LST QOSGLOBAL
type: MMLCommand
name: LST QOSGLOBAL（查询全局QoS配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSGLOBAL
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 全局QoS功能配置
- 全局QoS参数
status: active
---

# LST QOSGLOBAL（查询全局QoS配置）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询全局的QoS信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSGLOBAL]] · 全局QoS配置（QOSGLOBAL）

## 使用实例

查询全局的QoS信息。

```
%%LST QOSGLOBAL:;%%
RETCODE = 0  操作成功

全局QoS配置信息
---------------
   Qos Profile名  =  globalqos
绑定PreR8用户QoS  =  不使能
PreR8用户QoS索引  =  256
  绑定EPS用户QoS  =  不使能
  EPS用户QoS索引  =  256
   绑定5G用户QoS  =  不使能
   5G用户QoS索引  =  256
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-QOSGLOBAL.md`
