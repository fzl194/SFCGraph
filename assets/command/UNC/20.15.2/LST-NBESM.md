---
id: UNC@20.15.2@MMLCommand@LST NBESM
type: MMLCommand
name: LST NBESM（查询NB-S1模式SM协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NBESM
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
- NB-SM协议参数管理
status: active
---

# LST NBESM（查询NB-S1模式SM协议参数）

## 功能

**适用网元：MME**

该命令用于查询NB-S1模式SM协议参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [NB-S1模式SM协议参数（NBESM）](configobject/UNC/20.15.2/NBESM.md)

## 使用实例

执行如下命令查询NB-S1模式SM协议参数：

LST NBESM:;

```
%%LST NBESM:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
    T3485(s)  =  8
N3485(times)  =  4
    T3486(s)  =  8
N3486(times)  =  4
    T3489(s)  =  4
N3489(times)  =  2
    T3495(s)  =  8
N3495(times)  =  4
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NB-S1模式SM协议参数（LST-NBESM）_26305586.md`
