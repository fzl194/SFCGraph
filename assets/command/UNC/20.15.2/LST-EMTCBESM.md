---
id: UNC@20.15.2@MMLCommand@LST EMTCBESM
type: MMLCommand
name: LST EMTCBESM（查询S1模式eMTC SM协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EMTCBESM
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
- eMTC-SM协议参数管理
status: active
---

# LST EMTCBESM（查询S1模式eMTC SM协议参数）

## 功能

**适用网元：MME**

该命令用于设置S1模式CE Mode B（一种eMTC终端）用户的SM协议参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/EMTCBESM]] · S1模式eMTC SM协议参数（EMTCBESM）

## 使用实例

查询S1模式下CE MODE B用户SM协议参数：

LST EMTCBESM:;

```
%%LST EMTCBESM:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
    T3485 （s）  =  48
N3485 （times）  =  5
    T3486 （s）  =  48
N3486 （times）  =  5
    T3489 （s）  =  48
N3489 （times）  =  5
    T3495 （s）  =  48
N3495 （times）  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1模式eMTC-SM协议参数（LST-EMTCBESM）_26145780.md`
