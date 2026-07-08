---
id: UNC@20.15.2@MMLCommand@LST HSMFCHGCTRL
type: MMLCommand
name: LST HSMFCHGCTRL（查询漫游用户在归属地的计费方式和漫游参数的协商方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HSMFCHGCTRL
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- QBC计费控制
status: active
---

# LST HSMFCHGCTRL（查询漫游用户在归属地的计费方式和漫游参数的协商方式）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询漫游用户在归属地的计费方式和Roaming Charging Profile的协商方式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HSMFCHGCTRL]] · 漫游用户在归属地的计费方式和漫游参数的协商方式（HSMFCHGCTRL）

## 使用实例

查询漫游用户在归属地的计费方式和Roaming Charging Profile的协商方式：

```
%%LST HSMFCHGCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
               计费模式  =  QBC计费
FBC计费漫游参数协商开关  =  不使能
   本地漫游参数获取方式  =  使用本地配置
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HSMFCHGCTRL.md`
