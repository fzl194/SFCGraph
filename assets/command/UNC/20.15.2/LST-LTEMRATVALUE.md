---
id: UNC@20.15.2@MMLCommand@LST LTEMRATVALUE
type: MMLCommand
name: LST LTEMRATVALUE（查询LTE-M用户的RAT值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LTEMRATVALUE
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- LTE-M用户RAT值
status: active
---

# LST LTEMRATVALUE（查询LTE-M用户的RAT值）

## 功能

**适用NF：PGW-C、SGW-C、SMF**

该命令用于查询终端通过LTE-M接入方式时UNC给周边网元发送消息时RAT信元中携带的值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/LTEMRATVALUE]] · LTE-M用户的RAT值（LTEMRATVALUE）

## 使用实例

查询终端通过LTE-M接入方式时，UNC给周边网元发送的消息中RAT信元携带的值：

```
%%LST LTEMRATVALUE:;%%
RETCODE = 0  操作成功

结果如下
--------
                和OCS交互使用的RAT值  =  LTE_M
                和CHF交互使用的RAT值  =  LTE_M
                 和CG交互使用的RAT值  =  LTE_M
      和AAA计费服务器交互使用的RAT值  =  LTE_M
      和AAA鉴权服务器交互使用的RAT值  =  LTE_M
               和PCRF交互使用的RAT值  =  LTE_M
                和PCF交互使用的RAT值  =  LTE_M
UNC作为SGW-C发送给PGW-C时使用的RAT值  =  LTE_M
                和UPF交互使用的RAT值  =  LTE_M
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LTEMRATVALUE.md`
