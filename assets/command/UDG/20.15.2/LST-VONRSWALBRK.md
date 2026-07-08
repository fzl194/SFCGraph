---
id: UDG@20.15.2@MMLCommand@LST VONRSWALBRK
type: MMLCommand
name: LST VONRSWALBRK（显示VoNR滑窗相关参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VONRSWALBRK
command_category: 查询类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoNR质量监控配置
- VoNR吞字断续配置
status: active
---

# LST VONRSWALBRK（显示VoNR滑窗相关参数）

## 功能

**适用NF：UPF**

该命令用于显示VoNR吞字断续检测的相关参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/VONRSWALBRK]] · VoNR滑窗相关的参数（VONRSWALBRK）

## 使用实例

显示VoNR吞字断续检测的相关参数：

```
LST VONRSWALBRK:;
```

```

RETCODE = 0  操作成功

VoNR吞字断续检测参数
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

- 原始手册：`evidence/UDG/20.15.2/显示VoNR滑窗相关参数（LST-VONRSWALBRK）_91056086.md`
