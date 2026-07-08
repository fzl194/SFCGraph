---
id: UNC@20.15.2@MMLCommand@LST CNTMEMTHD
type: MMLCommand
name: LST CNTMEMTHD（查询容器内存阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CNTMEMTHD
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# LST CNTMEMTHD（查询容器内存阈值）

## 功能

该命令用于查询容器内存阈值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

无

## 操作的配置对象

- [容器内存阈值（CNTMEMTHD）](configobject/UNC/20.15.2/CNTMEMTHD.md)

## 使用实例

查询容器内存告警阈值。

```
%%LST CNTMEMTHD:;%%
RETCODE = 0  操作成功

结果如下
------------------------
告警上报门限  =  90
告警恢复门限  =  80
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询容器内存阈值（LST-CNTMEMTHD）_32743961.md`
