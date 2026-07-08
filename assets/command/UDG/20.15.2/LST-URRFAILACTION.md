---
id: UDG@20.15.2@MMLCommand@LST URRFAILACTION
type: MMLCommand
name: LST URRFAILACTION（显示计费URR上报失败动作参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: URRFAILACTION
command_category: 查询类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 计费URR上报失败时的处理动作
status: active
---

# LST URRFAILACTION（显示计费URR上报失败动作参数）

## 功能

**适用NF：UPF**

本条命令用于查询计费URR上报失败的动作。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@URRFAILACTION]] · 计费URR上报失败动作参数（URRFAILACTION）

## 使用实例

查询URR上报失败动作：

```
LST URRFAILACTION:;
```

```

RETCODE = 0  操作成功

配额申请失败动作信息
--------------------
        重发间隔  =  60
        重发次数  =  2
重发失败后的动作  =  阻塞
        保持时长  =  30
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-URRFAILACTION.md`
