---
id: UNC@20.15.2@MMLCommand@LST NBEMM
type: MMLCommand
name: LST NBEMM（查询NB-S1模式MM协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NBEMM
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- M2M管理
- NB-MM协议参数管理
status: active
---

# LST NBEMM（查询NB-S1模式MM协议参数）

## 功能

**适用网元：MME**

该命令用于查询NB-S1模式MM协议参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/NBEMM]] · NB-S1模式MM协议参数（NBEMM）

## 使用实例

查询NB-S1模式MM协议参数：

LST NBEMM:;

```
%%LST NBEMM:;%%
RETCODE = 0  操作成功。
操作结果如下
----------
                         T3422(s)  =  6
                     N3422(times)  =  4
                         T3450(s)  =  6
                     N3450(times)  =  4
                         T3460(s)  =  6
                     N3460(times)  =  4
                         T3470(s)  =  6
                     N3470(times)  =  4
                         T3413(s)  =  6
                     N3413(times)  =  2
                     SUB_T3413(s)  =  3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NB-S1模式MM协议参数（LST-NBEMM）_72345375.md`
