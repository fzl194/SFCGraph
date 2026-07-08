---
id: UDG@20.15.2@MMLCommand@LST GLBTRUNKREMARK
type: MMLCommand
name: LST GLBTRUNKREMARK（查询整机Trunk Remark配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBTRUNKREMARK
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 宽带集群流量管理
- 全局宽带集群QoS到DSCP或TOS映射
status: active
---

# LST GLBTRUNKREMARK（查询整机Trunk Remark配置）

## 功能

**适用NF：SGW-U、PGW-U**

该命令用于查询整机所有的Trunk Remark配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [整机Trunk Remark配置（GLBTRUNKREMARK）](configobject/UDG/20.15.2/GLBTRUNKREMARK.md)

## 使用实例

查询整机的Trunk Remark配置：

```
LST GLBTRUNKREMARK:;
```

```

RETCODE = 0  操作成功

宽带集群重标记配置信息
----------------------
QCI  ARP的优先级别  标记类型  DSCP  AF级别  AF丢弃优先级  TOS值  DSCP值  

1    1              TOS       EF    0       0             3      0       
1    2              TOS       EF    0       0             5      0       
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询整机Trunk-Remark配置（LST-GLBTRUNKREMARK）_70522432.md`
