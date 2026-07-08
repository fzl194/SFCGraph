---
id: UNC@20.15.2@MMLCommand@LST GLBCHRFUNC
type: MMLCommand
name: LST GLBCHRFUNC（查询全局CHR功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBCHRFUNC
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- CHR管理
- 全局CHR功能配置
status: active
---

# LST GLBCHRFUNC（查询全局CHR功能配置）

## 功能

**适用NF：SGW-C、PGW-C、GGSN、SMF**

该命令用于查询全局CHR功能配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [全局CHR功能配置（GLBCHRFUNC）](configobject/UNC/20.15.2/GLBCHRFUNC.md)

## 使用实例

查询全局CHR上报功能配置：

```
%%LST GLBCHRFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
                 CHR上报开关  =  使能
             支持上报CHR的会话数 = 0
        支持上报小范围CHR的会话数 = 3
支持上报小范围CHR的用户会话老化时长 = 24
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局CHR功能配置（LST-GLBCHRFUNC）_89350516.md`
