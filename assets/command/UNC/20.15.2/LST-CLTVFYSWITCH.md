---
id: UNC@20.15.2@MMLCommand@LST CLTVFYSWITCH
type: MMLCommand
name: LST CLTVFYSWITCH（查询双向认证开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CLTVFYSWITCH
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

# LST CLTVFYSWITCH（查询双向认证开关）

## 功能

此命令用于查询双向认证开关的开关状态。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CLTVFYSWITCH]] · 双向认证开关（CLTVFYSWITCH）

## 使用实例

查询双向认证开关：

```
LST CLTVFYSWITCH;
```

```
%%LST CLTVFYSWITCH:;%%
RETCODE = 0  操作成功  
操作结果如下 
------------ 
端口  开关    
6443  关      
9000  关      
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CLTVFYSWITCH.md`
