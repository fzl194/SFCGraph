---
id: UNC@20.15.2@MMLCommand@LST GLBPGWCHGPAUSE
type: MMLCommand
name: LST GLBPGWCHGPAUSE（查询全局计费暂停配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBPGWCHGPAUSE
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 计费暂停管理
- PGW计费暂停管理
status: active
---

# LST GLBPGWCHGPAUSE（查询全局计费暂停配置）

## 功能

**适用NF：PGW-C**

该命令用于查询全局的PGW的计费暂停功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GLBPGWCHGPAUSE]] · 全局计费暂停配置（GLBPGWCHGPAUSE）

## 使用实例

显示全局计费暂停配置：

```
%%LST GLBPGWCHGPAUSE:;%%
RETCODE = 0  操作成功

结果如下
--------
计费暂停开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GLBPGWCHGPAUSE.md`
