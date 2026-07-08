---
id: UNC@20.15.2@MMLCommand@LST CACHEPLCY
type: MMLCommand
name: LST CACHEPLCY（查询缓存策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CACHEPLCY
command_category: 查询类
applicable_nf:
- AMF
- SMF
- SMSF
- NCG
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF Cache管理
status: active
---

# LST CACHEPLCY（查询缓存策略）

## 功能

**适用NF：AMF、SMF、SMSF、NCG、NSSF**

该命令用于查询缓存策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [缓存策略（CACHEPLCY）](configobject/UNC/20.15.2/CACHEPLCY.md)

## 使用实例

查询缓存策略。

```
%%LST CACHEPLCY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
        缓存策略  =  全部缓存模式
快速老化时间(秒)  =  600
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询缓存策略（LST-CACHEPLCY）_18037977.md`
