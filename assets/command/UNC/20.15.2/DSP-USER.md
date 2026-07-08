---
id: UNC@20.15.2@MMLCommand@DSP USER
type: MMLCommand
name: DSP USER（显示用户锁定状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: USER
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 用户管理
status: active
---

# DSP USER（显示用户锁定状态）

## 功能

**适用NF：NCG**

该命令用于显示用户锁定状态。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USER]] · 用户锁定状态（USER）

## 使用实例

显示用户锁定状态：

```
DSP USER:;
```

```
 
RETCODE = 0  操作成功。

结果如下:
---------
用户名    锁定状态    RU名称           PULL任务标识    

BS        未锁定      CG_SP_RU_0064    Distribution_1st
BS        未锁定      CG_SP_RU_0065    Distribution_1st
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-USER.md`
