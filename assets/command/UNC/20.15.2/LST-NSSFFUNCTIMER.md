---
id: UNC@20.15.2@MMLCommand@LST NSSFFUNCTIMER
type: MMLCommand
name: LST NSSFFUNCTIMER（查询NSSF功能时长）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSFFUNCTIMER
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF功能时长管理
status: active
---

# LST NSSFFUNCTIMER（查询NSSF功能时长）

## 功能

**适用NF：NSSF**

该命令用于查询NSSF功能的时长类信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFFUNCTIMER]] · NSSF功能时长（NSSFFUNCTIMER）

## 使用实例

查询NSSF功能的时长类信息：

```
LST NSSFFUNCTIMER:;
%%LST NSSFFUNCTIMER:;%%
RETCODE = 0  操作成功

结果如下
--------
TPS平滑取值周期数  =  20
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NSSF功能时长（LST-NSSFFUNCTIMER）_76718586.md`
