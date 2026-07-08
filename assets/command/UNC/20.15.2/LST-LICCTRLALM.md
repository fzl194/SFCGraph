---
id: UNC@20.15.2@MMLCommand@LST LICCTRLALM
type: MMLCommand
name: LST LICCTRLALM（查询License容量告警配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LICCTRLALM
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# LST LICCTRLALM（查询License容量告警配置）

## 功能

该命令用于查询系统中License容量告警配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [License容量告警配置（LICCTRLALM）](configobject/UNC/20.15.2/LICCTRLALM.md)

## 使用实例

查询系统中当前的容量告警配置信息：

```
%%LST LICCTRLALM:;%%
RETCODE = 0  操作成功

操作结果如下
------------
    容量告警百分比(%)  =  80
容量告警恢复百分比(%)  =  70
          持续时间(h)  =  3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询License容量告警配置（LST-LICCTRLALM）_09653686.md`
