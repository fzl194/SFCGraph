---
id: UNC@20.15.2@MMLCommand@LST APPINFO
type: MMLCommand
name: LST APPINFO（查询应用信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APPINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 应用管理
status: active
---

# LST APPINFO（查询应用信息）

## 功能

本命令用于查询网元的实例信息。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/APPINFO]] · 应用信息（APPINFO）

## 使用实例

查询 UNC 网元的应用实例信息：

```
%%LST APPINFO:;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
      网元ID  =  0
    网元类型  =  
UNC

    应用名称  =  
UNC

    应用版本  =  22.1.0.B220
应用补丁版本  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询应用信息(LST-APPINFO)_15736940.md`
