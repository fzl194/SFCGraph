---
id: UNC@20.15.2@MMLCommand@LST IUSM
type: MMLCommand
name: LST IUSM（查询Iu模式SM协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IUSM
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- SM协议参数管理
- Iu模式SM协议参数
status: active
---

# LST IUSM（查询Iu模式SM协议参数）

## 功能

**适用网元：SGSN**

此命令用于查询IUSM协议配置信息，包括PDP上下文的激活、修改、去活流程相关定时器的值等。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [Iu模式SM协议参数（IUSM）](configobject/UNC/20.15.2/IUSM.md)

## 使用实例

查询IUSM协议配置信息：

LST IUSM:;

```
%%LST IUSM:;%%
RETCODE = 0  操作成功。

IUSM参数配置表
--------------
    T3385(s)  =  10
N3385(times)  =  4
    T3386(s)  =  10
N3386(times)  =  4
    T3395(s)  =  8
N3395(times)  =  4
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Iu模式SM协议参数(LST-IUSM)_72345299.md`
