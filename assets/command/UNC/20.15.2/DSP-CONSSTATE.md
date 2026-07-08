---
id: UNC@20.15.2@MMLCommand@DSP CONSSTATE
type: MMLCommand
name: DSP CONSSTATE（显示消费者状态信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CONSSTATE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Diameter管理
- 消费者状态
status: active
---

# DSP CONSSTATE（显示消费者状态信息）

## 功能

该命令用于显示Diameter消费者状态信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [消费者状态信息（CONSSTATE）](configobject/UNC/20.15.2/CONSSTATE.md)

## 使用实例

显示Diameter消费者状态信息：

```
DSP CONSSTATE:;
```

```

RETCODE = 0 操作成功

结果如下
-------------------------
用户PID   状态   发送信息计数 接收信息计数

0x1da4653 激活   3            4
0x2de4651 激活   3            4
(结果个数 = 2)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示消费者状态信息（DSP-CONSSTATE）_50121846.md`
