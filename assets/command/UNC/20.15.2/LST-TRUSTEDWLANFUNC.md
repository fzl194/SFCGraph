---
id: UNC@20.15.2@MMLCommand@LST TRUSTEDWLANFUNC
type: MMLCommand
name: LST TRUSTEDWLANFUNC（查询可信Non-3GPP接入开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TRUSTEDWLANFUNC
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- WLAN控制管理
status: active
---

# LST TRUSTEDWLANFUNC（查询可信Non-3GPP接入开关）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询可信Non-3GPP接入开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/TRUSTEDWLANFUNC]] · 可信Non-3GPP接入开关（TRUSTEDWLANFUNC）

## 使用实例

查询可信Non-3GPP接入开关：

```
%%LST TRUSTEDWLANFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
可信Non-3GPP接入开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-TRUSTEDWLANFUNC.md`
