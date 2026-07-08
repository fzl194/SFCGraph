---
id: UNC@20.15.2@MMLCommand@LST IFDSCPMCR
type: MMLCommand
name: LST IFDSCPMCR（查询接口DSCP配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IFDSCPMCR
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- 接口DSCP管理
- 接口DSCP参数管理
status: active
---

# LST IFDSCPMCR（查询接口DSCP配置）

## 功能

**适用网元：MME**

该命令用来查看MCR_VNFC对外网元接口发送IP包时携带的DSCP值。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [接口DSCP配置（IFDSCPMCR）](configobject/UNC/20.15.2/IFDSCPMCR.md)

## 使用实例

查询MCR_VNFC对外网元接口发送IP包时携带的DSCP配置：

LST IFDSCPMCR:;

```
%%LST IFDSCPMCR:;%%

DSCP查询结果如下
--------------
接口类型                     DSCP值
未指定接口                   56
SDUP                         36

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询接口DSCP配置(LST-IFDSCPMCR)_25131364.md`
