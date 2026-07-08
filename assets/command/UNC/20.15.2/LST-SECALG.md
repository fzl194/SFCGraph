---
id: UNC@20.15.2@MMLCommand@LST SECALG
type: MMLCommand
name: LST SECALG（查询安全算法）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SECALG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 安全算法配置
status: active
---

# LST SECALG（查询安全算法）

## 功能

该命令用于查询建链时使用的安全算法的开关状态。开关打开时该算法可以使用，关闭时该算法被禁用。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SECALG]] · 安全算法（SECALG）

## 使用实例

查询安全算法的开关状态。

```
%%LST SECALG:;%% 
RETCODE = 0  操作成功
  
操作结果如下 
------------ 
算法类型  =  DHE     
开关  =  关
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SECALG.md`
