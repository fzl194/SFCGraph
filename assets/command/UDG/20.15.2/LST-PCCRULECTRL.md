---
id: UDG@20.15.2@MMLCommand@LST PCCRULECTRL
type: MMLCommand
name: LST PCCRULECTRL（查询PCC QoS相关控制参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PCCRULECTRL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 业务QOS控制
- PCC QoS相关控制
status: active
---

# LST PCCRULECTRL（查询PCC QoS相关控制参数）

## 功能

**适用NF：PGW-U、UPF**

此命令用于显示PCC动态Rule生成的QoS Rule优先级是否按照PCF下发的优先级进行控制。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PCCRULECTRL]] · PCC QoS相关控制参数（PCCRULECTRL）

## 使用实例

当运营商需要查询QosRulePrio参数当前的值时，需要执行：

```
LST PCCRULECTRL:;
```

```

RETCODE = 0 操作成功。

PCC QoS相关控制参数
------------------------
QoS Rule优先级设置原则 = 等于PCC Rule优先级
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PCC-QoS相关控制参数（LST-PCCRULECTRL）_08342474.md`
