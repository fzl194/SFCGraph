---
id: UNC@20.15.2@MMLCommand@DSP CONSSTATIC
type: MMLCommand
name: DSP CONSSTATIC（显示消费者统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CONSSTATIC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Diameter管理
- 消费者统计
status: active
---

# DSP CONSSTATIC（显示消费者统计信息）

## 功能

该命令用于显示Diameter消费者统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CONSSTATIC]] · 消费者统计信息（CONSSTATIC）

## 使用实例

显示Diameter消费者统计信息：

```
DSP CONSSTATIC:;
```

```

RETCODE = 0 操作成功

结果如下
------------------------
用户PID        发送用户信息      接收用户信息        丢弃用户信息    最大延迟时间   消息重传计数

0x2DF004B      28                314                 0               0              0
0x2DC004A      128               2437                0               0              0
0x1DA0007      128               16                  0               0              0
0x2DE0005      28                22                  0               0              0
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-CONSSTATIC.md`
