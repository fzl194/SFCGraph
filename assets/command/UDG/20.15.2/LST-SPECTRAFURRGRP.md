---
id: UDG@20.15.2@MMLCommand@LST SPECTRAFURRGRP
type: MMLCommand
name: LST SPECTRAFURRGRP（查询全局缺省费率的流量使用量上报规则组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SPECTRAFURRGRP
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 特殊流量使用量上报规则组
status: active
---

# LST SPECTRAFURRGRP（查询全局缺省费率的流量使用量上报规则组）

## 功能

**适用NF：UPF**

本条命令用于查询全局缺省费率的使用量上报规则组。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SPECTRAFURRGRP]] · 全局缺省费率的流量使用量上报规则组（SPECTRAFURRGRP）

## 使用实例

查询显示全局缺省费率的使用量上报规则组：

```
LST SPECTRAFURRGRP:;
```

```

RETCODE = 0 操作成功。 
： 
使用量上报规则组名称 =  spec
 (结果个数 = 1) 
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局缺省费率的流量使用量上报规则组（LST-SPECTRAFURRGRP）_36146716.md`
