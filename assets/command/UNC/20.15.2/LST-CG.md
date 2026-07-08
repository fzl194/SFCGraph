---
id: UNC@20.15.2@MMLCommand@LST CG
type: MMLCommand
name: LST CG（查询CG）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CG
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
- CG管理
status: active
---

# LST CG（查询CG）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

LST CG命令用来查询系统当前CG配置表中所有CG的参数配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CG]] · CG（CG）

## 使用实例

查询系统当前CG配置表中所有CG的参数配置信息：

```
LST CG:;
```

```

RETCODE = 0 操作成功。

CG参数配置
----------
        CG端口号  =  25009
            等级  =  1
        话单类型  =  R9 PGW
           WAL值  =  0
         CG 地址  =  192.168.0.2
            域名  =  NULL
Ga接口本端端口号  =  NULL
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CG（LST-CG）_09896848.md`
