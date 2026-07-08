---
id: UNC@20.15.2@MMLCommand@LST CRACTRL
type: MMLCommand
name: LST CRACTRL（显示CRA控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CRACTRL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- CRA控制
status: active
---

# LST CRACTRL（显示CRA控制参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询实时位置上报的开关和本地Trigger的功能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CRACTRL]] · CRA控制参数（CRACTRL）

## 使用实例

查询实时位置上报的开关和本地Trigger：

```
LST CRACtrl:;
```

```

RETCODE = 0  操作成功

CRA控制参数
-----------
CRA控制  =  LOCAL
    TAI  =  使能
   ECGI  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CRACTRL.md`
