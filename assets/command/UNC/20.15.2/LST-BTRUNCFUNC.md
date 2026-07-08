---
id: UNC@20.15.2@MMLCommand@LST BTRUNCFUNC
type: MMLCommand
name: LST BTRUNCFUNC（查询宽带集群系统扩展功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BTRUNCFUNC
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 宽带集群系统扩展功能管理
status: active
---

# LST BTRUNCFUNC（查询宽带集群系统扩展功能）

## 功能

**适用NF：MME**

此命令用于查询宽带集群系统扩展功能配置参数。

## 注意事项

无。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/BTRUNCFUNC]] · 宽带集群系统扩展功能（BTRUNCFUNC）

## 使用实例

查询宽带集群系统扩展功能配置参数，执行命令：

```
LST BTRUNCFUNC:;
RETCODE = 0  操作成功。 
```

```
查询结果如下
-------------------------
    是否支持集群业务  =  否

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-BTRUNCFUNC.md`
