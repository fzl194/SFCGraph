---
id: UNC@20.15.2@MMLCommand@LST QOSREMARK
type: MMLCommand
name: LST QOSREMARK（查询全局QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSREMARK
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 全局QoS功能配置
- 全局DSCP_ToS映射功能
status: active
---

# LST QOSREMARK（查询全局QoS到TOS/DSCP的映射规则）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询系统上下行QoS映射功能配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QOSREMARK]] · 全局QoS到TOS/DSCP的映射规则（QOSREMARK）

## 使用实例

查询系统上下行QoS映射功能配置：

```
%%LST QOSREMARK:;%%
RETCODE = 0  操作成功

操作结果如下
------------
下行标记  =  使能
上行标记  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-QOSREMARK.md`
