---
id: UNC@20.15.2@MMLCommand@LST NWDAFINFOEXT
type: MMLCommand
name: LST NWDAFINFOEXT（查询NWDAF扩展信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NWDAFINFOEXT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- NWDAF
status: active
---

# LST NWDAFINFOEXT（查询NWDAF扩展信息）

## 功能

该命令用以查询NWDAF实例的扩展信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NWDAF扩展信息（NWDAFINFOEXT）](configobject/UNC/20.15.2/NWDAFINFOEXT.md)

## 使用实例

查询NWDAF实例的扩展信息：

```
%%LST NWDAFINFOEXT:;%%
RETCODE = 0  操作成功

结果如下
--------
NWDAF实例名称  =  NWDAF_Instance_0
           ID  =  central
NWDAF事件类型  =  QOS分析
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NWDAF扩展信息（LST-NWDAFINFOEXT）_14059357.md`
