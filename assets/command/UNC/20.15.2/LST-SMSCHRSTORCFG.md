---
id: UNC@20.15.2@MMLCommand@LST SMSCHRSTORCFG
type: MMLCommand
name: LST SMSCHRSTORCFG（查询SMS小范围CHR存储配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSCHRSTORCFG
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- CHR管理
status: active
---

# LST SMSCHRSTORCFG（查询SMS小范围CHR存储配置）

## 功能

**适用NF：SMSF**

该命令用于查询SMS小范围CHR存储配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSCHRSTORCFG]] · SMS小范围CHR存储配置（SMSCHRSTORCFG）

## 使用实例

运营商希望查询SMS小范围CHR存储配置，执行如下命令：

```
LST SMSCHRSTORCFG:;
%%LST SMSCHRSTORCFG:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
小范围CHR使能开关 =  打开
小范围CHR存储路径  =  保存到OMU
       
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSCHRSTORCFG.md`
