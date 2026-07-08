---
id: UDG@20.15.2@MMLCommand@LST SAAITRAINPARA
type: MMLCommand
name: LST SAAITRAINPARA（查询基于SA的Intelligence训练参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SAAITRAINPARA
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- SAPO服务管理
- SAPO训练参数
status: active
---

# LST SAAITRAINPARA（查询基于SA的Intelligence训练参数）

## 功能

**适用NF：UPF**

该命令用于查询基于SA的intelligence训练参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SAAITRAINPARA]] · 基于SA的Intelligence训练参数（SAAITRAINPARA）

## 使用实例

如果想查询基于SA的intelligence训练参数，执行以下命令：

```
LST SAAITRAINPARA:;
```

```

RETCODE = 0  操作成功

基于SA的intelligence训练参数
----------------------------
        Intelligence训练阈值  =  9900
        Intelligence训练开关  =  不使能
Intelligence训练周期（分钟）  =  30
      Intelligence训练抽样率  =  0
        SA性能优化库有效时间  =  300
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询基于SA的Intelligence训练参数（LST-SAAITRAINPARA）_69640518.md`
