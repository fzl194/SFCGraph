---
id: UDG@20.15.2@MMLCommand@ACT LICCTL
type: MMLCommand
name: ACT LICCTL（启动紧急License）
nf: UDG
version: 20.15.2
verb: ACT
object_keyword: LICCTL
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# ACT LICCTL（启动紧急License）

## 功能

![](启动紧急License(ACT LICCTL)_46781803.assets/notice_3.0-zh-cn.png)

大版本内该功能只能开启3次，请确认是否打开。

该命令用于系统License启动紧急状态。启动紧急功能打开时系统按照最大配置运行。

该命令的使用场景为：在紧急情况下，且无法获取到正确的License时，可以使用本命令用于系统License启动紧急功能。

> **说明**
> 一个大版本中最多可启动紧急功能3次，每次可持续7天。 启动紧急后，具有最高优先级；在停止紧急或紧急到期失效后，会以加载的License为准。

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/LICCTL]] · 紧急License（LICCTL）

## 使用实例

启动紧急License状态：

```
%%ACT LICCTL:;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ACT-LICCTL.md`
