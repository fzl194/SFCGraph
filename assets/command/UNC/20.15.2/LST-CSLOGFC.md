---
id: UNC@20.15.2@MMLCommand@LST CSLOGFC
type: MMLCommand
name: LST CSLOGFC（查询日志流控开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CSLOGFC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# LST CSLOGFC（查询日志流控开关）

## 功能

此命令用于查询日志流控开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/CSLOGFC]] · 日志流控开关（CSLOGFC）

## 使用实例

查询日志留空开关：

```
%%LST CSLOGFC:;%%
RETCODE = 0  操作成功

结果如下
--------
流控开关  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询日志流控开关（LST-CSLOGFC）_09587860.md`
