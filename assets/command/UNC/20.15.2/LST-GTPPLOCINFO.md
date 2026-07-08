---
id: UNC@20.15.2@MMLCommand@LST GTPPLOCINFO
type: MMLCommand
name: LST GTPPLOCINFO（查询GTPP本端信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPPLOCINFO
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
- 离线计费
- GTPP信令
- GTPP本地信息
status: active
---

# LST GTPPLOCINFO（查询GTPP本端信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询GTPP本端信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPPLOCINFO]] · GTPP本端信息（GTPPLOCINFO）

## 使用实例

查询GTPP本端信息：

```
LST GTPPLOCINFO:;
```

```

RETCODE = 0  操作成功

GTPP本端主机信息
----------------
    本端主机名  =  test
      本端域名  =  test
业务上下文标识  =  abc
    本端接口名  =  gaif1/0/1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTPP本端信息（LST-GTPPLOCINFO）_09896858.md`
