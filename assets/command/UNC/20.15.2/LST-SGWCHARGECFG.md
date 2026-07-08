---
id: UNC@20.15.2@MMLCommand@LST SGWCHARGECFG
type: MMLCommand
name: LST SGWCHARGECFG（查询SGW计费配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGWCHARGECFG
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- SGW计费控制
- SGW计费基础参数
status: active
---

# LST SGWCHARGECFG（查询SGW计费配置）

## 功能

**适用NF：SGW-C**

LST SGWCHARGECFG命令用来查询SGW计费配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [SGW计费配置（SGWCHARGECFG）](configobject/UNC/20.15.2/SGWCHARGECFG.md)

## 使用实例

当需要查询SGW计费配置，即本地用户、漫游用户、拜访用户的离线计费开关是否打开时，将命令配置为：

```
LST SGWCHARGECFG:;
```

```

RETCODE = 0  操作成功。

SGW计费控制
-----------
本地用户离线计费开关  =  禁止
漫游用户离线计费开关  =  允许
拜访用户离线计费开关  =  允许
       SGW CG IP选择  =  使用本地CG IP
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SGW计费配置（LST-SGWCHARGECFG）_09896990.md`
