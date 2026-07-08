---
id: UDG@20.15.2@MMLCommand@DEA LICCTL
type: MMLCommand
name: DEA LICCTL（停止紧急License）
nf: UDG
version: 20.15.2
verb: DEA
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

# DEA LICCTL（停止紧急License）

## 功能

![](停止紧急License(DEA LICCTL)_46861743.assets/notice_3.0-zh-cn.png)

该功能关闭前请检查正在使用的License满足需要，请确认是否关闭。

该命令用于关闭License紧急状态。

该命令的使用场景为：License处于紧急状态下，使用本命令关闭License紧急状态。

> **说明**
> 当紧急License状态停止时系统按照License授权配置运行。

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LICCTL]] · 紧急License（LICCTL）

## 使用实例

关闭License紧急状态：

```
%%DEA LICCTL:;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DEA-LICCTL.md`
