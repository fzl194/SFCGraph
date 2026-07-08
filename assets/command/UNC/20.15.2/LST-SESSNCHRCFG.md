---
id: UNC@20.15.2@MMLCommand@LST SESSNCHRCFG
type: MMLCommand
name: LST SESSNCHRCFG（查询会话CHR上报策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SESSNCHRCFG
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
- CHR管理
- 会话CHR配置
status: active
---

# LST SESSNCHRCFG（查询会话CHR上报策略）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询会话CHR单据采集及订阅流程和上报CHR单据的UNC产品设备号。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SESSNCHRCFG]] · 会话CHR上报策略（SESSNCHRCFG）

## 使用实例

查询会话CHR采集及订阅流程：

```
LST SESSNCHRCFG:;
RETCODE = 0 操作成功。

结果如下
------------------------
高性能服务器上报流程控制模板索引  =  0
低性能服务器上报流程控制模板索引  =  1
(结果个数= 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SESSNCHRCFG.md`
