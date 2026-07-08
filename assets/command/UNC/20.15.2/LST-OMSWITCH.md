---
id: UNC@20.15.2@MMLCommand@LST OMSWITCH
type: MMLCommand
name: LST OMSWITCH（查询OM功能开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OMSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 代理管理
status: active
---

# LST OMSWITCH（查询OM功能开关）

## 功能

此命令用于查询OM功能开关的开关状态。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [OM功能开关（OMSWITCH）](configobject/UNC/20.15.2/OMSWITCH.md)

## 使用实例

查询OM功能开关：

```
%%LST OMSWITCH:;%%
RETCODE = 0  操作成功  
操作结果如下 
------------ 
功能  =  Portal 
开关  =  开 
(结果个数 = 1)  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OM功能开关（LST-OMSWITCH）_86522834.md`
