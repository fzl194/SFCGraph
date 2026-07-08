---
id: UNC@20.15.2@MMLCommand@LST EMTCBEMM
type: MMLCommand
name: LST EMTCBEMM（查询S1模式eMTC MM协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EMTCBEMM
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- M2M管理
- eMTC-MM协议参数管理
status: active
---

# LST EMTCBEMM（查询S1模式eMTC MM协议参数）

## 功能

**适用网元：MME**

该命令用于查询S1模式eMTC Mode B用户的MM协议参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/EMTCBEMM]] · S1模式eMTC MM协议参数（EMTCBEMM）

## 使用实例

查询S1模式下CE MODE B用户MM协议参数：

```
LST EMTCBEMM:;
```

```
%%LST EMTCBEMM:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
    T3422 （s）  =  48
N3422 （times）  =  5
    T3450 （s）  =  48
N3450 （times）  =  5
    T3460 （s）  =  48
N3460 （times）  =  5
    T3470 （s）  =  48
N3470 （times）  =  5
    T3413 （s）  =  48
N3413 （times）  =  5
SUB_T3413 （s）  =  48
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1模式eMTC-MM协议参数（LST-EMTCBEMM）_72225457.md`
