---
id: UNC@20.15.2@MMLCommand@LST CERTESCAPESWITCH
type: MMLCommand
name: LST CERTESCAPESWITCH（查询证书过期逃生开关状态）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CERTESCAPESWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 证书维护
status: active
---

# LST CERTESCAPESWITCH（查询证书过期逃生开关状态）

## 功能

查询证书过期逃生开关状态。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CERTESCAPESWITCH]] · 证书过期逃生开关状态（CERTESCAPESWITCH）

## 使用实例

查询证书过期逃生开关状态。

```
%%LST CERTESCAPESWITCH:;%% 
RETCODE = 0  操作成功
  
操作结果如下 
------------ 
证书过期逃生开关状态  =  关 
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询证书过期逃生开关状态（LST-CERTESCAPESWITCH）_06110022.md`
