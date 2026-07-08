---
id: UNC@20.15.2@MMLCommand@LST IFMTUFRAGMODE
type: MMLCommand
name: LST IFMTUFRAGMODE（查询分片方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IFMTUFRAGMODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP性能配置
- 分片方式配置
status: active
---

# LST IFMTUFRAGMODE（查询分片方式）

## 功能

该命令用来查询当前分片方式。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [分片方式（IFMTUFRAGMODE）](configobject/UNC/20.15.2/IFMTUFRAGMODE.md)

## 使用实例

查询当前接口分片方式：

```
LST IFMTUFRAGMODE:;
```

```

RETCODE = 0 操作成功                                                
                                                                                

结果如下                                                        
------------------------                                                        
分片方式  =  标签加IP分片方式                                                                
(结果个数 = 1)                                                                                                             
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询分片方式（LST-IFMTUFRAGMODE）_49961402.md`
