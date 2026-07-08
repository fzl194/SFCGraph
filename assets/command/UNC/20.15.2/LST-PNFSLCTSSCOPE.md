---
id: UNC@20.15.2@MMLCommand@LST PNFSLCTSSCOPE
type: MMLCommand
name: LST PNFSLCTSSCOPE（查询选择对端NF时使用的业务服务区）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFSLCTSSCOPE
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- PCC公共参数
status: active
---

# LST PNFSLCTSSCOPE（查询选择对端NF时使用的业务服务区）

## 功能

**适用NF：SMF**

该命令用于查询选择对端NF时使用的业务服务区。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFSLCTSSCOPE]] · 选择对端NF时使用的业务服务区（PNFSLCTSSCOPE）

## 使用实例

查询选择对端NF时使用的业务服务区。

```
LST PNFSLCTSSCOPE:;
RETCODE = 0  操作成功

结果如下
--------
对端NF类型  =  默认的对端NF类型
服务区名称  =  ServingScope1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PNFSLCTSSCOPE.md`
