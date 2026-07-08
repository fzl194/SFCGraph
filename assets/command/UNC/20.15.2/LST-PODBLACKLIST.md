---
id: UNC@20.15.2@MMLCommand@LST PODBLACKLIST
type: MMLCommand
name: LST PODBLACKLIST（查询Pod自愈黑名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PODBLACKLIST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST PODBLACKLIST（查询Pod自愈黑名单）

## 功能

该命令用于查询Pod自愈黑名单。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PODBLACKLIST]] · Pod自愈黑名单（PODBLACKLIST）

## 使用实例

查询Pod自愈黑名单。

```
%%LST PODBLACKLIST:;%%
RETCODE = 0  操作成功

结果如下
--------
Pod类型     

ipctrl-pod  
sbim-pod    
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Pod自愈黑名单（LST-PODBLACKLIST）_09587374.md`
