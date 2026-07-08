---
id: UNC@20.15.2@MMLCommand@LST LINKMIGCTRL
type: MMLCommand
name: LST LINKMIGCTRL（查询链路迁移控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LINKMIGCTRL
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- 链路管理
status: active
---

# LST LINKMIGCTRL（查询链路迁移控制参数）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询链路迁移控制参数，涉及的链路接口类型为Ga/Gx/Gy/S6b。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [链路迁移控制参数（LINKMIGCTRL）](configobject/UNC/20.15.2/LINKMIGCTRL.md)

## 使用实例

查询链路迁移控制参数：

```
%%LST LINKMIGCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
     容器CPU阈值  = 65
链路均分时间间隔  = 2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询链路迁移控制参数（LST-LINKMIGCTRL）_81482578.md`
