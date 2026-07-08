---
id: UNC@20.15.2@MMLCommand@LST CHARGECTRL
type: MMLCommand
name: LST CHARGECTRL（查询计费控制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHARGECTRL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 用户属性计费控制
status: active
---

# LST CHARGECTRL（查询计费控制配置）

## 功能

**适用NF：PGW-C、SMF**

此命令查询漫游、拜访、本地属性来控制是否提供在线计费、离线计费和融合计费能力。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHARGECTRL]] · 计费控制配置（CHARGECTRL）

## 使用实例

查询计费控制当前的配置：

```
LST CHARGECTRL:;
```

```

RETCODE = 0  操作成功

计费控制
--------
    归属地在线用户计费控制  =  允许
    归属地融合用户计费控制  =  禁止
    归属地离线用户计费控制  =  允许
拜访地在线计费用户计费控制  =  允许
拜访地离线计费用户计费控制  =  允许
拜访地融合计费用户计费控制  =  禁止
  漫游在线计费用户计费控制  =  允许
  漫游离线计费用户计费控制  =  允许
  漫游融合计费用户计费控制  =  禁止
 融合计费是否支持处理UPF上报的备份流量 = 使能
在线离线计费是否支持处理UPF上报的备份流量 = 使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询计费控制配置（LST-CHARGECTRL）_09896793.md`
