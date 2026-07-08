---
id: UNC@20.15.2@MMLCommand@DSP GENERATESDC
type: MMLCommand
name: DSP GENERATESDC（查询强制产生业务数据容器结果）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GENERATESDC
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 离线计费维护
- 查询强制产生业务数据容器结果
status: active
---

# DSP GENERATESDC（查询强制产生业务数据容器结果）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

查询FOC GENERATESDC命令的执行结果。

## 注意事项

- 该命令执行后立即生效。
- 当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GENERATESDC]] · 强制产生业务数据容器（GENERATESDC）

## 使用实例

查询强制产生业务数据容器结果：

```
DSP GENERATESDC:;
```

```
 
 
Previously Focibly SDC Generation Result 
---------------------------------------- 
                                Time  =  2018-07-16 14:00:00 
 Porcess Online Charging User Number  =  50 
Porcess Offline Charging User Number  =  100 
                              Result  =  success 
(Number of results = 1) 
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询强制产生业务数据容器结果（DSP-GENERATESDC）_09897026.md`
