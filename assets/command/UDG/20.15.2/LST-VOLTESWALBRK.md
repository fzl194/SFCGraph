---
id: UDG@20.15.2@MMLCommand@LST VOLTESWALBRK
type: MMLCommand
name: LST VOLTESWALBRK（显示VoLTE滑窗相关参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VOLTESWALBRK
command_category: 查询类
applicable_nf:
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- VoLTE吞字断续配置
status: active
---

# LST VOLTESWALBRK（显示VoLTE滑窗相关参数）

## 功能

**适用NF：PGW-U**

该命令用于显示VoLTE吞字断续检测的相关参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [VoLTE滑窗相关的参数（VOLTESWALBRK）](configobject/UDG/20.15.2/VOLTESWALBRK.md)

## 使用实例

显示VoLTE吞字断续检测的相关参数：

```
LST VOLTESWALBRK:;
```

```

RETCODE = 0  操作成功

VoLTE吞字断续检测参数
---------------------
      功能开关  =  不使能（关闭）
  吞字滑窗大小  =  20
吞字的滑窗阈值  =  12
  断续滑窗大小  =  50
断续的滑窗阈值  =  30
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示VoLTE滑窗相关参数（LST-VOLTESWALBRK）_69418608.md`
