---
id: UDG@20.15.2@MMLCommand@DSP DCSNODE
type: MMLCommand
name: DSP DCSNODE（显示DCS微服务节点状态信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DCSNODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- MML命令
- 系统资源管理
status: active
---

# DSP DCSNODE（显示DCS微服务节点状态信息）

## 功能

该命令用于显示DCS微服务节点状态信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DCSNODE]] · DCS微服务节点状态信息（DCSNODE）

## 使用实例

显示所有实例的节点状态信息。

```
%%DSP DCSNODE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
              POD名称  =  relay-pod-0
             节点状态  =  节点状态正常
      内存总容量（MB） =  56500
      内存使用量（MB） =  15665
      磁盘总容量（MB） =  2103
      磁盘使用量（MB） =  612
节点写入速率（Mbit/s） =  0
节点读取速率（Mbit/s） =  0
磁盘写入速率（Mbit/s） =  0
磁盘读取速率（Mbit/s） =  0
跨板写入速率（Mbit/s） =  0
跨板读取速率（Mbit/s） =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DCSNODE.md`
