---
id: UDG@20.15.2@MMLCommand@LST CHRFILESAVETIME
type: MMLCommand
name: LST CHRFILESAVETIME（查询文件存留期设置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CHRFILESAVETIME
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- Chr管理
- Chr文件管理
status: active
---

# LST CHRFILESAVETIME（查询文件存留期设置）

## 功能

用于查看文件最大保留时间以及存留期设置是否生效。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/CHRFILESAVETIME]] · 文件存留期设置（CHRFILESAVETIME）

## 使用实例

用户需要查看当前的chr存留期的设置时，直接调用该命令，无需参数，系统会返回文件存留期限以及存留是否开启。

```
%%LST CHRFILESAVETIME:;%%
RETCODE = 0  操作成功

结果如下
--------
是否开启存留期功能  =  启用存留期控制
  文件最大保留天数  =  180
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询文件存留期设置（LST-CHRFILESAVETIME）_14567104.md`
