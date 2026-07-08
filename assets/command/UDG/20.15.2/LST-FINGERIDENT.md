---
id: UDG@20.15.2@MMLCommand@LST FINGERIDENT
type: MMLCommand
name: LST FINGERIDENT（查询SA指纹识别配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FINGERIDENT
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 协议识别
- SA指纹识别
- SA指纹识别
status: active
---

# LST FINGERIDENT（查询SA指纹识别配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询整机配置的SA指纹识别功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/FINGERIDENT]] · SA指纹识别配置（FINGERIDENT）

## 使用实例

查询所有SA指纹识别功能的配置信息：

```
LST FINGERIDENT:;
```

```

RETCODE = 0  操作成功

指纹识别配置信息
----------------
协议名称      指纹识别结果控制开关  指纹识别开关    配置域名称  

facebook      只做统计              使能（开启）    NULL        
youtube       不使能                使能（开启）    NULL        
all-protocol  不使能                不使能（关闭）  NULL        
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FINGERIDENT.md`
