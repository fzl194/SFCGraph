---
id: UNC@20.15.2@MMLCommand@LST SCTPINITFLOW
type: MMLCommand
name: LST SCTPINITFLOW（查询SCTP接入流控）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCTPINITFLOW
command_category: 查询类
applicable_nf:
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# LST SCTPINITFLOW（查询SCTP接入流控）

## 功能

**适用NF：MME、AMF**

该命令用于查询系统中SCTP接入流控参数。

## 注意事项

无。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPINITFLOW]] · SCTP接入流控（SCTPINITFLOW）

## 使用实例

查询SCTP接入流控参数信息：

```
LST SCTPINITFLOW:;
```

```
操作结果如下
------------
      流控开关  =  开启
S1固定流控速率  =  2000
N2固定流控速率  =  2000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SCTPINITFLOW.md`
