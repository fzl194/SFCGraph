---
id: UNC@20.15.2@MMLCommand@LST CHRFILESTGMODE
type: MMLCommand
name: LST CHRFILESTGMODE（查询上传至文件服务器的CHR文件转储方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHRFILESTGMODE
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

# LST CHRFILESTGMODE（查询上传至文件服务器的CHR文件转储方式）

## 功能

该命令用于查询上传至文件服务器的CHR文件转储信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [上传至文件服务器的CHR文件转储方式（CHRFILESTGMODE）](configobject/UNC/20.15.2/CHRFILESTGMODE.md)

## 使用实例

用户需要查看当前上传至文件服务器CHR文件转储信息时，直接调用该命令：

```
LST CHRFILESTGMODE:;
RETCODE = 0  操作成功

结果如下
--------
是否开启上传CHR文件到文件服务器  =  否
             文件转储大小（MB）  =  50
           文件转储周期（分钟）  =  30
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询上传至文件服务器的CHR文件转储方式（LST-CHRFILESTGMODE）_28275345.md`
