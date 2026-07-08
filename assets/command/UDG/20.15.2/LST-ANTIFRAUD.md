---
id: UDG@20.15.2@MMLCommand@LST ANTIFRAUD
type: MMLCommand
name: LST ANTIFRAUD（查询防欺诈配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ANTIFRAUD
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- 防欺诈参数
status: active
---

# LST ANTIFRAUD（查询防欺诈配置）

## 功能

**适用NF：PGW-U、UPF**

此命令用于查询当前系统的防欺诈相关参数的配置信息。包括DNS防欺诈开关、FUI防欺诈开关、HTTP防欺诈开关的开启状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/ANTIFRAUD]] · 防欺诈配置（ANTIFRAUD）

## 使用实例

假如运营商需要查看防欺诈功能的配置，则命令如下：

```
LST ANTIFRAUD:;
```

```

RETCODE = 0  操作成功。

防欺诈信息
----------
  空记录DNS防欺诈开关  =  使能
文本记录DNS防欺诈开关  =  不使能
  启发式DNS防欺诈开关  =  不使能
        FUI防欺诈开关  =  不使能
     HTTP防欺诈总开关  =  不使能
  URL重定向防欺诈开关  =  不使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询防欺诈配置（LST-ANTIFRAUD）_82837793.md`
