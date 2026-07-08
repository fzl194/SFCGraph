---
id: UNC@20.15.2@MMLCommand@LST UPCSCANRATE
type: MMLCommand
name: LST UPCSCANRATE（查询用户面控制扫描速率）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPCSCANRATE
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- 用户面控制扫描速率管理
status: active
---

# LST UPCSCANRATE（查询用户面控制扫描速率）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于查询用户面控制扫描速率。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPCSCANRATE]] · 用户面控制扫描速率（UPCSCANRATE）

## 使用实例

查询用户面控制扫描速率配置，执行如下命令：

```
%%LST UPCSCANRATE:;%%
RETCODE = 0  操作成功

结果如下
--------
扫描任务类型       扫描速率(个/秒)      扫描间隔（秒）

去激活任务         1                    0
检查任务           1                    0
日常检查任务       1                    0
迁移任务           1                    0
地址去活任务       1                    0
惯性运行任务       1                    0
N3/N9链路故障任务  1                    0
GTPU链路故障任务   1                    0
APN故障任务        1                    0
路径故障迁移任务   1                    0
路径迁移任务       1                    0
故障恢复回迁任务   10                   5
(结果个数 = 12)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPCSCANRATE.md`
