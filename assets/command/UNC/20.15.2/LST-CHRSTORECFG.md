---
id: UNC@20.15.2@MMLCommand@LST CHRSTORECFG
type: MMLCommand
name: LST CHRSTORECFG（查询CHR存盘配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHRSTORECFG
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- CHR管理
- CHR存盘管理
status: active
---

# LST CHRSTORECFG（查询CHR存盘配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询系统上配置的 ucf 是否进行CHR单据本地存储的策略。

## 注意事项

只有在 “CHR存储开关” 参数配置为 “ON(开)” 时， “存储类型” 才会被输出。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [CHR存盘配置（CHRSTORECFG）](configobject/UNC/20.15.2/CHRSTORECFG.md)

## 使用实例

查询CHR存盘配置：

LST CHRSTORECFG:;

```
%%LST CHRSTORECFG:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
    CHR存储开关  =  开
       存储类型  =  仅存储
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CHR存盘配置(LST-CHRSTORECFG)_72225297.md`
