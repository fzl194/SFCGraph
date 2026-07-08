---
id: UDG@20.15.2@MMLCommand@LST PATHDWNALMGLO
type: MMLCommand
name: LST PATHDWNALMGLO（查询单条路径断告警抑制参数全局配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PATHDWNALMGLO
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务告警管理
- 单条路径断告警配置
status: active
---

# LST PATHDWNALMGLO（查询单条路径断告警抑制参数全局配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询单条路径断告警抑制参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PATHDWNALMGLO]] · 单条路径断告警抑制参数全局配置（PATHDWNALMGLO）

## 使用实例

查询ALM-81018 GTPU路径断告警抑制参数：

```
LST PATHDWNALMGLO:;
```

```

RETCODE = 0  操作成功。

单路径告警抑制参数全局配置
--------------------------
告警上报的连续中断次数  =  5
    告警上报的探测次数  =  5
告警上报的累计中断次数  =  3
告警恢复的连续正常次数  = 5
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PATHDWNALMGLO.md`
