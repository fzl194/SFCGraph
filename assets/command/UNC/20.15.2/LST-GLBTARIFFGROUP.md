---
id: UNC@20.15.2@MMLCommand@LST GLBTARIFFGROUP
type: MMLCommand
name: LST GLBTARIFFGROUP（查询全局费率切换组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBTARIFFGROUP
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 费率切换
- 全局费率切换组
status: active
---

# LST GLBTARIFFGROUP（查询全局费率切换组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查询全局绑定的费率切换组。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBTARIFFGROUP]] · 全局费率切换组（GLBTARIFFGROUP）

## 使用实例

查询全局绑定的费率切换组，命令为：

```
LST GLBTARIFFGROUP:;
```

```

RETCODE = 0  操作成功。

全局费率组
----------
费率切换组名  =  huawei
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GLBTARIFFGROUP.md`
