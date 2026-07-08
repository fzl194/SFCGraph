---
id: UNC@20.15.2@MMLCommand@LST DIAMDICTPATH
type: MMLCommand
name: LST DIAMDICTPATH（查询Diameter字典加载路径）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DIAMDICTPATH
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter字典管理
- 加载路径
status: active
---

# LST DIAMDICTPATH（查询Diameter字典加载路径）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询Diameter字典加载路径。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIAMDICTPATH]] · Diameter字典加载路径（DIAMDICTPATH）

## 使用实例

当需要查询当前配置的Diameter字典加载路径时：

```
LST DIAMDICTPATH:;
```

```

RETCODE = 0  操作成功

Diameter字典加载路径
--------------------
应用  字典序号  字典加载路径     

Gy    1         EPC标准字典路径  
Gy    2         定制字典路径2    
Gx    1         定制字典路径1    
S6b   1         EPC标准字典路径  
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Diameter字典加载路径（LST-DIAMDICTPATH）_09897250.md`
