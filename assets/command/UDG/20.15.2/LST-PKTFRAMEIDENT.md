---
id: UDG@20.15.2@MMLCommand@LST PKTFRAMEIDENT
type: MMLCommand
name: LST PKTFRAMEIDENT（查询帧包识别功能相关参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PKTFRAMEIDENT
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 帧包识别
- 帧包识别参数
status: active
---

# LST PKTFRAMEIDENT（查询帧包识别功能相关参数）

## 功能

**适用NF：UPF、PGW-U**

该命令用于显示帧包识别功能相关参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [帧包识别功能相关参数（PKTFRAMEIDENT）](configobject/UDG/20.15.2/PKTFRAMEIDENT.md)

## 使用实例

假如运营商希望查看帧包识别相关参数：

```
LST PKTFRAMEIDENT:;
```

```

RETCODE = 0  操作成功
 
帧包识别参数
------------
      帧包识别功能开关  =  使能（开启）
帧包关系学习时间（秒）  =  3
    关键帧识别功能开关  =  不使能（关闭）
(结果个数 = 1)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询帧包识别功能相关参数（LST-PKTFRAMEIDENT）_29298862.md`
