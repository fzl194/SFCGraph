---
id: UNC@20.15.2@MMLCommand@LST SMFSERVICELIST
type: MMLCommand
name: LST SMFSERVICELIST（查询特定SMF功能实例服务名）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFSERVICELIST
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# LST SMFSERVICELIST（查询特定SMF功能实例服务名）

## 功能

**适用NF：SMF**

本命令用于查询特定SMF功能实例的服务列表。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFSERVICELIST]] · 特定SMF功能实例服务名（SMFSERVICELIST）

## 使用实例

查询SMF功能实体服务列表：

```
%%LST SMFSERVICELIST:;%%
RETCODE = 0  操作成功

结果如下
------------------------
服务名称  =  SMF-SERVICENAME001
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFSERVICELIST.md`
