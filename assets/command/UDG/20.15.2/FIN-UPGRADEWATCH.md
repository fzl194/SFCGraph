---
id: UDG@20.15.2@MMLCommand@FIN UPGRADEWATCH
type: MMLCommand
name: FIN UPGRADEWATCH（结束升级观察期）
nf: UDG
version: 20.15.2
verb: FIN
object_keyword: UPGRADEWATCH
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 升级补丁管理
- 观察期管理
status: active
---

# FIN UPGRADEWATCH（结束升级观察期）

## 功能

![](结束升级观察期(FIN UPGRADEWATCH)_13690342.assets/notice_3.0-zh-cn.png)

执行此命令会结束所有网元升级观察期后，且无法回退到升级前的版本，请谨慎操作。

该命令用于结束所有网元的升级观察期。

> **说明**
> - 执行此命令后会尝试结束大颗粒服务观察期，即使无网元处于升级观察期状态也会执行此操作。

## 参数

无。

## 操作的配置对象

- [升级观察期（UPGRADEWATCH）](configobject/UDG/20.15.2/UPGRADEWATCH.md)

## 使用实例

结束升级观察期。

```
%%FIN UPGRADEWATCH:;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/结束升级观察期(FIN-UPGRADEWATCH)_13690342.md`
