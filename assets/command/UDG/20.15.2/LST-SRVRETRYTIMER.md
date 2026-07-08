---
id: UDG@20.15.2@MMLCommand@LST SRVRETRYTIMER
type: MMLCommand
name: LST SRVRETRYTIMER（查询服务重试等待时间）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SRVRETRYTIMER
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- 服务重试定时器
status: active
---

# LST SRVRETRYTIMER（查询服务重试等待时间）

## 功能

**适用NF：PGW-U、UPF**

此命令用于显示服务上报出现上报失败/上报响应超时/响应失败的异常场景后重新发起上报需要等待的时间。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVRETRYTIMER]] · 服务重试等待时间（SRVRETRYTIMER）

## 使用实例

查询服务重新上报需要等待的时间：

```
LST SRVRETRYTIMER:;
```

```

RETCODE = 0 操作成功。
服务重试定时器信息
------------------
      ADC重新上报等待时间（秒） = 40
      QOS重新上报等待时间（秒） = 50
Tethering重新上报等待时间（秒） = 60
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询服务重试等待时间（LST-SRVRETRYTIMER）_06055000.md`
